import unittest
from parsers import CustomParser
from utils.exceptions import InvalidFormat


class CustomParserTestCase(unittest.TestCase):

    def test_1(self):
        dummy_prediction = """
LEN 46
1 5 10
6 10 2
11 35 5
36 37 3
39 39 8
40 40 9
42 45 1
"""

        expected = [10, 10, 10, 10, 10, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                    5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 'NAN', 8, 9, 'NAN', 1, 1, 1, 1, 'NAN']

        output = CustomParser(dummy_prediction)
        self.assertEquals(46, len(output))
        self.assertListEqual(expected, output)

    def test_2(self):
        dummy_prediction = """XXXX
LEN 46
1 5 10
6 10 2
11 35 5
36 37 3
39 39 8
40 40 9
42 45 1
"""
        with self.assertRaises(InvalidFormat):
            output = CustomParser(dummy_prediction)

    def test_3(self):
        dummy_prediction = """LEN XX
1 5 10
6 10 2
11 35 5
36 37 3
39 39 8
40 40 9
42 45 1
"""
        with self.assertRaises(InvalidFormat):
            output = CustomParser(dummy_prediction)

    def test_4(self):
        dummy_prediction = """LEN 44
1 5 10
6 10 2
11 35 5
36 37 3
39 39 8
40 40 9
42 45 1
"""
        with self.assertRaises(InvalidFormat):
            output = CustomParser(dummy_prediction)

    def test_5(self):
        dummy_prediction = """LEN 46
1 5 10
6 10 2
11 35 5
36 37 3
39 39 8
40 40 9
45 42 1
"""
        with self.assertRaises(InvalidFormat):
            output = CustomParser(dummy_prediction)

    def test_6(self):
        dummy_prediction = """LEN 46
1 5 10
6 10 2
11 35 5
36 37 12
39 39 8
40 40 9
42 45 1
"""
        with self.assertRaises(InvalidFormat):
            output = CustomParser(dummy_prediction)

    def test_7(self):
        dummy_prediction = """LEN 46
1 5 10
6 10 2
11 35 5
36 37 0
39 39 8
40 40 9
42 45 10
"""
        with self.assertRaises(InvalidFormat):
            output = CustomParser(dummy_prediction)