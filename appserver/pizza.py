import click
import os
import jsonify
from app import create_app, db
from app.models import Account

app_config = os.environ['FLASK_APP_CONFIG']
app = create_app(config=f'config.{app_config}')

@app.route('/', methods=['GET'])
def home():
    return jsonify(dict(result='Home runn!!!')), 200

@app.cli.command('create-user')
@click.argument('name')
def create_user(name):
    user = Account(username=name, email=f'{name}@pizza.co')
    db.session.add(user)
    db.session.commit()

