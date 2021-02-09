import unittest
from parsers import ContactParser
from utils.exceptions import InvalidFormat


class ContactParserTestCase(unittest.TestCase):

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
11 T   5 Q 0.000 0.178 0.066 0.730 0.876 0.727
"""

        expected_res2 = [5, 6, 6, 5, 6, 6, 6, 5, 5, 6]
        expected_res1 = [11, 79, 94, 10, 62, 78, 80, 21, 58, 63]
        expected_score = [0.727, 0.679, 0.679, 0.634, 0.585, 0.581, 0.578, 0.557, 0.535, 0.529]

        output = ContactParser(dummy_prediction, 'BCLCONTACTS')

        self.assertEqual(10, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_score, [contact[2] for contact in output])

    def test_2(self):
        dummy_prediction = """###
D U M M Y
100 8 5.382865
"""
        with self.assertRaises(InvalidFormat):
            output = ContactParser(dummy_prediction, 'BCLCONTACTS')

    def test_3(self):
        dummy_prediction = """#identifier diversity     direction viterbiscore indexpred        state  res1  res2
1EAZ      0.65  Antiparallel     9.860725         1        first    29    24
1EAZ      0.65  Antiparallel     9.860725         1     internal    30    23
1EAZ      0.65  Antiparallel     9.860725         1         last    31    22
1EAZ      0.65      Parallel    -6.855870        29        first    87    54
1EAZ      0.65      Parallel    -6.855870        29     internal    88    55
1EAZ      0.65      Parallel    -6.855870        29         last    89    56
1EAZ      0.65      Parallel    -6.855870        29         last    56    89
"""

        expected_res1 = [29, 30, 31, 87, 88, 89]
        expected_res2 = [24, 23, 22, 54, 55, 56]
        expected_score = [0, 0, 0, 0, 0, 0]

        output = ContactParser(dummy_prediction, 'BBCONTACTS')

        self.assertEqual(6, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_score, [contact[2] for contact in output])

    def test_4(self):
        dummy_prediction = """112 X 145 X Hx-Hx 
38 X 49 X  Hx-Hx 
24 X 56 X  Hx-Hx 
109 X 145 X  Hx-Hx 
109 X 141 X Hx-Hx 
64 X 125 X Hx-Hx 
128 X 138 X Hx-Hx 
34 X 53 X Hx-Hx 
75 X 81 X Hx-Hx 
57 X 146 X Hx-Hx 
146 X 57 X Hx-Hx """

        expected_res2 = [112, 38, 24, 109, 109, 64, 128, 34, 75, 57]
        expected_res1 = [145, 49, 56, 145, 141, 125, 138, 53, 81, 146]
        expected_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        output = ContactParser(dummy_prediction, 'COMSAT')
        self.assertEqual(10, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_score, [contact[2] for contact in output])

    def test_5(self):
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

        expected_res2 = [112, 38, 24, 109, 109, 64, 128, 34, 75, 57]
        expected_res1 = [145, 49, 56, 145, 141, 125, 138, 53, 81, 146]
        expected_score = [0.99560225, 0.99520814, 0.995158, 0.99344337, 0.99096644, 0.98981607, 0.9892521, 0.98918885,
                          0.9883262, 0.98828995]

        output = ContactParser(dummy_prediction, 'EVFOLD')
        self.assertEqual(10, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_score, [contact[2] for contact in output])

    def test_6(self):
        dummy_prediction = """112 145 0.99560225 
38 49 0.99520814
24 56 0.995158
109 145 0.99344337
109 141 0.99096644
64 125 0.98981607
128 138 0.9892521
34 53 0.98918885
75 81 0.9883262
57 146 0.98828995"""

        expected_res2 = [112, 38, 24, 109, 109, 64, 128, 34, 75, 57]
        expected_res1 = [145, 49, 56, 145, 141, 125, 138, 53, 81, 146]
        expected_score = [0.99560225, 0.99520814, 0.995158, 0.99344337, 0.99096644, 0.98981607, 0.9892521, 0.98918885,
                          0.9883262, 0.98828995]

        output = ContactParser(dummy_prediction, 'FLIB')
        self.assertEqual(10, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_score, [contact[2] for contact in output])

    def test_7(self):
        dummy_prediction = """112 145 0.99560225 
38 49 0.99520814
24 56 0.995158
109 145 0.99344337
109 141 0.99096644
64 125 0.98981607
128 138 0.9892521
34 53 0.98918885
75 81 0.9883262
57 146 0.98828995"""

        expected_res2 = [112, 38, 24, 109, 109, 64, 128, 34, 75, 57]
        expected_res1 = [145, 49, 56, 145, 141, 125, 138, 53, 81, 146]
        expected_score = [0.99560225, 0.99520814, 0.995158, 0.99344337, 0.99096644, 0.98981607, 0.9892521, 0.98918885,
                          0.9883262, 0.98828995]

        output = ContactParser(dummy_prediction, 'PCONS')
        self.assertEqual(10, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_score, [contact[2] for contact in output])

    def test_8(self):
        dummy_prediction = """112 X 145 X 0.99560225 0
