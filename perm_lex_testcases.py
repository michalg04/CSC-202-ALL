#Test Cases for Lab2
# Name: Michal Golovanevsky
# Section: 7

from perm_lex import *

import unittest

class TestCase(unittest.TestCase):
    def test_perm_lex(self):
        # tests to see if the program works with basic input
        self.assertEqual(perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        # tests to see if the program works with basic input
        self.assertEqual(perm_gen_lex('ab'),['ab', 'ba'])
        # tests to see if the program works with basic input
        self.assertEqual(perm_gen_lex('cde'), ['cde', 'ced', 'dce', 'dec', 'ecd', 'edc'])
        # tests to see if the program works with empty string
        self.assertEqual(perm_gen_lex(''), [])
        # tests to see if the program works with a single letter
        self.assertEqual(perm_gen_lex('a'), ['a'])

# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()
