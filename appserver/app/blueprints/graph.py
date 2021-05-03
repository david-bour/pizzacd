from flask import Blueprint, jsonify
from app import neo4j
import random

bp = Blueprint('graph', __name__, url_prefix='/graph')

def create_pizza(tx, name):
    result = tx.run('CREATE (n:Pizza { name: $name }) RETURN id(n) AS node_id', name=name)
    record = result.single()
    return record['node_id']

def get_pizza(tx):
    result = tx.run('MATCH (n:Pizza) RETURN n.name as name')
    records = [record['name'] for record in result]
    return records

@bp.route('/', methods=['GET'])
def get_pizzas():
    pizzas = neo4j.session.read_transaction(get_pizza)
    return jsonify(dict(pizzas=pizzas))

@bp.route('/<name>', methods=['POST'])
def make_pizza(name):
    node_id = neo4j.session.write_transaction(create_pizza, f'{name}-{random.randint(1, 100)}')
    return jsonify(dict(pizza_id=node_id))
