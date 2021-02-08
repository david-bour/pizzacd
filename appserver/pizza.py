import click
import os
from flask import jsonify
from app import create_app, db
from app.models import Account
from debugger import initialize_flask_server_debugger_if_needed
from uuid import getnode as get_mac

initialize_flask_server_debugger_if_needed()

app_config = os.environ['FLASK_APP_CONFIG']
app = create_app(config=f'config.{app_config}')

@app.route('/', methods=['GET'])
def home():
    return jsonify(dict(result=f'Ready to rule the world at {get_mac}')), 200

@app.cli.command('create-user')
@click.argument('name')
def create_user(name):
    user = Account(username=name, email=f'{name}@pizza.co')
    db.session.add(user)
    db.session.commit()

