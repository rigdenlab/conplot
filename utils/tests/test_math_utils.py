import unittest
from utils import math_utils


class MathUtilsTestCase(unittest.TestCase):

    def test_1(self):
        dummy_cmap = [(52, 50), (53, 51), (145, 143), (142, 140), (150, 148), (53, 50), (147, 145), (141, 139),
                      (143, 141), (148, 146)]
        expected_density = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 7, 10, 10, 7, 4, 1, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 5, 8, 10, 9, 8, 8, 8, 8, 8, 7, 6, 4, 2, 1, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        density = math_utils.get_contact_density(dummy_cmap, 168)
        print(density)
        self.assertListEqual(density, expected_density)
