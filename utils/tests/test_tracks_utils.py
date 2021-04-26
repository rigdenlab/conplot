import os
import unittest
from utils import tracks_utils
from collections import namedtuple

DisplayControlSettings = namedtuple('DisplayControlSettings', ('factor', 'seq_length'))


class TrackUtilsTestCase(unittest.TestCase):

    @unittest.skipIf('THIS_IS_GH_ACTIONS' in os.environ, "not implemented in Travis CI")
    def test_1(self):
        dummy_cmap = [(52, 50), (53, 51), (145, 143), (142, 140), (150, 148), (53, 50), (147, 145), (141, 139),
                      (143, 141), (148, 146)]
        expected_density = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 7, 10, 10, 7, 4, 1, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 7, 6, 5, 6, 6, 5, 5, 4, 4, 3, 2, 1, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        density = tracks_utils.calculate_density(dummy_cmap, 168, 20)
        self.assertListEqual(density, expected_density)

    def test_2(self):
        dummy_cmap_1 = [(52, 50), (53, 51), (145, 143), (142, 140), (150, 148), (53, 50), (147, 145), (141, 139),
                        (143, 141), (148, 146)]
        dummy_cmap_2 = [(52, 50), (53, 51), (145, 143), (142, 140), (150, 148), (53, 50), (147, 145), (141, 139),
                        (143, 141), (148, 146)]
        expected_diff = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1]
        dummy_display_settings = DisplayControlSettings(factor=0, seq_length=168)
        diff = tracks_utils.calculate_diff(dummy_cmap_1, dummy_cmap_2, dummy_display_settings)
        self.assertListEqual(diff, expected_diff)

    def test_3(self):
        dummy_cmap_1 = [(52, 50), (53, 51), (145, 143), (142, 140), (150, 148), (53, 50), (147, 145), (141, 139),
                        (143, 141), (148, 146)]
        dummy_cmap_2 = [(150, 148), (53, 50), (147, 145), (141, 139), (143, 141), (148, 146), (120, 12), (25, 35)]
        expected_diff = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 3, 1, 3, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1]
        dummy_display_settings = DisplayControlSettings(factor=0, seq_length=168)
        diff = tracks_utils.calculate_diff(dummy_cmap_1, dummy_cmap_2, dummy_display_settings)
        self.assertListEqual(diff, expected_diff)

    def test_4(self):
        dummy_cmap_1 = [(52, 50), (53, 51), (145, 143), (142, 140), (150, 148), (53, 50), (147, 145), (141, 139),
                        (143, 141), (148, 146), (10, 55), (5, 145)]
        dummy_cmap_2 = [(150, 148), (53, 50), (147, 145), (141, 139), (143, 141), (148, 146), (120, 12), (25, 35)]
        expected_diff = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 3, 1, 10, 1, 3, 1, 0, 3, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1]
        dummy_display_settings = DisplayControlSettings(factor=20, seq_length=168)

        diff = tracks_utils.calculate_diff(dummy_cmap_1, dummy_cmap_2, dummy_display_settings)
        self.assertListEqual(diff, expected_diff)

    def test_5(self):
        """
        cmap_1
            2 8 9 0
            5 0 0 9
            7 0 0 8
            0 7 5 2
        cmap_2
            9 6 0 0
            5 1 0 0
            5 0 1 6
            0 5 5 9
        """
        cmap_1 = [
            [2, 1, 0, 7],
            [3, 1, 0, 5],
            [4, 1, 0, 2],
            [4, 2, 0, 8],
            [3, 2, 0, 0],
            [4, 3, 0, 9]
        ]

        cmap_2 = [
            [2, 1, 0, 5],
            [3, 1, 0, 5],
            [4, 1, 0, 9],
            [3, 2, 0, 1],
            [4, 2, 0, 6],
            [4, 3, 0, 0]
        ]

        expected = [7, 4, 10, 10]
        output = tracks_utils.get_cmap_rmsd(cmap_1, cmap_2, 4)
        self.assertListEqual(output, expected)
