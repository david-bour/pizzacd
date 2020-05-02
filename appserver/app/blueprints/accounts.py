from flask import Blueprint
from app.models import Account, accounts_schema

bp = Blueprint('accounts', __name__, url_prefix='/accounts')

@bp.route('/', methods=['GET'])
def accounts():
    accounts = Account.query.all()
    return accounts_schema.dump(accounts)
