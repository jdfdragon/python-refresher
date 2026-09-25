import unittest
from random import uniform
from random import gauss
import os
import sys

# Allows running from main directory, my_utils is there.
module_path = os.path.abspath(".")

sys.path.append(module_path)

import my_utils  # noqa


class TestUtils(unittest.TestCase):

    """get_mean() Tests"""
    # Test mean function even
    def test_mean_pos4(self):
        lst = [1, 2, 4, 5]
        m = my_utils.get_mean(lst)
        self.assertEqual(m, 3)

    def test_mean_neg4(self):
        lst = [-1, -2, -4, -5]
        m = my_utils.get_mean(lst)
        self.assertEqual(m, -3)

    # Test mean function odd
    def test_mean_pos5(self):
        lst = [2, 3, 4, 5, 6]
        m = my_utils.get_mean(lst)
        self.assertEqual(m, 4)

    def test_mean_neg5(self):
        lst = [-2, -3, -4, -5, -6]
        m = my_utils.get_mean(lst)
        self.assertEqual(m, -4)

    # Test mean function float
    def test_mean_posFloat(self):
        lst = [1.5, 2.5, 4.5, 5.5]
        m = my_utils.get_mean(lst)
        self.assertEqual(m, 3.5)

    def test_mean_negFloat(self):
        lst = [-1.5, -2.5, -4.5, -5.5]
        m = my_utils.get_mean(lst)
        self.assertEqual(m, -3.5)

    # Assorted mean error handling
    def test_mean_str(self):
        lst = ["a", 1, 2]
        self.assertRaises(SystemExit, my_utils.get_mean, lst)

    def test_mean_empty(self):
        lst = []
        self.assertRaises(SystemExit, my_utils.get_mean, lst)

    def test_mean_none(self):
        lst = None
        self.assertRaises(SystemExit, my_utils.get_mean, lst)

    # Test mean large numbers
    def test_mean_rand(self):
        lst = [uniform(-10, 10) for _ in range(100000)]
        m = my_utils.get_mean(lst)
        self.assertAlmostEqual(m, 0, 1)

    """get_median() Tests"""
    # Test median function even
    def test_median_pos4(self):
        lst = [1, 2, 4, 10]
        m = my_utils.get_median(lst)
        self.assertEqual(m, 3)

    def test_median_neg4(self):
        lst = [-1, -2, -4, -10]
        m = my_utils.get_median(lst)
        self.assertEqual(m, -3)

    # Test median function odd
    def test_median_pos5(self):
        lst = [1, 3, 4, 6, 20]
        m = my_utils.get_median(lst)
        self.assertEqual(m, 4)

    def test_median_neg5(self):
        lst = [-1, -3, -4, -6, -20]
        m = my_utils.get_median(lst)
        self.assertEqual(m, -4)

    # Test median float
    def test_median_posFloat(self):
        lst = [0.1, 3.5, 4.5, 800.2]
        m = my_utils.get_median(lst)
        self.assertEqual(m, 4)

    def test_median_negFloat(self):
        lst = [-0.1, -3.5, -4.5, -800.2]
        m = my_utils.get_median(lst)
        self.assertEqual(m, -4)

    # Assorted median error handling
    def test_median_str(self):
        lst = ["a", 1, "2"]
        self.assertRaises(SystemExit, my_utils.get_median, lst)

    def test_median_empty(self):
        lst = []
        self.assertRaises(SystemExit, my_utils.get_median, lst)

    def test_median_none(self):
        lst = None
        self.assertRaises(SystemExit, my_utils.get_median, lst)

    def test_median_order(self):
        lower = [uniform(-10, 0) for _ in range(10)]
        upper = [uniform(0, 10) for _ in range(10)]
        lst = upper + lower + [0]  # Keep bad order for testing, keep 0 too
        m = my_utils.get_median(lst)
        self.assertEqual(m, 0)

    # Test median large numbers
    def test_median_large(self):
        lst = [uniform(10, 20) for _ in range(1000000)]
        m = my_utils.get_median(lst)
        self.assertAlmostEqual(m, 15, 1)

    """get_sd() Tests"""
    # Test sd function even
    def test_sd_pos4(self):
        lst = [0, 0, 2, 2]
        sd = my_utils.get_sd(lst)
        self.assertAlmostEqual(sd, 1)

    def test_sd_neg4(self):
        lst = [0, 0, -2, -2]
        sd = my_utils.get_sd(lst)
        self.assertAlmostEqual(sd, 1)

    # Test sd function float
    def test_sd_Float(self):
        lst = [-2.45, 0, 2.449]
        sd = my_utils.get_sd(lst)
        self.assertAlmostEqual(sd, 2, 4)

    # Assorted sd error handling
    def test_sd_str(self):
        lst = ["a", 1, 2]
        self.assertRaises(SystemExit, my_utils.get_sd, lst)

    def test_sd_empty(self):
        lst = []
        self.assertRaises(SystemExit, my_utils.get_sd, lst)

    def test_sd_none(self):
        lst = None
        self.assertRaises(SystemExit, my_utils.get_sd, lst)

    # Test sd function large numbers
    def test_sd_large(self):
        lst = [gauss(0, 1) for _ in range(100000)]
        sd = my_utils.get_sd(lst)
        self.assertAlmostEqual(sd, 1, 2)


if __name__ == '__main__':
    unittest.main()
