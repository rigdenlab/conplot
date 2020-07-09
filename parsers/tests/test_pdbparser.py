import unittest
from parsers import PDBParser
from utils.exceptions import InvalidFormat


class PDBParserTestCase(unittest.TestCase):

    def test_1(self):
        dummy_prediction = """ATOM      1  N   TYR A  36      39.107  51.628   3.103  0.50 43.13           N
ATOM      2  CA  TYR A  36      38.300  50.814   2.204  0.50 41.80           C
ATOM      3  O   TYR A  36      38.712  48.587   1.405  0.50 41.03           O
ATOM      4  CB  TYR A  36      37.586  51.694   1.175  0.50 41.61           C
ATOM      5  N   PHE A  86      32.465  47.498   5.487  0.50 25.81           N
ATOM      6  CA  PHE A  86      32.670  48.303   4.288  0.50 26.45           C
ATOM      7  O   PHE A  86      31.469  50.326   3.758  0.50 28.47           O
ATOM      8  CB  PHE A  86      32.977  47.392   3.090  0.50 25.35           C
ATOM      9  N   TRP A 171      23.397  37.507  -1.161  0.50 18.04           N
ATOM     10  CA  TRP A 171      23.458  36.846   0.143  0.50 20.46           C
ATOM     11  O   TRP A 171      22.235  34.954   0.951  0.50 22.45           O
ATOM     12  CB  TRP A 171      23.647  37.866   1.275  0.50 18.83           C
ATOM     13  N   PHE A 208      32.221  42.624  -5.829  0.50 19.96           N
ATOM     14  CA  PHE A 208      31.905  43.710  -4.909  0.50 20.31           C
ATOM     15  O   PHE A 208      32.852  45.936  -5.051  0.50 17.69           O
ATOM     16  CB  PHE A 208      31.726  43.102  -3.518  0.50 19.90           C
END
"""

        expected_res1 = [86, 208]
        expected_res2 = [36, 86]
        expected_score = [0.934108, 0.920229]

        output = PDBParser(dummy_prediction)
        self.assertEquals(2, len(output))
        self.assertListEqual(expected_res1, [contact[0] for contact in output])
        self.assertListEqual(expected_res2, [contact[1] for contact in output])
        self.assertListEqual(expected_score, [contact[2] for contact in output])

    def test_2(self):
        dummy_prediction = """###
D U M M Y
100 8 5.382865
"""
        with self.assertRaises(InvalidFormat):
            output = PDBParser(dummy_prediction)