38 X 49 X 0.99520814 0
24 X 56 X 0.995158 0
109 X 145 X 0.99344337 0
109 X 141 X 0.99096644 0
64 X 125 X 0.98981607 0
128 X 138 X 0.9892521 0
34 X 53 X 0.98918885 0
75 X 81 X 0.9883262 0
57 X 146 X 0.98828995 0"""

        expected_res2 = [112, 38, 24, 109, 109, 64, 128, 34, 75, 57]
        expected_res1 = [145, 49, 56, 145, 141, 125, 138, 53, 81, 146]
        expected_score = [0.99560225, 0.99520814, 0.995158, 0.99344337, 0.99096644, 0.98981607, 0.9892521, 0.98918885,
                          0.9883262, 0.98828995]

        output = ContactParser(dummy_prediction, 'FREECONTACT')
        self.assertEqual(10, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_score, [contact[2] for contact in output])

    def test_9(self):
        dummy_prediction = """112,145,0.99560225
38,49,0.99520814
24,56,0.995158
109,145,0.99344337
109,141,0.99096644
64,125,0.98981607
128,138,0.9892521
34,53,0.98918885
75,81,0.9883262
57,146,0.98828995"""

        expected_res2 = [112, 38, 24, 109, 109, 64, 128, 34, 75, 57]
        expected_res1 = [145, 49, 56, 145, 141, 125, 138, 53, 81, 146]
        expected_score = [0.99560225, 0.99520814, 0.995158, 0.99344337, 0.99096644, 0.98981607, 0.9892521, 0.98918885,
                          0.9883262, 0.98828995]

        output = ContactParser(dummy_prediction, 'PLMDCA')
        self.assertEqual(10, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_score, [contact[2] for contact in output])

    def test_10(self):
        dummy_prediction = """LEN     146
CON 112 145 0.995602
CON 38 49 0.995208
CON 24 56 0.995158
CON 109 145 0.993443
CON 109 141 0.990966
CON 64 125 0.989816
CON 128 138 0.989252
CON 34 53 0.989189
CON 75 81 0.988326
CON 57 146 0.988290
PRF     0       T       X       0.0321  0.0078  0.0582  0.1021  0.0207  0.0384  0.038   0.0386  0.0697  0.0376  0.0586
PRF     1       M       X       0.0228  0.0052  0.0103  0.0112  0.1236  0.0083  0.0106  0.1182  0.0104  0.3046  0.1922
PRF     2       K       X       0.0322  0.0048  0.0563  0.128   0.0116  0.0481  0.0332  0.0319  0.1099  0.0366  0.0228
PRF     3       I       X       0.0147  0.0062  0.0025  0.0034  0.2786  0.0058  0.0057  0.1876  0.0053  0.2779  0.0302
PRF     4       I       X       0.0404  0.0057  0.1139  0.2398  0.0104  0.028   0.0275  0.0278  0.0491  0.0283  0.0051
"""

        expected_res2 = [112, 38, 24, 109, 109, 64, 128, 34, 75, 57]
        expected_res1 = [145, 49, 56, 145, 141, 125, 138, 53, 81, 146]
        expected_score = [0.995602, 0.995208, 0.995158, 0.993443, 0.990966, 0.989816, 0.989252, 0.989189,
                          0.988326, 0.98829]

        output = ContactParser(dummy_prediction, 'MAPALIGN')
        self.assertEqual(10, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_score, [contact[2] for contact in output])

    def test_11(self):
        dummy_prediction = """147
112 145
38 49
24 56
109 145
109 141
64 125
128 138
34 53
75 81
57 146
"""

        expected_res2 = [112, 38, 24, 109, 109, 64, 128, 34, 75, 57]
        expected_res1 = [145, 49, 56, 145, 141, 125, 138, 53, 81, 146]
        expected_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        output = ContactParser(dummy_prediction, 'ALEIGEN')
        self.assertEqual(10, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_score, [contact[2] for contact in output])

    def test_12(self):
        dummy_prediction = """
i       j       i_id    j_id    r_sco   s_sco   prob
112     145     112_X   145_X   0.99560225      1.0     1.0
38      49      38_X    49_X    0.99520814      1.0     1.0
24      56      24_X    56_X    0.995158        1.0     1.0
109     145     109_X   145_X   0.99344337      1.0     1.0
109     141     109_X   141_X   0.99096644      1.0     1.0
64      125     64_X    125_X   0.98981607      1.0     1.0
128     138     128_X   138_X   0.9892521       1.0     1.0
34      53      34_X    53_X    0.98918885      1.0     1.0
75      81      75_X    81_X    0.9883262       1.0     1.0
57      146     57_X    146_X   0.98828995      1.0     1.0
"""

        expected_res2 = [112, 38, 24, 109, 109, 64, 128, 34, 75, 57]
        expected_res1 = [145, 49, 56, 145, 141, 125, 138, 53, 81, 146]
        expected_score = [0.99560225, 0.99520814, 0.995158, 0.99344337, 0.99096644, 0.98981607, 0.9892521, 0.98918885,
                          0.9883262, 0.98828995]

        output = ContactParser(dummy_prediction, 'GREMLIN')
        self.assertEqual(10, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_score, [contact[2] for contact in output])
