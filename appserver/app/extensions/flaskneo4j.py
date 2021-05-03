import logging
from neo4j import GraphDatabase
from flask import _app_ctx_stack

logging.getLogger('neo4j').setLevel('DEBUG')

class FlaskNeo4j(object):
    def __init__(self, app=None):
        self.app = app
        self.driver = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('NEO4J_PROTOCOL', 'bolt')
        app.config.setdefault('NEO4J_PORT', 7687)
        app.config.setdefault('NEO4J_MAX_POOL_SIZE', 1000)
        app.config.setdefault('NEO4J_MAX_CONN_TIME', 3600)
        app.config.setdefault('NEO4J_KEEP_ALIVE', True)
        print(f'Neo4j Host: {app.config["NEO4J_HOST"]}')
        print(f'Neo4j Port: {app.config["NEO4J_PORT"]}')
        graph_url = '{protocol}://{host}:{port}'.format(
            protocol=app.config["NEO4J_PROTOCOL"],
            host=app.config["NEO4J_HOST"],
            port=app.config["NEO4J_PORT"]
        )
        config_params = {
            'auth': (app.config['NEO4J_USER'], app.config['NEO4J_PASSWORD']),
            # 'max_connection_lifetime': 15,
            # 'max_connection_pool_size': 2,
        }
        # GraphDatabase.driver(uri, auth=("neo4j", "password"), max_connection_lifetime=1000)
        self.driver = GraphDatabase.driver(graph_url, **config_params)

    def teardown(self, exc):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'neo4j_db'):
            ctx.neo4j_db.close()

    @property
    def session(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'neo4j_db'):
                ctx.neo4j_db = self.driver.session()
            return ctx.neo4j_db