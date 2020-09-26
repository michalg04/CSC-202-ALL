# Names: Brittani Kealoha and Michal Golovanevsky
#Test cases for Lab 4
# Section: 07

import unittest
from ordered_list import *


class TestOrderedList(unittest.TestCase):
    # tests the functionality of the add function
    def test_add(self):
        test = OrderedList()
        test.add(4)
        test.add(7)
        test.add(0)
        self.assertEqual(test.size(), 3)
        self.assertFalse(test.is_empty())
        test.add(200)
        self.assertEqual(test.size(), 4)
        self.assertFalse(test.is_empty())
        test.pop()
        test.add(45)
        self.assertEqual(test.size(), 4)

    # tests the functionality of the remove funciton
    def test_remove(self):
        test = OrderedList()
        test.add(4)
        test.add(7)
        test.add(0)
        test.add(25)
        test.remove(0)
        self.assertEqual(test.size(), 3)
        self.assertFalse(test.search_forward(0))
        self.assertEqual(test.remove(12), -1)
        self.assertFalse(test.is_empty())
        test.remove(25)
        test.remove(7)
        test.remove(4)
        self.assertTrue(test.is_empty)


    # tests the functionality of search_forward
    def test_search_forward(self):
        test = OrderedList()
        self.assertEqual(test.search_forward(2), False)
        test.add(2)
        self.assertEqual(test.search_forward(2), True)
        self.assertEqual(test.search_forward(3), False)
        test.add(4)
        test.add(5)
        test.add(6)
        test.add(7)
        self.assertEqual(test.search_forward(6), True)
        self.assertEqual(test.search_forward(0), False)

    # tests the functionality of search_backwards
    def test_search_backward(self):
        test = OrderedList()
        self.assertEqual(test.search_backward(2), False)
        test.add(2)
        self.assertEqual(test.search_backward(2), True)
        self.assertEqual(test.search_backward(3), False)
        test.add(4)
        test.add(5)
        test.add(6)
        test.add(7)
        self.assertEqual(test.search_backward(6), True)
        self.assertEqual(test.search_backward(0), False)

    # tests the functionality of is_empty
    def test_is_empty(self):
        test = OrderedList()
        self.assertTrue(OrderedList.is_empty(test))
        test.add(4)
        self.assertFalse(test.is_empty())
        test.add(5)
        test.add(6)
        self.assertFalse(test.is_empty())
        test.add(7)
        self.assertEqual(test.pop(), 7)
        self.assertEqual(test.pop(), 6)
        self.assertFalse(test.is_empty())
        self.assertEqual(test.pop(), 5)
        self.assertFalse(test.is_empty())
        self.assertEqual(test.pop(), 4)
        self.assertTrue(test.is_empty())

    # tests the functionality of size
    def test_size(self):
        test = OrderedList()
        self.assertEqual(test.size(),0)
        test.add(4)
        self.assertEqual(test.size(),1)
        test.add(5)
        test.add(6)
        self.assertEqual(test.size(), 3)
        test.add(7)
        self.assertEqual(test.size(), 4)
        self.assertEqual(test.pop(), 7)
        self.assertEqual(test.pop(), 6)
        self.assertEqual(test.size(), 2)
        self.assertEqual(test.pop(), 5)
        self.assertEqual(test.size(), 1)
        self.assertEqual(test.pop(), 4)
        self.assertEqual(test.size(), 0)

    # tests the functionality of index
    def test_index(self):
        test = OrderedList()
        self.assertEqual(test.index(2), -1)
        test.add(4)
        self.assertEqual(test.index(4), 0)
        test.add(5)
        test.add(6)
        self.assertEqual(test.index(8), -1)
        test.add(7)
        self.assertEqual(test.index(6), 2)
        self.assertEqual(test.pop(), 7)
        self.assertEqual(test.pop(), 6)
        self.assertEqual(test.index(6), -1)
        self.assertEqual(test.pop(), 5)
        self.assertEqual(test.index(4), 0)
        self.assertEqual(test.pop(), 4)
        self.assertEqual(test.index(9), -1)

    # tests the functionality of pop()
    def test_pop(self):
        test = OrderedList()
        test.add(4)
        test.add(7)
        test.add(0)
        test.add(25)
        self.assertEqual(test.pop(), 25)
        self.assertEqual(test.pop(), 7)
        self.assertEqual(test.size(), 2)
        self.assertEqual(test.pop(), 4)
        self.assertFalse(test.is_empty())
        self.assertEqual(test.pop(), 0)
        self.assertTrue(test.is_empty)
        with self.assertRaises(IndexError):
            test.pop()
        self.assertEqual(test.size(), 0)
        test.add(300)
        test.add(35)
        test.pop()
        self.assertEqual(test.size(), 1)

    # tests the functionality of pop(pos)
    def test_pop_pos(self):
        test = OrderedList()
        test.add(4)
        test.add(7)
        test.add(0)
        test.add(25)
        self.assertEqual(test.pop(1), 4)
        self.assertEqual(test.pop(3), -1)
        self.assertEqual(test.pop(2), 25)
        self.assertEqual(test.size(), 2)
        self.assertEqual(test.pop(0), 0)
        self.assertEqual(test.size(), 1)
        self.assertEqual(test.pop(4), -1)
        test.add(16)
        self.assertEqual(test.pop(0), 7)
        self.assertEqual(test.pop(0), 16)
        self.assertTrue(test.is_empty())
        with self.assertRaises(IndexError):
            test.pop(0)
        with self.assertRaises(IndexError):
            test.pop(4)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
