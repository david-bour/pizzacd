from flask import Blueprint, jsonify
from app.models import Account, accounts_schema

bp = Blueprint('accounts', __name__, url_prefix='/accounts')

@bp.route('/', methods=['GET'])
def accounts():
    accounts = Account.query.all()
    data = [account.username for account in accounts]
    data = [f'hello {name}! :)' for name in data]
    return jsonify(dict(result=data))
