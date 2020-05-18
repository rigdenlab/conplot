import unittest
from utils import session_utils, compress_data


class SessionUtilsTestCase(unittest.TestCase):

    def test_1(self):
        test_input = {b'dummy_key_1': compress_data(['dummy_value_1', 'dummy_fname_1']),
                      b'dummy_key_2': compress_data(['dummy_value_2', 'dummy_fname_2'])}
        expected_output = {b'dummy_key_1': ['dummy_value_1'], b'dummy_key_2': ['dummy_value_2']}

        self.assertDictEqual(expected_output, session_utils.decompress_session(test_input))
