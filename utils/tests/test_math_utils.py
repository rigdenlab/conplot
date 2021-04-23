import unittest
from utils import math_utils
import numpy as np


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

    def test_2(self):
        expected_output = 3.0210772833723656
        output = math_utils.calculate_mcc(5, 2, 120, 2)
        self.assertEqual(output, expected_output)

    def test_3(self):
        expected_output = 1
        output = math_utils.calculate_mcc(0, 0, 120, 2)
        self.assertEqual(output, expected_output)

    def test_4(self):
        expected_output = 10
        output = math_utils.calculate_mcc(12, 1, 0, 2)
        self.assertEqual(output, expected_output)

    def test_5(self):
        expected_output = 24.714285714285715
        expected_array = np.array([10, 8, 1, 5, 5, 7, 5, 8, 5, 6, 8, 2, 1, 9])
        observed_array = np.array([1, 8, 10, 1, 5, 3, 7, 5, 1, 3, 8, 9, 0, 1])
        output = math_utils.calculate_rmsd(expected_array, observed_array)
        self.assertEqual(output, expected_output)
