import unittest
from parsers import TopconsParser, MembraneStates, InvalidFormat


class TopconsParserTestCase(unittest.TestCase):

    def test_1(self):
        dummy_prediction = """##############################################################################
TOPCONS2 result file
Generated from http://topcons.cbr.su.se at 2019-08-15 10:48:49 CEST
Total request time: 0.4 seconds.
##############################################################################
Sequence number: 1
Sequence name: tr|W9DY28|W9DY28_METTI Putative membrane protein OS=Methanolobus tindarius DSM 2278 OX=1090322 GN=MettiDRAFT_2055 PE=4 SV=1
Sequence length: 10 aa.
Sequence:
MSLEATVLDL


TOPCONS predicted topology:
iiMMMoooiM


OCTOPUS predicted topology:
MiMiMoioiM


Philius predicted topology:
oiMMMMooio



Homology:
No homologous hits found



Predicted Delta-G-values (kcal/mol) (left column=sequence position; right column=Delta-G)

10 5.196
11 5.185
12 4.762
13 5.008
14 4.287

Predicted TOPCONS reliability (left column=sequence position; right column=reliability)

11	95.24
12	95.24
13	95.24
14	95.24

##############################################################################

"""

        expected = [
            MembraneStates.INSIDE.value,
            MembraneStates.INSIDE.value,
            MembraneStates.INSERTED.value,
            MembraneStates.INSERTED.value,
            MembraneStates.INSERTED.value,
            MembraneStates.OUTSIDE.value,
            MembraneStates.OUTSIDE.value,
            MembraneStates.OUTSIDE.value,
            MembraneStates.INSIDE.value,
            MembraneStates.INSERTED.value,
        ]

        output = TopconsParser(dummy_prediction)
        self.assertEquals(10, len(output))
        self.assertListEqual(expected, output)

    def test_2(self):
        dummy_prediction = """##############################################################################
TOPCONS2 result file
Generated from http://topcons.cbr.su.se at 2019-08-15 10:48:49 CEST
Total request time: 0.4 seconds.
##############################################################################
Sequence number: 1
Sequence name: tr|W9DY28|W9DY28_METTI Putative membrane protein OS=Methanolobus tindarius DSM 2278 OX=1090322 GN=MettiDRAFT_2055 PE=4 SV=1
Sequence length: 10 aa.
Sequence:
MSLEATVLDL


TOPCONS predicted topology:
iiMXMoooiM


OCTOPUS predicted topology:
MiMiMoioiM


Philius predicted topology:
oiMMMMooio



Homology:
No homologous hits found



Predicted Delta-G-values (kcal/mol) (left column=sequence position; right column=Delta-G)

10 5.196
11 5.185
12 4.762
13 5.008
14 4.287

Predicted TOPCONS reliability (left column=sequence position; right column=reliability)

11	95.24
12	95.24
13	95.24
14	95.24

##############################################################################

"""
        with self.assertRaises(InvalidFormat):
            output = TopconsParser(dummy_prediction)
