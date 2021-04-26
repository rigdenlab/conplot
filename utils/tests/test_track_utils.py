import unittest
from utils import tracks_utils


class TrackUtilsTestCase(unittest.TestCase):

    def test_1(self):
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
