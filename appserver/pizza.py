import click
import os
from flask import jsonify, g
from app import create_app, db
from app.models import Account
from uuid import getnode as get_mac
from guppy import hpy

app_config = os.environ['FLASK_APP_CONFIG']
app = create_app(config=f'config.{app_config}')

@app.before_request
def before():
    hp = hpy()
    before = hp.heap()
    g.heapy = (hp, before)

@app.teardown_appcontext
def teardown(err):
    if 'heapy' in g:
        heapy, before = g.heapy
        after = heapy.heap()
        print(after - before)

@app.route('/', methods=['GET'])
def home():
    return jsonify(dict(result=f'Ready to rule the world at {get_mac}')), 200

@app.cli.command('create-user')
@click.argument('name')
def create_user(name):
    user = Account(username=name, email=f'{name}@pizza.co')
    db.session.add(user)
    db.session.commit()

