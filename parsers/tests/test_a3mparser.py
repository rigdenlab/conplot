import unittest
from parsers import A3mParser
from utils.exceptions import InvalidFormat


class A3mParserTestCase(unittest.TestCase):

    def test_1(self):
        dummy_msa = """ >example
ETESMKTVRIREKIKKFLGDRPRNTAEILEHINSTMRHGTTSQQLGNVLSKDKDIVKVGYIKRSGILSGGYDICEWATRNWVAEHCPEWTE
>1
----MRTTRLRQKIKKFLNERGeANTTEILEHVNSTMRHGTTPQQLGNVLSKDKDILKVATTKRGGALSGRYEICVWTLRP-----------
>2
----MDSQNLRDLIRNYLSERPRNTIEISAWLASQMDPNSCPEDVTNILEADESIVRIGTVRKSGMRLTDLPISEWASSSWVRRHE-----
>3
----MNSQNLRELIRNYLSERPRNTIEISTWLSSQIDPTNSPVDITSILEADDQIVRIGTVRKSGMRRSESPVSEWASNTWVKHHE-----
>4
--RDMDTEKVREIVRNYISERPRNTAEIAAWLNRH-DDGTGGSDVAAILESDGSFVRIGTVRTSGMTGNSPPLSEWATEKWIQHHER----
>5
-----RTRRLREAVLVFLEEKGnANTVEVFDYLNERFRWGATMNQVGNILAKDTRFAKVGHQ-RGQFRGSVYTVCVWALS------------
>6
-----RTKRLREAVRVYLAENGrSHTVDIFDHLNDRFSWGATMNQVGNILAKDNRFEKVGHVRD-FFRGARYTVCVWDLAS-----------"""

        expected_output = [0, 0, 2, 2, 7, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                           10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 8, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                           10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 8, 10, 8, 10, 10, 10, 10, 10, 10, 10,
                           10, 10, 10, 10, 10, 10, 10, 10, 8, 5, 5, 5, 5, 5, 5, 2, 0, 0, 0, 0]

        output = A3mParser(dummy_msa)

        self.assertListEqual(output, expected_output)

    def test_2(self):
        dummy_msa = """###
D U M M Y
100 8 5.382865
"""
        with self.assertRaises(InvalidFormat):
            output = A3mParser(dummy_msa)
            self.assertListEqual(output, [])

    def test_3(self):
        dummy_msa = """">example
ETESMKTVRIREKIKKFL8GDRPRNTAEILEHINSTMRHGTTSQQLGNVLSKDKDIVKVGYIKRSGILSGGYDICEWATRNWVAEHCPEWTE
>1
----MRTTRLRQKIKKFLNERGeANTTEILEHVNSTMRHGTTPQQLGNVLSKDKDILKVATTKRGGALSGRYEICVWTLRP-----------
>2
----MDSQNLRDLIRNYLSERPRNTIEISAWLASQMDPNSCPEDVTNILEADESIVRIGTVRKSGMRLTDLPISEWASSSWVRRHE-----
>3
----MNSQNLRELIRNYLSERPRNTIEISTWLSSQIDPTNSPVDITSILEADDQIVRIGTVRKSGMRRSESPVSEWASNTWVKHHE-----
>4
--RDMDTEKVREIVRNYISERPRNTAEIAAWLNRH-DDGTGGSDVAAILESDGSFVRIGTVRTSGMTGNSPPLSEWATEKWIQHHER----
>5
-----RTRRLREAVLVFLEEKGnANTVEVFDYLNERFRWGATMNQVGNILAKDTRFAKVGHQ-RGQFRGSVYTVCVWALS------------
>6
-----RTKRLREAVRVYLAENGrSHTVDIFDHLNDRFSWGATMNQVGNILAKDNRFEKVGHVRD-FFRGARYTVCVWDLAS-----------"""
        with self.assertRaises(InvalidFormat):
            output = A3mParser(dummy_msa)