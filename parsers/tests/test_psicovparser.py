import unittest
from parsers import PsicovParser
from utils.exceptions import InvalidFormat


class PsicovParserTestCase(unittest.TestCase):

    def test_1(self):
        dummy_prediction = """46 78 0 8 9.301869
80 105 0 8 8.856009
111 129 0 8 7.252451
75 205 0 8 6.800462
19 44 0 8 6.588349
111 130 0 8 6.184269
23 41 0 8 6.163786
171 205 0 8 5.519271
53 126 0 8 5.440612
100 140 0 8 5.382865"""

        expected_res1 = [46, 80, 111, 75, 19, 111, 23, 171, 53, 100]
        expected_res2 = [78, 105, 129, 205, 44, 130, 41, 205, 126, 140]
        expected_score = [9.301869, 8.856009, 7.252451, 6.800462, 6.588349, 6.184269, 6.163786, 5.519271, 5.440612,
                          5.382865]

        output = PsicovParser(dummy_prediction)
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
            output = PsicovParser(dummy_prediction)
