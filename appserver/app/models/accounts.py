from app import db, ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True, unique=True)

class AccountSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Account
        load_instance = True

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)
