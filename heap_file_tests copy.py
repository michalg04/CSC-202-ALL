#Test Cases for Lab7
#Name: Michal Golovanevsky
#Section: 7

from heap_lab import *

import unittest

class TestCase(unittest.TestCase):
    def test_insert(self):
        heap = MaxHeap(4)
        #tests if_empty
        self.assertTrue(heap.is_empty())
        self.assertTrue(heap.insert(8))
        self.assertTrue(heap.insert(0))
        self.assertTrue(heap.insert(17))
        self.assertFalse(heap.is_empty())
        # tests if_full
        self.assertFalse(heap.is_full())
        self.assertTrue(heap.insert(-2))
        self.assertTrue(heap.is_full())
        self.assertFalse(heap.insert(8))

    def test_find_max(self):
        alist = [9, 12, 0, 8, -5, 42, 16, 3]
        heap = MaxHeap(50)
        self.assertTrue(heap.build_heap(alist))
        self.assertTrue(heap.find_max(), 42)
        #tests if empty list
        alist = []
        heap = MaxHeap(50)
        self.assertFalse(heap.build_heap(alist))
        self.assertEqual(heap.find_max(), None)
        # tests one element
        alist = [7]
        heap = MaxHeap(50)
        self.assertTrue(heap.build_heap(alist))
        self.assertEqual(heap.find_max(), 7)

    def test_del_max(self):
        heap = MaxHeap(7)
        alist = [1, 7, 0, 8]
        self.assertTrue(heap.build_heap(alist))
        self.assertEqual(heap.get_heap_size(), 4)
        self.assertEqual(heap.del_max(), 8)
        self.assertEqual(heap.get_heap_size(), 3)
        self.assertEqual(heap.del_max(), 7)
        self.assertEqual(heap.get_heap_size(), 2)
        self.assertEqual(heap.del_max(), 1)
        self.assertEqual(heap.get_heap_size(), 1)
        self.assertEqual(heap.del_max(), 0)
        self.assertEqual(heap.get_heap_size(), 0)
        #tests deleting when empty
        self.assertFalse(heap.del_max())
        self.assertEqual(heap.get_heap_size(), 0)

    def test_heap_contents(self):
        alist = [9, 12, 0, 8, -5, 42, 16, 3]
        heap = MaxHeap(50)
        self.assertTrue(heap.build_heap(alist))
        self.assertEqual(heap.heap_contents(), [42, 12, 16, 8, -5, 0, 9, 3])
        #empty list
        alist = []
        heap = MaxHeap(50)
        self.assertFalse(heap.build_heap(alist))
        self.assertEqual(heap.heap_contents(), [])
        # one element
        alist = [7]
        heap = MaxHeap(50)
        self.assertTrue(heap.build_heap(alist))
        self.assertEqual(heap.heap_contents(), [7])

    def test_build_heap(self):
        alist = [9, 12, 0, 8, -5, 42, 16, 3]
        heap = MaxHeap(50)
        self.assertTrue(heap.build_heap(alist))
        self.assertEqual(heap.heap_contents(), [42, 12, 16, 8, -5, 0, 9, 3])
        # empty list
        alist = []
        heap = MaxHeap(50)
        self.assertFalse(heap.build_heap(alist))
        self.assertEqual(heap.heap_contents(), [])
        # one element
        alist = [7]
        heap = MaxHeap(50)
        self.assertTrue(heap.build_heap(alist))
        self.assertEqual(heap.heap_contents(), [7])

    def test_get_heap_cap(self):
        heap = MaxHeap(7)
        self.assertEqual(heap.get_heap_cap(), 7)
        heap = MaxHeap(50)
        self.assertEqual(heap.get_heap_cap(), 50)
        heap = MaxHeap(0)
        self.assertEqual(heap.get_heap_cap(), 0)

    def test_get_heap_size(self):
        heap = MaxHeap(7)
        alist = [1, 7, 0, 8]
        self.assertTrue(heap.build_heap(alist))
        self.assertEqual(heap.get_heap_size(), 4)
        self.assertTrue(heap.insert(5))
        self.assertEqual(heap.get_heap_size(), 5)
        self.assertTrue(heap.insert(19))
        self.assertEqual(heap.get_heap_size(), 6)
        self.assertEqual(heap.del_max(), 19)
        self.assertEqual(heap.get_heap_size(), 5)


    def test_heap_sort_increase(self):
        alist = [9, 12, 0, 8, -5, 42, 16, 3]
        heap = MaxHeap(50)
        self.assertEqual(heap.heap_sort_increase(alist), [-5, 0, 3, 8, 9, 12, 16, 42])
        alist = [1, 2, 3, 4]
        heap = MaxHeap(50)
        self.assertEqual(heap.heap_sort_increase(alist),[1, 2, 3, 4])
        alist = [4, 3, 2, 1]
        heap = MaxHeap(50)
        self.assertEqual(heap.heap_sort_increase(alist), [1, 2, 3, 4])
        #empty list
        alist = []
        heap = MaxHeap(50)
        self.assertEqual(heap.heap_sort_increase(alist), [])
        # one element
        alist = [3]
        heap = MaxHeap(50)
        self.assertEqual(heap.heap_sort_increase(alist), [3])

if (__name__ == '__main__'):
    unittest.main()
