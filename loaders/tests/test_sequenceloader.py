from Bio.Alphabet.IUPAC import protein
import unittest
from loaders import SequenceLoader
from loaders.sequenceloader import get_hydrophobicity
from utils import compress_data


class SequenceLoaderTestCase(unittest.TestCase):

    def test_1(self):
        dummy_raw_file = 'data:application/octet-stream;base64,PnRyfFc5RFkyOHxXOURZMjhfTUVUVEkgUHV0YXRpdmUgbWVtYnJhbmU' \
                         'gcHJvdGVpbiBPUz1NZXRoYW5vbG9idXMgdGluZGFyaXVzIERTTSAyMjc4IE9YPTEwOTAzMjIgR049TWV0dGlEUkFGVF8' \
                         'yMDU1IFBFPTQgU1Y9MQpNU0xFQVRWTERMTFNTRlBIV0xBVE1WSUdBTVBJRkVMUkdBSVBJQUxHSVlETVNQVlNBRklGQVZ' \
                         'MR05NSVBWVlBMTExGTERQVlNUWUxSUkZBSUZES0ZGU1dMRkdSVEhSTkhTRVJGRUtZR1RMQUxUTEZWQVZQTFBWVEdBV1R' \
                         'HQ0FBQUZWRkdJS0ZSSEFGUEFJTEFHVkxJQUdJSVZTU1ZUTEdHSUdMVkRMRlMKCg=='

        expected_seq_data = compress_data(
            ['M', 'S', 'L', 'E', 'A', 'T', 'V', 'L', 'D', 'L', 'L', 'S', 'S', 'F', 'P', 'H', 'W', 'L', 'A', 'T', 'M',
             'V', 'I', 'G', 'A', 'M', 'P', 'I', 'F', 'E', 'L', 'R', 'G', 'A', 'I', 'P', 'I', 'A', 'L', 'G', 'I', 'Y',
             'D', 'M', 'S', 'P', 'V', 'S', 'A', 'F', 'I', 'F', 'A', 'V', 'L', 'G', 'N', 'M', 'I', 'P', 'V', 'V', 'P',
             'L', 'L', 'L', 'F', 'L', 'D', 'P', 'V', 'S', 'T', 'Y', 'L', 'R', 'R', 'F', 'A', 'I', 'F', 'D', 'K', 'F',
             'F', 'S', 'W', 'L', 'F', 'G', 'R', 'T', 'H', 'R', 'N', 'H', 'S', 'E', 'R', 'F', 'E', 'K', 'Y', 'G', 'T',
             'L', 'A', 'L', 'T', 'L', 'F', 'V', 'A', 'V', 'P', 'L', 'P', 'V', 'T', 'G', 'A', 'W', 'T', 'G', 'C', 'A',
             'A', 'A', 'F', 'V', 'F', 'G', 'I', 'K', 'F', 'R', 'H', 'A', 'F', 'P', 'A', 'I', 'L', 'A', 'G', 'V', 'L',
             'I', 'A', 'G', 'I', 'I', 'V', 'S', 'S', 'V', 'T', 'L', 'G', 'G', 'I', 'G', 'L', 'V', 'D', 'L', 'F', 'S'])

        expected_hydro_data = compress_data(
            [-0.44, 0.33, -0.69, 0.12, 0.33, 0.11, -0.53, -0.69, 0.5, -0.69, -0.69, 0.33, 0.33, -0.58, -0.31, -0.06,
             -0.24, -0.69, 0.33, 0.11, -0.44, -0.53, -0.81, 1.14, 0.33, -0.44, -0.31, -0.81, -0.58, 0.12, -0.69, 1.0,
             1.14, 0.33, -0.81, -0.31, -0.81, 0.33, -0.69, 1.14, -0.81, 0.23, 0.5, -0.44, 0.33, -0.31, -0.53, 0.33,
             0.33, -0.58, -0.81, -0.58, 0.33, -0.53, -0.69, 1.14, 0.43, -0.44, -0.81, -0.31, -0.53, -0.53, -0.31, -0.69,
             -0.69, -0.69, -0.58, -0.69, 0.5, -0.31, -0.53, 0.33, 0.11, 0.23, -0.69, 1.0, 1.0, -0.58, 0.33, -0.81,
             -0.58, 0.5, 1.81, -0.58, -0.58, 0.33, -0.24, -0.69, -0.58, 1.14, 1.0, 0.11, -0.06, 1.0, 0.43, -0.06, 0.33,
             0.12, 1.0, -0.58, 0.12, 1.81, 0.23, 1.14, 0.11, -0.69, 0.33, -0.69, 0.11, -0.69, -0.58, -0.53, 0.33, -0.53,
             -0.31, -0.69, -0.31, -0.53, 0.11, 1.14, 0.33, -0.24, 0.11, 1.14, 0.22, 0.33, 0.33, 0.33, -0.58, -0.53,
             -0.58, 1.14, -0.81, 1.81, -0.58, 1.0, -0.06, 0.33, -0.58, -0.31, 0.33, -0.81, -0.69, 0.33, 1.14, -0.53,
             -0.69, -0.81, 0.33, 1.14, -0.81, -0.81, -0.53, 0.33, 0.33, -0.53, 0.11, -0.69, 1.14, 1.14, -0.81, 1.14,
             -0.69, -0.53, 0.5, -0.69, -0.58, 0.33])

        seq_data, hydro_data, invalid = SequenceLoader(dummy_raw_file)
        self.assertFalse(invalid)
        self.assertEqual(seq_data, expected_seq_data)
        self.assertEqual(hydro_data, expected_hydro_data)

    def test_2(self):
        dummy_raw_file = 'data:application/octet-stream;base64,TEVOIDE2OAoxIDEwIDEKMTAgMTUgMgo0MCA' \
                         '1NSA3CjU1IDg1IDgKODUgOTkgOQoxMDAgMTYwIDEwCg=='

        seq_data, hydro_data, invalid = SequenceLoader(dummy_raw_file)
        self.assertIsNone(seq_data)
        self.assertIsNone(hydro_data)
        self.assertTrue(invalid)

    def test_6(self):
        expected = [0.33, 0.22, 0.5, 0.12, -0.58, 1.14, -0.06, -0.81, 1.81, -0.69, -0.44, 0.43, -0.31, 0.19, 1.0, 0.33,
                    0.11, -0.53, -0.24, 0.23]
        seq = protein.letters
        self.assertListEqual(expected, get_hydrophobicity(seq))
