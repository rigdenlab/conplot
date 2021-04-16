import unittest
from parsers import MappredParser
from utils.exceptions import InvalidFormat


class MappredParserTestCase(unittest.TestCase):

    def test_1(self):
        dummy_prediction = """#REMARK MapPred 1.1
#REMARK idx_i, idx_j, distance distribution of 34 bins
#REMARK 34 bins consist of 32 normal bins (4-20A with a step of 0.5A) and two boundary bins ( [0,4) and [20, inf) ), as follows: [0,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15,15.5,16,16.5,17,17.5,18,18.5,19,19.5,20,inf]
5 10 0.0129 0.0358 0.1879 0.2688 0.4436 0.0364 0.0016 0.0011 0.0005 0.0004 0.0004 0.0005 0.0005 0.0004 0.0004 0.0003 0.0002 0.0002 0.0002 0.0001 0.0002 0.0002 0.0002 0.0003 0.0002 0.0002 0.0002 0.0001 0.0001 0.0001 0.0001 0.0000 0.0000 0.0058
1 35 0.0002 0.0017 0.0046 0.0158 0.0374 0.0660 0.1207 0.2161 0.2476 0.1666 0.0729 0.0354 0.0049 0.0013 0.0008 0.0004 0.0002 0.0002 0.0002 0.0002 0.0002 0.0001 0.0002 0.0002 0.0002 0.0001 0.0001 0.0000 0.0000 0.0001 0.0000 0.0000 0.0000 0.0058
43 85 0.0009 0.0027 0.0044 0.0115 0.0209 0.0149 0.0120 0.0190 0.0210 0.0383 0.0718 0.1105 0.1392 0.1948 0.1630 0.1048 0.0407 0.0159 0.0033 0.0006 0.0004 0.0003 0.0002 0.0002 0.0002 0.0002 0.0001 0.0002 0.0002 0.0001 0.0001 0.0001 0.0001 0.0073
85 43 0.0009 0.0027 0.0044 0.0115 0.0209 0.0149 0.0120 0.0190 0.0210 0.0383 0.0718 0.1105 0.1392 0.1948 0.1630 0.1048 0.0407 0.0159 0.0033 0.0006 0.0004 0.0003 0.0002 0.0002 0.0002 0.0002 0.0001 0.0002 0.0002 0.0001 0.0001 0.0001 0.0001 0.0073
50 50 0.0009 0.0027 0.0044 0.0115 0.0209 0.0149 0.0120 0.0190 0.0210 0.0383 0.0718 0.1105 0.1392 0.1948 0.1630 0.1048 0.0407 0.0159 0.0033 0.0006 0.0004 0.0003 0.0002 0.0002 0.0002 0.0002 0.0001 0.0002 0.0002 0.0001 0.0001 0.0001 0.0001 0.0073
18 50 0.0006 0.0009 0.0010 0.0018 0.0024 0.0027 0.0027 0.0032 0.0043 0.0052 0.0068 0.0105 0.0156 0.0222 0.0298 0.0526 0.0895 0.1389 0.1769 0.1865 0.1278 0.0709 0.0316 0.0096 0.0021 0.0005 0.0002 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0028
"""
        expected_res1 = [10, 35, 85, 50]
        expected_res2 = [5, 1, 43, 18]
        expected_raw_score = [0.9885999999999999, 0.7101, 0.1073, 0.0196]
        expected_bin_distance = [1, 2, 4, 5]
        expected_bin_score = [0.9360999999999999, 0.6504, 0.5033,0.6301]

        output = MappredParser(dummy_prediction)

        self.assertEqual('DISTO', output.pop(-1))
        self.assertEqual(4, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_raw_score, [contact[2] for contact in output])
        self.assertListEqual(expected_bin_distance, [contact[3] for contact in output])
        self.assertListEqual(expected_bin_score, [contact[4] for contact in output])

    def test_2(self):
        dummy_prediction = """###
D U M M Y
100 8 5.382865
1 5 0.0009 0.0027 0.0044 0.0115 0.0209 0.0149 0.0120 0.0190 0.0210 0.0383 0.0718 0.1105 0.1392 0.1948 0.1630 0.1048 0.0407 0.0159 0.0033 0.0006 0.0004 0.0003 0.0002 0.0002 0.0002 0.0002 0.0001 0.0002 0.0002 0.0001 0.0001 0.0001 0.0001 0.0073
"""
        with self.assertRaises(InvalidFormat):
            output = MappredParser(dummy_prediction)
            self.assertListEqual(output, [])
