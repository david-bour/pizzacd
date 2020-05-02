from app import db, ma
from marshmallow import Schema

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True, unique=True)

class AccountSchema(Schema):
    class Meta:
        model = Account

    _links = ma.Hyperlinks(
        {'self': ma.URLFor('user_detail', id='<id>'), 'collection': ma.URLFor('users')}
    )

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)
