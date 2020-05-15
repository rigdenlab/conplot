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
                                       'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'dummy_fname'])

        data, invalid = Loader(dummy_raw_file, 'CUSTOM', 'dummy_fname')
        self.assertFalse(invalid)
        self.assertEqual(data, expected_data)

    def test_2(self):
        dummy_raw_file = 'data:application/octet-stream;base64,TEVOIDE2OAoxIDEwIDEKMTAgMTUgMgo0MCA' \
                         '1NSA3CjU1IDg1IDgKODUgOTkgOQoxMDAgMTYwIDEwCg=='

        data, invalid = Loader(dummy_raw_file, 'TOPCONS', 'dummy_fname')
        self.assertIsNone(data)
        self.assertTrue(invalid)

    def test_3(self):
        dummy_raw_file = 'data:application/octet-stream;base64,NTAgWCA1OCBYIDAgMC45OTk5MDg5CjUxIFggNTggWCAwIDAuOTk5ODk' \
                         '3ODQKMTQzIFggMTg1IFggMCAwLjk5OTg5NDMKMTQwIFggMTUyIFggMCAwLjk5OTg3Nzc1CjE0OCBYIDE5MCBYIDAgMC4' \
                         '5OTk4NzU0CjUwIFggMTUzIFggMCAwLjk5OTg2MjIKMTQ1IFggMTE3IFggMCAwLjk5OTg1NTY0CjEzOSBYIDEwMSBYIDA' \
                         'gMC45OTk4Mjc1CjE0MSBYIDE5MyBYIDAgMC45OTk4MjIzCgo='

        expected_data = compress_data(
            [(50, 58, 0.9999089), (51, 58, 0.99989784), (143, 185, 0.9998943), (140, 152, 0.99987775),
             (148, 190, 0.9998754), (50, 153, 0.9998622), (145, 117, 0.99985564), (139, 101, 0.9998275),
             (141, 193, 0.9998223), 'dummy_fname'])

        data, invalid = Loader(dummy_raw_file, 'EVFOLD', 'dummy_fname')
        self.assertFalse(invalid)
        self.assertEqual(data, expected_data)
