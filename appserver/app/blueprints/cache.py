from flask import Blueprint, jsonify
from app import r as cache

bp = Blueprint('cache', __name__, url_prefix='/cache')

@bp.route('/<topic>', methods=['GET'])
def get_cache(topic):
    data = cache.get(topic)
    if data is None:
        data = 'No topic'
    else:
        data = data.decode('utf-8')

    return jsonify(dict(result=data)), 200

@bp.route('/<topic>', methods=['POST'])
def add_cache(topic):
    cache.set(topic, topic)
    return jsonify(dict(result=topic)), 200
