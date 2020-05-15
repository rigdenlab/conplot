import unittest
from loaders import SequenceLoader
from utils import compress_data


class SequenceLoaderTestCase(unittest.TestCase):

    def test_1(self):
        dummy_raw_file = 'data:application/octet-stream;base64,PnRyfFc5RFkyOHxXOURZMjhfTUVUVEkgUHV0YXRpdmUgbWVtYnJhbmU' \
                         'gcHJvdGVpbiBPUz1NZXRoYW5vbG9idXMgdGluZGFyaXVzIERTTSAyMjc4IE9YPTEwOTAzMjIgR049TWV0dGlEUkFGVF8' \
                         'yMDU1IFBFPTQgU1Y9MQpNU0xFQVRWTERMTFNTRlBIV0xBVE1WSUdBTVBJRkVMUkdBSVBJQUxHSVlETVNQVlNBRklGQVZ' \
                         'MR05NSVBWVlBMTExGTERQVlNUWUxSUkZBSUZES0ZGU1dMRkdSVEhSTkhTRVJGRUtZR1RMQUxUTEZWQVZQTFBWVEdBV1R' \
                         'HQ0FBQUZWRkdJS0ZSSEFGUEFJTEFHVkxJQUdJSVZTU1ZUTEdHSUdMVkRMRlMKCg=='

        expected_data = compress_data('MSLEATVLDLLSSFPHWLATMVIGAMPIFELRGAIPIALGIYDMSPVSAFIFAVLGNMIPVVPLLLFLDPVSTYLRRFA'
                                      'IFDKFFSWLFGRTHRNHSERFEKYGTLALTLFVAVPLPVTGAWTGCAAAFVFGIKFRHAFPAILAGVLIAGIIVSSVTL'
                                      'GGIGLVDLFS')

        data, invalid = SequenceLoader(dummy_raw_file)
        self.assertFalse(invalid)
        self.assertEqual(data, expected_data)

    def test_2(self):
        dummy_raw_file = 'data:application/octet-stream;base64,TEVOIDE2OAoxIDEwIDEKMTAgMTUgMgo0MCA' \
                         '1NSA3CjU1IDg1IDgKODUgOTkgOQoxMDAgMTYwIDEwCg=='

        data, invalid = SequenceLoader(dummy_raw_file)
        self.assertIsNone(data)
        self.assertTrue(invalid)
