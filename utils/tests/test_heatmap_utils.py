import unittest
from utils import heatmap_utils


class HeatmapUtilsTestCase(unittest.TestCase):

    def test_1(self):
        expected_heat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected_hover = [[None, None, None], [None, None, None], [None, None, None]]
        heat, hover = heatmap_utils.init_heatmap(2)
        self.assertListEqual(expected_hover, hover.tolist())
        self.assertListEqual(expected_heat, heat.tolist())
