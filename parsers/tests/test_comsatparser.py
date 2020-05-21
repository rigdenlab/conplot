import unittest
from parsers import ComsatParser
from utils.exceptions import InvalidFormat


class ComsatParserTestCase(unittest.TestCase):

    def test_1(self):
        dummy_prediction = """112 X 145 X Hx-Hx 
38 X 49 X  Hx-Hx 
24 X 56 X  Hx-Hx 
109 X 145 X  Hx-Hx 
109 X 141 X Hx-Hx 
64 X 125 X Hx-Hx 
128 X 138 X Hx-Hx 
34 X 53 X Hx-Hx 
75 X 81 X Hx-Hx 
57 X 146 X Hx-Hx """

        expected_res1 = [112, 38, 24, 109, 109, 64, 128, 34, 75, 57]
        expected_res2 = [145, 49, 56, 145, 141, 125, 138, 53, 81, 146]
        expected_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        output = ComsatParser(dummy_prediction)
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
            output = ComsatParser(dummy_prediction)