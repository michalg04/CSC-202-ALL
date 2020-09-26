# Name: Michal Golovanevsky
# Section: 7
#Test cases for Project 2

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    #tests invalid postfix expressions
    def test_invalid(self):
        #tests empty postfix
        self.assertFalse(postfix_valid(""))
        #tests no operator
        self.assertFalse(postfix_valid("2 3"))
        #tests no operands
        self.assertFalse(postfix_valid("- +"))
        # tests multiple operators
        self.assertFalse(postfix_valid("3 * +"))
        #tests empty with space
        self.assertFalse(postfix_valid(" "))
        #tests infix expressions
        self.assertFalse(postfix_valid("6 ^ 3 ^ 2"))
        self.assertFalse(postfix_valid("6 - 3"))
        self.assertFalse(postfix_valid("6 * ( 3 + 2 )"))
        self.assertFalse(postfix_valid("9 * ( ( 2 + 3 ) * 5 ) ^ ( 7 - 9 ) ^ ( ( 5 * 2 ) + 3 ) + 1"))

    # tests valid postfix expressions
    def test_valid(self):
        #test addition
        self.assertTrue(postfix_valid("2 3 +"))
        # test subtraciton
        self.assertTrue(postfix_valid("2 3 -"))
        # test multiplication
        self.assertTrue(postfix_valid("2 3 *"))
        # test division
        self.assertTrue(postfix_valid("2 3 /"))
        # test exponentiation
        self.assertTrue(postfix_valid("2 3 ^"))
        #tests more complex expressions
        self.assertTrue(postfix_valid("6 3 2 + *"))
        self.assertTrue(postfix_valid("6 3 - 2 +"))
        self.assertTrue(postfix_valid("6 3 2 ^ ^"))
        self.assertTrue(postfix_valid("9 2 3 + 5 * 7 9 - 5 2 * 3 + ^ ^ * 1 +"))
        #tests single number
        self.assertTrue(postfix_valid("6"))
        # tests multiple digits
        self.assertTrue(postfix_valid("60"))
        self.assertTrue(postfix_valid("6 72 +"))
        self.assertTrue(postfix_valid("6 3 2000 + *"))
        # tests negative numbers
        self.assertTrue(postfix_valid("-6 3 2000 + *"))
        # tests decimals
        self.assertTrue(postfix_valid("6.78 3 2000 + *"))
        #tests extra prantasis
        self.assertTrue(postfix_valid("(6) (72) +"))

    #tests postfix evaluation with basic addition
    def test_postfixeval1(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    # tests postfix evaluation with decimals
    def test_postfixeval1(self):
        self.assertAlmostEqual(postfix_eval("3.5 5 +"), 8.5)

    # tests postfix evaluation with negative numbers
    def test_postfixeval1(self):
        self.assertAlmostEqual(postfix_eval("-3 5 +"), 2)

    # tests postfix evaluation with multiple digit number
    def test_postfixeval1(self):
        self.assertAlmostEqual(postfix_eval("30 5 +"), 35)

    def test_postfixeval1(self):
        self.assertAlmostEqual(postfix_eval("300 5 +"), 305)

    # tests postfix to infix with subtraction
    def test_inToPostBasicAssoc(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")

    def test_inToPostBasicAssoc1(self):
        self.assertEqual(infix_to_postfix("6 - 3 + 2"), "6 3 - 2 +")

    # tests postfix to infix with exponentiation
    def test_inToPostBasicAssoc2(self):
        self.assertEqual(infix_to_postfix("6 ^ 3 ^ 2"), "6 3 2 ^ ^")

    # tests postfix to infix with more complex inputs
    def test_inToPostBasicAssoc3(self):
        self.assertEqual(infix_to_postfix("6 * ( 3 + 2 )"), "6 3 2 + *")

    def test_inToPostBasicAssoc3(self):
        self.assertEqual(infix_to_postfix("19 * ( ( 2 + 3 ) * 5 ) ^ ( 7 - 9 ) ^ ( ( 5 * 2 ) + 305 ) + 10"), "19 2 3 + 5 * 7 9 - 5 2 * 305 + ^ ^ * 10 +")

    # tests postfix to infix with more complex inputs and negatives
    def test_inToPostBasicAssoc3(self):
        self.assertEqual(infix_to_postfix("-6 * ( -3 + 2 )"), "-6 -3 2 + *")

    # tests postfix to infix with more complex inputs and decimals
    def test_inToPostBasicAssoc3(self):
        self.assertEqual(infix_to_postfix("6.689 * ( 3 + 2.1 )"), "6.689 3 2.1 + *")

    # tests postfix to infix with more complex inputs and multiple digits
    def test_inToPostBasicAssoc3(self):
        self.assertEqual(infix_to_postfix("605 * ( 3000 + 2 )"), "605 3000 2 + *")

    # tests postfix to infix with one number
    def test_inToPostBasicAssoc5(self):
        self.assertEqual(infix_to_postfix("6"), "6")
        #tests that an error rises when divided by zero
        with self.assertRaises(ValueError): 
            postfix_eval("3 0 /")
        with self.assertRaises(ValueError):
            postfix_eval("3000 0 /")

if __name__ == "__main__":
    unittest.main()
