import unittest
from parsers import PsipredParser, SecondaryStructureStates, InvalidFormat


class PsipredParserTestCase(unittest.TestCase):

    def test_1(self):
        dummy_prediction = """# PSIPRED VFORMAT (PSIPRED V4.0)

   1 M C   0.999  0.001  0.000
   2 S C   0.879  0.094  0.002
   3 L H   0.031  0.972  0.000
   4 E H   0.027  0.976  0.000
   5 A H   0.012  0.989  0.000
   6 T E   0.006  0.996  0.000
   7 V E   0.006  0.996  0.000
   8 L C   0.005  0.997  0.000
   9 D H   0.008  0.994  0.000
  10 L H   0.021  0.984  0.000
  
"""

        expected = [
            SecondaryStructureStates.COIL.value,
            SecondaryStructureStates.COIL.value,
            SecondaryStructureStates.HELIX.value,
            SecondaryStructureStates.HELIX.value,
            SecondaryStructureStates.HELIX.value,
            SecondaryStructureStates.SHEET.value,
            SecondaryStructureStates.SHEET.value,
            SecondaryStructureStates.COIL.value,
            SecondaryStructureStates.HELIX.value,
            SecondaryStructureStates.HELIX.value,
        ]

        output = PsipredParser(dummy_prediction)
        self.assertEquals(10, len(output))
        self.assertListEqual(expected, output)

    def test_2(self):
        dummy_prediction = """# PSIPRED VFORMAT (PSIPRED V4.0)

           1 M C   0.999  0.001  0.000
           2 S C   0.879  0.094  0.002
           3 L H   0.031  0.972  0.000
           4 E H   0.027  0.976  0.000
           5 A H   0.012  0.989  0.000
           6 T E   0.006  0.996  0.000
           7 V X   0.006  0.996  0.000
           8 L C   0.005  0.997  0.000
           9 D H   0.008  0.994  0.000
          10 L H   0.021  0.984  0.000

"""
        with self.assertRaises(InvalidFormat):
            output = PsipredParser(dummy_prediction)
