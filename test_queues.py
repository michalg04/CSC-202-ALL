#Test Cases for Lab 3
# Name: Michal Golovanevsky
# Section: 7

import unittest
import queues

class TestCases(unittest.TestCase):
   def test_queue_array(self):
       queue1 = queues.QueueArray(5)
       #tests enqueue
       queue1.enqueue(3)
       #test num_in_queue
       self.assertEqual(queue1.num_in_queue(), 1)
       queue1.enqueue('a')
       # tests if is_full returns false when queue is not full
       self.assertFalse(queue1.is_full())
       queue1.enqueue(17)
       queue1.enqueue(25)
       queue1.enqueue('b')
       # tests if is_empty returns false when queue is full
       self.assertFalse(queue1.is_empty())
       # test if is_full returns true when list is full
       self.assertTrue(queue1.is_full())
       # tests that error is raised when enqueue is called on a full queue
       with self.assertRaises(IndexError):
           queue1.enqueue(9)
       # tests dequeue
       queue1.dequeue()
       queue1.dequeue()
       # test num_in_queue
       self.assertEqual(queue1.num_in_queue(), 3)
       queue1.dequeue()
       queue1.dequeue()
       queue1.dequeue()
       # tests if is_full returns false when queue is empty
       self.assertFalse(queue1.is_full())
       # tests if is_empty returns true when queue is empty
       self.assertTrue(queue1.is_empty())
       # tests that error is raised when dequeue is called on an empty queue
       with self.assertRaises(IndexError):
            queue1.dequeue()
       # tests num_in_queue works with empty queue
       self.assertEqual(queue1.num_in_queue(), 0)


   def test_queue_linked(self):
       queue1 = queues.QueueLinked(5)
       #tests enqueue
       queue1.enqueue(3)
       #test num_in_queue
       self.assertEqual(queue1.num_in_queue(), 1)
       queue1.enqueue('a')
       # tests if is_full returns false when queue is not full
       self.assertFalse(queue1.is_full())
       queue1.enqueue(17)
       queue1.enqueue(25)
       queue1.enqueue('b')
       # tests if is_empty returns false when queue is full
       self.assertFalse(queue1.is_empty())
       # test if is_full returns true when list is full
       self.assertTrue(queue1.is_full())
       # tests that error is raised when enqueue is called on a full queue
       with self.assertRaises(IndexError):
           queue1.enqueue(9)
       # tests dequeue
       queue1.dequeue()
       queue1.dequeue()
       # test num_in_queue
       self.assertEqual(queue1.num_in_queue(), 3)
       queue1.dequeue()
       queue1.dequeue()
       queue1.dequeue()
       # tests if is_full returns false when queue is empty
       self.assertFalse(queue1.is_full())
       # tests if is_empty returns true when queue is empty
       self.assertTrue(queue1.is_empty())
       # tests that error is raised when dequeue is called on an empty queue
       with self.assertRaises(IndexError):
            queue1.dequeue()
       # tests num_in_queue works with empty queue
       self.assertEqual(queue1.num_in_queue(), 0)


if __name__ == "__main__":
   unittest.main()
