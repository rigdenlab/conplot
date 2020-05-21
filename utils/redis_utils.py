import os
import urllib.parse
import redis


def create_pool():
    redis_url = urllib.parse.urlparse(os.environ.get('REDISCLOUD_URL'))
    redis_pool = redis.ConnectionPool(host=redis_url.hostname, port=redis_url.port, password=redis_url.password)
    return redis_pool
