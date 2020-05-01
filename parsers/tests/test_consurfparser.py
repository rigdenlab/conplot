import unittest
from parsers import ConsurfParser, ConservationStates


class ConsurfParserTestCase(unittest.TestCase):

    def test_1(self):
        dummy_prediction = """	 Amino Acid Conservation Scores
	===============================

- POS: The position of the AA in the SEQRES derived sequence.
- SEQ: The SEQRES derived sequence in one letter code.
- SCORE: The normalized conservation scores.
- COLOR: The color scale representing the conservation scores (9 - conserved, 1 - variable).
- CONFIDENCE INTERVAL: When using the bayesian method for calculating rates, a confidence interval is assigned to each of the inferred evolutionary conservation scores.
- CONFIDENCE INTERVAL COLORS: When using the bayesian method for calculating rates. The color scale representing the lower and upper bounds of the confidence interval.
- B/E: Burried (b) or Exposed (e) residue.
- FUNCTION: functional (f) or structural (s) residue (f - highly conserved and exposed, s - highly conserved and burried).
- MSA DATA: The number of aligned sequences having an amino acid (non-gapped) from the overall number of sequences at each position.
- RESIDUE VARIETY: The residues variety at each position of the multiple sequence alignment.

 POS	 SEQ	SCORE		COLOR	CONFIDENCE INTERVAL	CONFIDENCE INTERVAL COLORS	B/E	FUNCTION	MSA DATA	RESIDUE VARIETY
    	    	(normalized)	        	               
   1	   M	-0.743		  7*	-1.183,-0.492			    9,6			  e	        	   5/150	V,M
   2	   S	-0.971		  8*	-1.398,-0.769			    9,7			  e	       f	   4/150	S
   3	   L	 0.790		  3*	-0.115, 1.537			    5,1			  e	        	   6/150	L,K,V,I
   4	   E	 0.170		  4	-0.492, 0.493			    6,4			  e	        	  10/150	V,A,E,Q,K
   5	   A	 0.689		  3	-0.115, 1.051			    5,2			  e	        	  12/150	G,D,S,E,N,A,T
   6	   T	 2.476		  1	 1.537, 2.816			    1,1			  b	        	  18/150	V,I,A,S,K,H,T,Y,L,Q,E
   7	   V	-0.163		  5	-0.568, 0.143			    7,5			  b	        	  29/150	M,L,F,V,I
   8	   L	 0.532		  3	 0.006, 0.733			    5,3			  b	        	  38/150	I,V,F,Y,T,M,N,Q,L,D
   9	   D	 0.732		  3	 0.143, 1.051			    5,2			  e	        	  38/150	R,A,E,Q,N,D,S
  10	   L	 2.200		  1	 1.051, 2.816			    2,1			  b	        	  42/150	N,M,L,Y,W,T,H,F,A,V,I
  11	   L	-0.341		  6	-0.639,-0.115			    7,5			  b	        	  52/150	V,I,T,A,L,S,F
  12	   S	 0.266		  4	-0.115, 0.493			    5,4			  e	        	  62/150	P,D,Q,N,E,V,A,R,S,K,G,F
  13	   S	 0.936		  2	 0.493, 1.051			    4,2			  e	        	  71/150	T,E,N,M,L,D,A,V,I,G,F,K,S
  14	   F	 0.092		  5	-0.223, 0.302			    6,4			  b	        	  73/150	L,F,V,I,W
  15	   P	 0.003		  5	-0.321, 0.143			    6,5			  e	        	  76/150	S,K,G,F,H,V,A,N,Q,P,T,W
  16	   H	 2.481		  1	 1.537, 2.816			    1,1			  e	        	  83/150	S,H,G,K,I,V,R,A,N,E,Q,D,L,T,P
  17	   W	-0.322		  6	-0.568,-0.115			    7,5			  e	        	  99/150	Y,W,Q,E,R,C,V,F,G,S
  18	   L	-0.101		  5	-0.321, 0.006			    6,5			  b	        	 114/150	V,I,A,W,M,L,F
  19	   A	 0.961		  2	 0.493, 1.051			    4,2			  b	        	 123/150	Q,E,N,M,L,D,Y,T,H,F,K,S,A,I,V
  20	   T	-0.950		  8	-1.090,-0.885			    8,8			  b	        	 130/150	A,V,I,T,M
  21	   M	-0.237		  6	-0.492,-0.115			    6,5			  b	        	 135/150	L,M,F,I,V,T,A
  22	   V	 0.340		  4	 0.006, 0.493			    5,4			  b	        	 136/150	S,G,F,V,I,A,M,L,T
  23	   I	-0.281		  6	-0.492,-0.115			    6,5			  b	        	 137/150	M,L,W,T,G,F,A,C,I,V
  24	   G	-1.012		  8	-1.137,-0.940			    8,8			  b	        	 138/150	A,T,G,S
  25	   A	-0.826		  8	-0.940,-0.769			    8,7			  b	        	 138/150	S,G,F,V,I,C,A,L,M,T
  26	   M	 0.282		  4	 0.006, 0.493			    5,4			  b	        	 146/150	T,M,L,A,V,I,G,F,S
  27	   P	-1.464		  9	-1.518,-1.442			    9,9			  b	       s	 146/150	P
  28	   I	-0.424		  6	-0.639,-0.321			    7,6			  b	        	 147/150	V,I,T,W,A,L,F
  29	   F	 0.192		  4	-0.115, 0.302			    5,4			  b	        	 147/150	L,T,G,F,S,A,V,I
  30	   E	-1.483		  9	-1.518,-1.489			    9,9			  e	       f	 148/150	E
  31	   L	-1.184		  9	-1.270,-1.137			    9,8			  b	       s	 148/150	S,L,Q,A,V,I
  32	   R	-1.459		  9	-1.518,-1.442			    9,9			  e	       f	 148/150	R,K
  33	   G	-0.645		  7	-0.829,-0.568			    8,7			  e	        	 148/150	I,V,Y,A,L,G,F
  34	   A	-0.914		  8	-1.042,-0.829			    8,8			  b	        	 148/150	I,V,T,A,S,M,G
  35	   I	-1.251		  9	-1.356,-1.227			    9,9			  b	       s	 148/150	L,I,V
  36	   P	-1.190		  9	-1.313,-1.137			    9,8			  b	       s	 148/150	S,L,I,V,P
  37	   I	 0.378		  4	 0.006, 0.493			    5,4			  b	        	 148/150	F,I,V,A,M,L,Y,W
  

*Below the confidence cut-off - The calculations for this site were performed on less than 6 non-gaped homologue sequences,
or the confidence interval for the estimated score is equal to- or larger than- 4 color grades.
"""

        expected = [
            ConservationStates.CONSERVED,
            ConservationStates.CONSERVED,
            ConservationStates.VARIABLE,
            ConservationStates.AVERAGE,
            ConservationStates.VARIABLE,
            ConservationStates.VARIABLE,
            ConservationStates.AVERAGE,
            ConservationStates.VARIABLE,
            ConservationStates.VARIABLE,
            ConservationStates.VARIABLE,
            ConservationStates.AVERAGE,
            ConservationStates.AVERAGE,
            ConservationStates.VARIABLE,
            ConservationStates.AVERAGE,
            ConservationStates.AVERAGE,
            ConservationStates.VARIABLE,
            ConservationStates.AVERAGE,
            ConservationStates.AVERAGE,
            ConservationStates.VARIABLE,
            ConservationStates.CONSERVED,
            ConservationStates.AVERAGE,
            ConservationStates.AVERAGE,
            ConservationStates.AVERAGE,
            ConservationStates.CONSERVED,
            ConservationStates.CONSERVED,
            ConservationStates.AVERAGE,
            ConservationStates.CONSERVED,
            ConservationStates.AVERAGE,
            ConservationStates.AVERAGE,
            ConservationStates.CONSERVED,
            ConservationStates.CONSERVED,
            ConservationStates.CONSERVED,
            ConservationStates.CONSERVED,
            ConservationStates.CONSERVED,
            ConservationStates.CONSERVED,
            ConservationStates.CONSERVED,
            ConservationStates.AVERAGE,
        ]

        parser = ConsurfParser(dummy_prediction)
        parser.parse()
        self.assertFalse(parser.error)
        self.assertIsNotNone(parser.output)
        self.assertEquals(37, len(parser.output))
        self.assertListEqual(expected, parser.output)

    def test_2(self):
        dummy_prediction = """	 Amino Acid Conservation Scores
    ===============================

- POS: The position of the AA in the SEQRES derived sequence.
- SEQ: The SEQRES derived sequence in one letter code.
- SCORE: The normalized conservation scores.
- COLOR: The color scale representing the conservation scores (9 - conserved, 1 - variable).
- CONFIDENCE INTERVAL: When using the bayesian method for calculating rates, a confidence interval is assigned to each of the inferred evolutionary conservation scores.
- CONFIDENCE INTERVAL COLORS: When using the bayesian method for calculating rates. The color scale representing the lower and upper bounds of the confidence interval.
- B/E: Burried (b) or Exposed (e) residue.
- FUNCTION: functional (f) or structural (s) residue (f - highly conserved and exposed, s - highly conserved and burried).
- MSA DATA: The number of aligned sequences having an amino acid (non-gapped) from the overall number of sequences at each position.
- RESIDUE VARIETY: The residues variety at each position of the multiple sequence alignment.
"""
        parser = ConsurfParser(dummy_prediction)
        parser.parse()
        self.assertTrue(parser.error)
        self.assertIsNone(parser.output)
