import unittest
from loaders import Loader
from utils import compress_data


class LoaderTestCase(unittest.TestCase):

    def test_1(self):
        dummy_raw_file = 'data:application/octet-stream;base64,TEVOIDE2OAoxIDEwIDEKMTAgMTUgMgo0MCA' \
                         '1NSA3CjU1IDg1IDgKODUgOTkgOQoxMDAgMTYwIDEwCg=='
        expected_data = compress_data([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 'NAN', 'NAN', 'NAN', 'NAN', 'NAN',
                                       'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN',
                                       'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 7, 7, 7, 7, 7, 7, 7, 7,
                                       7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
                                       8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10,
                                       10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                                       10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                                       10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                                       'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN'])

        data, invalid = Loader(dummy_raw_file, 'CUSTOM')
        self.assertFalse(invalid)
        self.assertEqual(data, expected_data)

    def test_2(self):
        dummy_raw_file = 'data:application/octet-stream;base64,TEVOIDE2OAoxIDEwIDEKMTAgMTUgMgo0MCA' \
                         '1NSA3CjU1IDg1IDgKODUgOTkgOQoxMDAgMTYwIDEwCg=='

        data, invalid = Loader(dummy_raw_file, 'TOPCONS')
        self.assertIsNone(data)
        self.assertTrue(invalid)
