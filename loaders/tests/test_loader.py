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

    def test_3(self):
        dummy_raw_file = 'data:application/octet-stream;base64,NTAgWCA1OCBYIDAgMC45OTk5MDg5CjUxIFggNTggWCAwIDAuOTk5ODk' \
                         '3ODQKMTQzIFggMTg1IFggMCAwLjk5OTg5NDMKMTQwIFggMTUyIFggMCAwLjk5OTg3Nzc1CjE0OCBYIDE5MCBYIDAgMC4' \
                         '5OTk4NzU0CjUwIFggMTUzIFggMCAwLjk5OTg2MjIKMTQ1IFggMTE3IFggMCAwLjk5OTg1NTY0CjEzOSBYIDEwMSBYIDA' \
                         'gMC45OTk4Mjc1CjE0MSBYIDE5MyBYIDAgMC45OTk4MjIzCgo='

        expected_data = compress_data(
            [[58, 50, 0.9999089], [58, 51, 0.99989784], [185, 143, 0.9998943], [152, 140, 0.99987775],
             [190, 148, 0.9998754], [153, 50, 0.9998622], [145, 117, 0.99985564], [139, 101, 0.9998275],
             [193, 141, 0.9998223]])

        data, invalid = Loader(dummy_raw_file, 'EVFOLD')
        self.assertFalse(invalid)
        self.assertEqual(data, expected_data)
