import os
import urllib.parse
import keydb


def create_pool():
    keydb_url = urllib.parse.urlparse(os.environ.get('KEYDB_URL'))
    keydb_pool = keydb.ConnectionPool(host=keydb_url.hostname, port=keydb_url.port, password=keydb_url.password)
    return keydb_pool
