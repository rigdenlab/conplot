import unittest
from parsers import BclcontactsParser
from utils.exceptions import InvalidFormat


class BclcontactsParserTestCase(unittest.TestCase):

    def test_1(self):
        dummy_prediction = """5 I    9 Q 0.000 0.286 0.185 0.836 0.875 0.749
5 I   10 R 0.000 0.000 0.105 0.875 0.482 0.634
5 I   11 I 0.000 0.178 0.066 0.730 0.876 0.727
5 I   21 I 0.030 0.021 0.233 0.645 0.733 0.557
5 I   58 G 0.000 0.054 0.010 0.642 0.799 0.535
6 T   62 V 0.000 0.000 0.027 0.485 0.428 0.585
6 T   63 S 0.000 0.004 0.051 0.547 0.387 0.529
6 T   78 L 0.000 0.000 0.039 0.624 0.384 0.581
6 T   79 T 0.000 0.000 0.036 0.657 0.415 0.679
6 T   80 I 0.000 0.076 0.003 0.513 0.386 0.578
6 T   94 Q 0.000 0.068 0.041 0.534 0.489 0.679
"""

        expected_res1 = [5, 6, 6, 5, 6, 6, 6, 5, 5, 6]
        expected_res2 = [11, 79, 94, 10, 62, 78, 80, 21, 58, 63]
        expected_score = [0.727, 0.679, 0.679, 0.634, 0.585, 0.581, 0.578, 0.557, 0.535, 0.529]

        output = BclcontactsParser(dummy_prediction)

        self.assertEquals(10, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_score, [contact[2] for contact in output])

    def test_2(self):
        dummy_prediction = """###
D U M M Y
100 8 5.382865
"""
        with self.assertRaises(InvalidFormat):
            output = BclcontactsParser(dummy_prediction)