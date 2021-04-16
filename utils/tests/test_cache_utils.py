import unittest
import keydb
import logging
from utils import cache_utils, keydb_utils, session_utils


class CacheUtilsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        keydb_pool = keydb_utils.create_pool('redis://127.0.0.1:6379')
        cls.cache = keydb.KeyDB(connection_pool=keydb_pool)
        cls.session_id = session_utils.initiate_session(cls.cache, logging.getLogger())

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

    def test_4(self):
        cache_utils.store_fname(self.cache, self.session_id, 'dummy_fname_1', 'dummy_key')
        self.assertTrue(self.cache.hexists(self.session_id, 'dummy_key'))
        expected = cache_utils.compress_data(['dummy_fname_1'])
        self.assertEqual(self.cache.hget(self.session_id, 'dummy_key'), expected)

        cache_utils.store_fname(self.cache, self.session_id, 'dummy_fname_2', 'dummy_key')
        expected = cache_utils.compress_data(['dummy_fname_1', 'dummy_fname_2'])
        self.assertEqual(self.cache.hget(self.session_id, 'dummy_key'), expected)
        self.cache.hdel(self.session_id, 'dummy_key')

    def test_5(self):
        self.assertIsNone(cache_utils.remove_fname(self.cache, self.session_id, 'dummy_fname', 'dummy_key'))
        cache_utils.store_fname(self.cache, self.session_id, 'dummy_fname_1', 'dummy_key')
        cache_utils.store_fname(self.cache, self.session_id, 'dummy_fname_2', 'dummy_key')

        cache_utils.remove_fname(self.cache, self.session_id, 'dummy_fname_1', 'dummy_key')
        expected = cache_utils.compress_data(['dummy_fname_2'])
        self.assertEqual(self.cache.hget(self.session_id, 'dummy_key'), expected)

        cache_utils.remove_fname(self.cache, self.session_id, 'dummy_fname_2', 'dummy_key')
        expected = cache_utils.compress_data([])
        self.assertEqual(self.cache.hget(self.session_id, 'dummy_key'), expected)
        self.cache.hdel(self.session_id, 'dummy_key')

    def test_6(self):
        cache_utils.store_fname(self.cache, self.session_id, 'dummy_fname', 'sequence')
        cache_utils.store_fname(self.cache, self.session_id, 'dummy_fname', 'hydrophobicity')
        cache_utils.remove_fname(self.cache, self.session_id, 'dummy_fname', 'sequence')
        self.assertIsNone(self.cache.hget(self.session_id, 'sequence'))
        self.assertIsNone(self.cache.hget(self.session_id, 'hydrophobicity'))

    def test_7(self):
        cache_utils.store_figure(self.session_id, 'figure_json', 'display_control_json', self.cache)
        expected = cache_utils.compress_data('figure_json')
        self.assertEqual(self.cache.hget(self.session_id, 'figure_json'), expected)
        expected = cache_utils.compress_data('display_control_json')
        self.assertEqual(self.cache.hget(self.session_id, 'display_control_json'), expected)

    def test_8(self):
        self.cache.hset(self.session_id, 'dummy_fname', 'sequence_data')
        self.cache.hset(self.session_id, 'hydrophobicity', 'seq_hydrophobicity')
        self.cache.hset(self.session_id, 'sequence', cache_utils.compress_data('dummy_fname'))
        cache_utils.store_fname(self.cache, self.session_id, 'dummy_fname_1', 'contact')
        cache_utils.store_fname(self.cache, self.session_id, 'dummy_fname_2', 'disorder')
        cache_utils.store_figure(self.session_id, 'figure_json', 'display_control_json', self.cache)
        cache_utils.clear_cache(self.session_id, self.cache)
        expected = {b'id': cache_utils.compress_data(self.session_id)}
        self.assertDictEqual(expected, self.cache.hgetall(self.session_id))

    def test_9(self):
        cachekey_1 = 'fname_1_{}_2'.format(cache_utils.CacheKeys.METADATA_TAG.value).encode()
        density_1 = [1, 2, 3, 3, 4, 5]
        cachekey_2 = 'fname_2_{}_2'.format(cache_utils.CacheKeys.METADATA_TAG.value).encode()
        density_2 = [5, 6, 7, 8, 9, 0]

        cache_utils.store_density(self.session_id, cachekey_1, density_1, self.cache)
        cache_utils.store_density(self.session_id, cachekey_2, density_2, self.cache)
        output = cache_utils.retrieve_density(self.session_id, cachekey_2, self.cache)
        self.assertListEqual(output, density_2)
        expected_cache = {b'id': cache_utils.compress_data(self.session_id)}
        cache_utils.remove_all_density(self.session_id, self.cache)
        self.assertDictEqual(expected_cache, self.cache.hgetall(self.session_id))
