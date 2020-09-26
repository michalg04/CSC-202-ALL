# Names: Brittani Kealoha and Michal Golovanevsky
# Section: 07

import unittest
from ordered_list import *


class TestOrderedList(unittest.TestCase):
    # Michal Golovanevsky
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


    # Michal Golovanevsky
    def test_remove(self):
        test = OrderedList()
        test.add(4)
        test.add(7)
        test.add(0)
        test.add(25)
        test.remove(0)
        self.assertEqual(test.size(), 3)
        self.assertFalse(test.search_forward(0))

    # Kealoha
    # tests the functionality of search_forward
    def test_search_forward(self):
        test = OrderedList()
        self.assertEqual(OrderedList.search_forward(test, 2), False)
        # test.add(2)
        # self.assertEqual(test.search_forward(2), True)
        # self.assertEqual(test.search_forward(3), False)
        # test.add(4)
        # test.add(5)
        # test.add(6)
        # test.add(7)
        # self.assertEqual(OrderedList.search_forward(6), True)
        # self.assertEqual(OrderedList.search_forward( 0), False)

    # Kealoha
    # tests the functionality of search_backwards
    def test_search_backward(self):
        test = OrderedList()
        self.assertEqual(OrderedList.search_backward(test, 2), False)
        # self.assertEqual(OrderedList.search_backwards(test, 2), True)
        # self.assertEqual(OrderedList.search_backwards(test, 3), False)
        # OrderedList.add(test, 4)
        # OrderedList.add(test, 5)
        # OrderedList.add(test, 6)
        # OrderedList.add(test, 7)
        # self.assertEqual(OrderedList.search_backwards(test, 6), True)
        # self.assertEqual(OrderedList.search_backwards(test, 0), False)

    # Kealoha
    # tests the functionality of is_empty
    def test_is_empty(self):
        test = OrderedList()
        self.assertTrue(OrderedList.is_empty(test))
        # OrderedList.add(test, 4)
        # self.assertFalse(OrderedList.is_empty(test))
        # OrderedList.add(test, 5)
        # OrderedList.add(test, 6)
        # self.assertFalse(OrderedList.is_empty(test))
        # OrderedList.add(test, 7)
        # self.assertEqual(OrderedList.pop(test), 7)
        # self.assertEqual(OrderedList.pop(test), 6)
        # self.assertFalse(OrderedList.is_empty(test))
        # self.assertEqual(OrderedList.pop(test), 5)
        # self.assertFalse(OrderedList.is_empty(test))
        # self.assertEqual(OrderedList.pop(test), 4)
        # self.assertTrue(OrderedList.is_empty(test))

    # Kealoha
    # tests the functionality of size
    def test_size(self):
        test = OrderedList()
        self.assertEqual(OrderedList.size(test),0)
        # OrderedList.add(test, 4)
        # self.assertEqual(OrderedList.size(test),1)
        # OrderedList.add(test, 5)
        # OrderedList.add(test, 6)
        # self.assertEqual(OrderedList.size(test), 3)
        # OrderedList.add(test, 7)
        # self.assertEqual(OrderedList.size(test), 4)
        # self.assertEqual(OrderedList.pop(test), 7)
        # self.assertEqual(OrderedList.pop(test), 6)
        # self.assertEqual(OrderedList.size(test), 2)
        # self.assertEqual(OrderedList.pop(test), 5)
        # self.assertEqual(OrderedList.size(test), 1)
        # self.assertEqual(OrderedList.pop(test), 4)
        # self.assertEqual(OrderedList.size(test), 0)

    # Kealoha
    # tests the functionality of index
    def test_index(self):
        test = OrderedList()
        self.assertEqual(OrderedList.index(test, 2), -1)
        # OrderedList.add(test, 4)
        # self.assertEqual(OrderedList.index(test, 4), 0)
        # OrderedList.add(test, 5)
        # OrderedList.add(test, 6)
        # self.assertEqual(OrderedList.index(test, 8), -1)
        # OrderedList.add(test, 7)
        # self.assertEqual(OrderedList.index(test, 6), 2)
        # self.assertEqual(OrderedList.pop(test), 7)
        # self.assertEqual(OrderedList.pop(test), 6)
        # self.assertEqual(OrderedList.index(test, 6), -1)
        # self.assertEqual(OrderedList.pop(test), 5)
        # self.assertEqual(OrderedList.index(test, 4), 0)
        # self.assertEqual(OrderedList.pop(test), 4)
        # self.assertEqual(OrderedList.index(test, 9), -1)

    # Michal Golovanevsky
    def test_pop(self):
        pass
    # Michal Golovanevsky
    def test_pop_pos(self):
        pass


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
