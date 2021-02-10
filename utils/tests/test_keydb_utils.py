import os
import unittest
import redis
import keydb
from utils import keydb_utils


class KeydbUtilsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        REDIS_HOST = '127.0.0.1'
        REDIS_PORT = 6379
        cls.REDIS_CONNECTION_POOL = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=0)

    def test_1(self):
        self.assertIsInstance(self.REDIS_CONNECTION_POOL, redis.connection.ConnectionPool)

    def test_2(self):
        cache = keydb.KeyDB(connection_pool=self.REDIS_CONNECTION_POOL)
        cache.ping()
