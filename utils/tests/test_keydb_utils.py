import unittest
import redis
import keydb
from utils import keydb_utils


class KeydbUtilsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.keydb_pool = keydb_utils.create_pool('redis://127.0.0.1:6379')

    def test_1(self):
        self.assertIsInstance(self.keydb_pool, redis.connection.ConnectionPool)

    def test_2(self):
        cache = keydb.KeyDB(connection_pool=self.keydb_pool)
        cache.ping()
