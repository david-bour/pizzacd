import click
import os
from app import create_app, db
from app.models import Account

app_config = os.environ['FLASK_APP_CONFIG']
app = create_app(config=f'config.{app_config}')

@app.cli.command('create-user')
@click.argument('name')
def create_user(name):
    user = Account(username=name)
    db.session.add(user)
    db.session.commit()

