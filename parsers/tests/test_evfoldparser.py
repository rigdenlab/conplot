import unittest
from parsers import EvfoldParser
from utils.exceptions import InvalidFormat


class EvfoldParserTestCase(unittest.TestCase):

    def test_1(self):
        dummy_prediction = """112 X 145 X 0 0.99560225 
38 X 49 X 0 0.99520814
24 X 56 X 0 0.995158
109 X 145 X 0 0.99344337
109 X 141 X 0 0.99096644
64 X 125 X 0 0.98981607
128 X 138 X 0 0.9892521
34 X 53 X 0 0.98918885
75 X 81 X 0 0.9883262
57 X 146 X 0 0.98828995"""


        expected_res1 = [112, 38, 24, 109, 109, 64, 128, 34, 75, 57]
        expected_res2 =[145, 49, 56, 145, 141, 125, 138, 53, 81, 146]
        expected_score = [0.99560225, 0.99520814, 0.995158, 0.99344337, 0.99096644, 0.98981607, 0.9892521, 0.98918885,
                          0.9883262, 0.98828995]

        output = EvfoldParser(dummy_prediction)
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
            output = EvfoldParser(dummy_prediction)