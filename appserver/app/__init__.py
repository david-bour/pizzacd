import logging
from logging.config import dictConfig
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.utils import find_modules, import_string
from app.extensions import FlaskNeo4j
from flask_caching import Cache

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

BLUEPRINT_PACKAGE = __package__ + '.blueprints'
BLUEPRINT_OBJNAME = 'bp'

cache = Cache()
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()
neo4j = FlaskNeo4j()

def create_app(name='application', config='config.Development'):
    app = Flask(name)
    app.config.from_object(config)

    neo4j.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app, resources={"*": {"origins": "*"}})
    cache_config = {
        'CACHE_TYPE': 'simple',
        'CACHE_THRESHOLD': 10,
    }
    cache.init_app(app, config=cache_config)

    register_blueprints(app, BLUEPRINT_PACKAGE)
    return app

def register_blueprints(app, pkgname):
    for name in find_modules(pkgname):
        mod = import_string(name)
        if hasattr(mod, BLUEPRINT_OBJNAME):
            app.register_blueprint(mod.bp)
