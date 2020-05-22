import unittest
from parsers import BbcontactsParser
from utils.exceptions import InvalidFormat


class BbcontactsParserTestCase(unittest.TestCase):

    def test_1(self):
        dummy_prediction = """#identifier diversity     direction viterbiscore indexpred        state  res1  res2
1EAZ      0.65  Antiparallel     9.860725         1        first    29    24
1EAZ      0.65  Antiparallel     9.860725         1     internal    30    23
1EAZ      0.65  Antiparallel     9.860725         1         last    31    22
1EAZ      0.65      Parallel    -6.855870        29        first    87    54
1EAZ      0.65      Parallel    -6.855870        29     internal    88    55
1EAZ      0.65      Parallel    -6.855870        29         last    89    56
"""

        expected_res1 = [29, 30, 31, 87, 88, 89]
        expected_res2 = [24, 23, 22, 54, 55, 56]
        expected_score = [0, 0, 0, 0, 0, 0]

        output = BbcontactsParser(dummy_prediction)

        self.assertEquals(6, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_score, [contact[2] for contact in output])

    def test_2(self):
        dummy_prediction = """###
D U M M Y
100 8 5.382865
"""
        with self.assertRaises(InvalidFormat):
            output = BbcontactsParser(dummy_prediction)