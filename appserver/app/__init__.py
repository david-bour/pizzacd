import os
import redis
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.utils import find_modules, import_string

BLUEPRINT_PACKAGE = __package__ + '.blueprints'
BLUEPRINT_OBJNAME = 'bp'

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()

r = redis.Redis(
    host=os.environ.get('REDIS_HOST'),
    password=os.environ.get('REDIS_PASSWORD'),
    port=os.environ.get('REDIS_PORT'),
    ssl=os.environ.get('REDIS_SSL') in ['True', 'true'],
)

def create_app(name='application', config='config.Development'):
    app = Flask(name)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app, resources={"*": {"origins": "*"}})

    register_blueprints(app, BLUEPRINT_PACKAGE)
    return app

def register_blueprints(app, pkgname):
    for name in find_modules(pkgname):
        mod = import_string(name)
        if hasattr(mod, BLUEPRINT_OBJNAME):
            app.register_blueprint(mod.bp)
