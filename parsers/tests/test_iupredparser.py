import unittest
from parsers import IupredParser, DisorderStates


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
            DisorderStates.DISORDER,
            DisorderStates.ORDER,
            DisorderStates.DISORDER,
            DisorderStates.DISORDER,
            DisorderStates.ORDER,
            DisorderStates.ORDER,
            DisorderStates.DISORDER,
            DisorderStates.DISORDER,
            DisorderStates.ORDER,
            DisorderStates.ORDER,
        ]

        parser = IupredParser(dummy_prediction)
        parser.parse()
        self.assertFalse(parser.error)
        self.assertIsNotNone(parser.output)
        self.assertEquals(10, len(parser.output))
        self.assertListEqual(expected, parser.output)

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

        parser = IupredParser(dummy_prediction)
        parser.parse()
        self.assertTrue(parser.error)
        self.assertIsNone(parser.output)

    def test_3(self):
        dummy_prediction = """# IUPred2A: context-dependent prediction of protein disorder as a function of redox state and protein binding
    # Balint Meszaros, Gabor Erdos, Zsuzsanna Dosztanyi
    # Nucleic Acids Research 2018, Submitted
    # POS	AMINO ACID	IUPRED SCORE	ANCHOR SCORE
    
    
    
    """

        parser = IupredParser(dummy_prediction)
        parser.parse()
        self.assertTrue(parser.error)
        self.assertIsNone(parser.output)
