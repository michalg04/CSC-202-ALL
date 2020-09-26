#Test Cases for Lab1
# Name: Michal Golovanevsky
# Section: 7

from Lab1 import *

import unittest

class TestCase(unittest.TestCase):

    def test_max_list_iter(self):
        tlist = [10, 9, 8, 4, 9]
        self.assertEqual(max_list_iter(tlist), 10)
        tlist = []
        with self.assertRaises(ValueError):  # magic - uses context manager
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec("abcd"), "dcba")

    def test_bin_search(self):
        #tests to see if the program works with basic input
        list_val = [1, 3, 4, 7, 12, 40, 99]
        self.assertEqual(bin_search(7, 1, 5, list_val), 3)
        #tests to see if the program works with high and low being greater than the length of the list
        with self.assertRaises(ValueError):
            bin_search(7, 10, 17, list_val)
        #tests to see if the program works with low being greater than high
        self.assertEqual(bin_search(7, 6, 2, list_val), None)
        #tests to see if the program works with a negative boundry
        with self.assertRaises(ValueError):
            bin_search(7, -6, 2, list_val)
        #tests to see if the program works with an empty list
        list_val = []
        self.assertEqual(bin_search(7, 1, 3, list_val), None)
        #tests to see if the program works with an unsorted list
        list_val = [1, 10, 0, 7, 2, 15, 40, 15]
        self.assertEqual(bin_search(7, 1, 5, list_val), 3)
        # tests to see if the program works with target not in the list
        list_val = [1, 3, 4, 12, 40, 99]
        self.assertEqual(bin_search(7, 1, 5, list_val), None)


        # Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()

