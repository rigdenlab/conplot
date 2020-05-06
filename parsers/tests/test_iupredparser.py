import unittest
from parsers import IupredParser, DisorderStates
from utils.exceptions import InvalidFormat


class IupredParserTestCase(unittest.TestCase):

    def test_1(self):
        dummy_prediction = """# IUPred2A: context-dependent prediction of protein disorder as a function of redox state and protein binding
# Balint Meszaros, Gabor Erdos, Zsuzsanna Dosztanyi
# Nucleic Acids Research 2018, Submitted
# POS	AMINO ACID	IUPRED SCORE	ANCHOR SCORE
1	M	0.5000	0.0076
2	S	0.0083	0.0074
3	L	0.6108	0.0073
4	E	0.5040	0.0072
5	A	0.4093	0.0068
6	T	0.0113	0.0067
7	V	0.7000	0.0061
8	L	0.9800	0.0057
9	D	0.1065	0.0056
10	L	0.3482	0.0050



"""

        expected = [
            DisorderStates.DISORDER.value,
            DisorderStates.ORDER.value,
            DisorderStates.DISORDER.value,
            DisorderStates.DISORDER.value,
            DisorderStates.ORDER.value,
            DisorderStates.ORDER.value,
            DisorderStates.DISORDER.value,
            DisorderStates.DISORDER.value,
            DisorderStates.ORDER.value,
            DisorderStates.ORDER.value,
        ]

        output = IupredParser(dummy_prediction)
        self.assertEquals(10, len(output))
        self.assertListEqual(expected, output)

    def test_2(self):
        dummy_prediction = """# IUPred2A: context-dependent prediction of protein disorder as a function of redox state and protein binding
# Balint Meszaros, Gabor Erdos, Zsuzsanna Dosztanyi
# Nucleic Acids Research 2018, Submitted
# POS	AMINO ACID	IUPRED SCORE	ANCHOR SCORE
1	M	0.X000	0.0076
2	S	0.0083	0.0074
3	L	0.6108	0.0073
4	E	0.5040	0.0072
5	A	0.4093	0.0068
6	T	0.0113	0.0067
7	V	0.7000	0.0061
8	L	0.9800	0.0057
9	D	0.1065	0.0056
10	L	0.3482	0.0050



"""

        with self.assertRaises(InvalidFormat):
            output = IupredParser(dummy_prediction)

    def test_3(self):
        dummy_prediction = """# IUPred2A: context-dependent prediction of protein disorder as a function of redox state and protein binding
    # Balint Meszaros, Gabor Erdos, Zsuzsanna Dosztanyi
    # Nucleic Acids Research 2018, Submitted
    # POS	AMINO ACID	IUPRED SCORE	ANCHOR SCORE
    
    
    
    """

        with self.assertRaises(InvalidFormat):
            output = IupredParser(dummy_prediction)
