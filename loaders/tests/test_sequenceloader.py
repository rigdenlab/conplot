from Bio.Alphabet.IUPAC import protein
import unittest
from loaders import SequenceLoader
from loaders.sequenceloader import get_hydrophobicity
from utils import compress_data, decompress_data


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
            [7, 4, 9, 1, 7, 4, 9, 9, 1, 9, 9, 4, 4, 8, 3, 1, 4, 9, 7, 4, 7, 9, 10, 4, 7, 7, 3, 10, 8, 1, 9, 0, 4, 7, 10,
             3, 10, 7, 9, 4, 10, 3, 1, 7, 4, 3, 9, 4, 7, 8, 10, 8, 7, 9, 9, 4, 1, 7, 10, 3, 9, 9, 3, 9, 9, 9, 8, 9, 1,
             3, 9, 4, 4, 3, 9, 0, 0, 8, 7, 10, 8, 1, 0, 8, 8, 4, 4, 9, 8, 4, 0, 4, 1, 0, 1, 1, 4, 1, 0, 8, 1, 0, 3, 4,
             4, 9, 7, 9, 4, 9, 8, 9, 7, 9, 3, 9, 3, 9, 4, 4, 7, 4, 4, 4, 7, 7, 7, 7, 8, 9, 8, 4, 10, 0, 8, 0, 1, 7, 8,
             3, 7, 10, 9, 7, 4, 9, 9, 10, 7, 4, 10, 10, 9, 4, 4, 9, 4, 9, 4, 4, 10, 4, 9, 9, 1, 9, 8, 4]
        )

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

    def test_3(self):
        expected = [7, 7, 1, 1, 8, 4, 1, 10, 0, 9, 7, 1, 3, 1, 0, 4, 4, 9, 4, 3]
        seq = protein.letters
        self.assertListEqual(expected, get_hydrophobicity(seq))
