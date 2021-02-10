import unittest
import keydb
from utils import cache_utils, keydb_utils


class CacheUtilsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        keydb_pool = keydb_utils.create_pool('redis://127.0.0.1:6379')
        cls.cache = keydb.KeyDB(connection_pool=keydb_pool)

    def test_1(self):
        dummy_data = [x for x in range(0, 100)]
        compressed_data = cache_utils.compress_data(dummy_data)
        decompressed_data = cache_utils.decompress_data(compressed_data)
        self.assertListEqual(dummy_data, decompressed_data)

    def test_2(self):
        dummy_data = ['a' for x in range(0, 100)]
        compressed_data = cache_utils.compress_data(dummy_data)
        decompressed_data = cache_utils.decompress_data(compressed_data)
        self.assertListEqual(dummy_data, decompressed_data)

    def test_3(self):
        self.assertTrue(cache_utils.is_redis_available(self.cache))