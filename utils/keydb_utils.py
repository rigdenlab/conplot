import keydb
import urllib.parse


def create_pool(url):
    keydb_url = urllib.parse.urlparse(url)
    keydb_pool = keydb.ConnectionPool(host=keydb_url.hostname, port=keydb_url.port, password=keydb_url.password)
    return keydb_pool
