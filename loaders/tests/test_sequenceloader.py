import unittest
from loaders import SequenceLoader
from utils import compress_data


class SequenceLoaderTestCase(unittest.TestCase):

    def test_1(self):
        dummy_raw_file = 'data:application/octet-stream;base64,PnRyfFc5RFkyOHxXOURZMjhfTUVUVEkgUHV0YXRpdmUgbWVtYnJhbmU'\
                         'gcHJvdGVpbiBPUz1NZXRoYW5vbG9idXMgdGluZGFyaXVzIERTTSAyMjc4IE9YPTEwOTAzMjIgR049TWV0dGlEUkFGVF8'\
                         'yMDU1IFBFPTQgU1Y9MQpNU0xFQVRWTERMTFNTRlBIV0xBVE1WSUdBTVBJRkVMUkdBSVBJQUxHSVlETVNQVlNBRklGQVZ'\
                         'MR05NSVBWVlBMTExGTERQVlNUWUxSUkZBSUZES0ZGU1dMRkdSVEhSTkhTRVJGRUtZR1RMQUxUTEZWQVZQTFBWVEdBV1R'\
                         'HQ0FBQUZWRkdJS0ZSSEFGUEFJTEFHVkxJQUdJSVZTU1ZUTEdHSUdMVkRMRlMKCg=='

        expected_data = compress_data(
            ['M', 'S', 'L', 'E', 'A', 'T', 'V', 'L', 'D', 'L', 'L', 'S', 'S', 'F', 'P', 'H', 'W', 'L', 'A', 'T', 'M',
             'V', 'I', 'G', 'A', 'M', 'P', 'I', 'F', 'E', 'L', 'R', 'G', 'A', 'I', 'P', 'I', 'A', 'L', 'G', 'I', 'Y',
             'D', 'M', 'S', 'P', 'V', 'S', 'A', 'F', 'I', 'F', 'A', 'V', 'L', 'G', 'N', 'M', 'I', 'P', 'V', 'V', 'P',
             'L', 'L', 'L', 'F', 'L', 'D', 'P', 'V', 'S', 'T', 'Y', 'L', 'R', 'R', 'F', 'A', 'I', 'F', 'D', 'K', 'F',
             'F', 'S', 'W', 'L', 'F', 'G', 'R', 'T', 'H', 'R', 'N', 'H', 'S', 'E', 'R', 'F', 'E', 'K', 'Y', 'G', 'T',
             'L', 'A', 'L', 'T', 'L', 'F', 'V', 'A', 'V', 'P', 'L', 'P', 'V', 'T', 'G', 'A', 'W', 'T', 'G', 'C', 'A',
             'A', 'A', 'F', 'V', 'F', 'G', 'I', 'K', 'F', 'R', 'H', 'A', 'F', 'P', 'A', 'I', 'L', 'A', 'G', 'V', 'L',
             'I', 'A', 'G', 'I', 'I', 'V', 'S', 'S', 'V', 'T', 'L', 'G', 'G', 'I', 'G', 'L', 'V', 'D', 'L', 'F', 'S',
             'dummy_fname'])

        data, invalid = SequenceLoader(dummy_raw_file, 'dummy_fname')
        self.assertFalse(invalid)
        self.assertEqual(data, expected_data)

    def test_2(self):
        dummy_raw_file = 'data:application/octet-stream;base64,TEVOIDE2OAoxIDEwIDEKMTAgMTUgMgo0MCA' \
                         '1NSA3CjU1IDg1IDgKODUgOTkgOQoxMDAgMTYwIDEwCg=='

        data, invalid = SequenceLoader(dummy_raw_file, 'dummy_fname')
        self.assertIsNone(data)
        self.assertTrue(invalid)
