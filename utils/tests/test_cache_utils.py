import unittest
from utils import cache_utils


class CacheUtilsTestCase(unittest.TestCase):

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
