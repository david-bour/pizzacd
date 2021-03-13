import os
import redis
import time
from flask import Blueprint, jsonify, g

def get_redis():

    # This for sure creates multiple connections
    # r = redis.Redis(
    #     host=os.environ.get('REDIS_HOST'),
    #     password=os.environ.get('REDIS_PASSWORD'),
    #     port=os.environ.get('REDIS_PORT'),
    #     ssl=os.environ.get('REDIS_SSL') in ['True', 'true'],
    # )
    # return r

    if 'redis' not in g:
        r = redis.Redis(
            host=os.environ.get('REDIS_HOST'),
            password=os.environ.get('REDIS_PASSWORD'),
            port=os.environ.get('REDIS_PORT'),
            ssl=os.environ.get('REDIS_SSL') in ['True', 'true'],
        )
        g.redis = r
    return g.redis

bp = Blueprint('cache', __name__, url_prefix='/cache')

@bp.route('/<topic>', methods=['GET'])
def get_cache(topic):
    cache = get_redis()
    data = cache.get(topic)
    if data is None:
        data = 'No topic'
    else:
        data = data.decode('utf-8')
    # time.sleep(10)
    return jsonify(dict(result=data)), 200

@bp.route('/<topic>', methods=['POST'])
def add_cache(topic):
    cache = get_redis()
    cache.set(topic, topic)
    return jsonify(dict(result=topic)), 200

@bp.route('/info', methods=['GET'])
def info():
    cache = get_redis()
    redis_client_id = cache.client_id()
    redis_connected_clients = cache.client_list()
    return jsonify(dict(client_id=redis_client_id, connected_clients=len(redis_connected_clients))), 200
