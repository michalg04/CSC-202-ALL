#Test Cases for Proejct 1
# Name: Michal Golovanevsky
# Section: 7

import unittest
import stacks

class TestCases(unittest.TestCase):
   def test_stack_array(self):
       # tests the StackArray with basic input
       my_stack = stacks.StackArray(3)
       #test the push function
       my_stack.push(2)
       #checks the size
       self.assertEqual(my_stack.size(), 1)
       my_stack.push(5)
       my_stack.push(19)
       # test the pop function
       my_stack.pop()
       my_stack.push('a')
       # checks to see if is_empty works with full list
       self.assertFalse(my_stack.is_empty())
       # checks to see if is_full works with full list
       self.assertTrue(my_stack.is_full())
       # checks to see if peek works correctly
       self.assertEqual(my_stack.peek(), 'a')
       # checks the size
       self.assertEqual(my_stack.size(), 3)
       my_stack.pop()
       my_stack.pop()
       my_stack.pop()
       # checks to see if is_full works with empty list
       self.assertFalse(my_stack.is_full())
       # checks to see if peek raises an error with empty stack
       with self.assertRaises(IndexError):
           my_stack.peek()
       # checks to see if pop raises an error with empty stack
       with self.assertRaises(IndexError):
           my_stack.pop()
       # checks to see if peek raises an error with empty stack
       with self.assertRaises(IndexError):
           my_stack.peek()
       my_stack.push(9)
       my_stack.push(200)
       my_stack.push(7)
       # checks to see if push raises an error if the stack is full
       with self.assertRaises(IndexError):
           my_stack.push('c')
       # checks the size
       self.assertEqual(my_stack.size(), 3)
       # checks to see if is_empty works with full list
       self.assertFalse(my_stack.is_empty())
       # checks to see if is_full works with full list
       self.assertTrue(my_stack.is_full())
       # checks to see if push raises an error if the stack is full even with None being pushed
       with self.assertRaises(IndexError):
           my_stack.push(None)


   def test_stack_linked(self):
       # tests the StackLink with basic input
       my_stack = stacks.StackLinked(4)
       #test the push function
       my_stack.push(2)
       #checks the size
       self.assertEqual(my_stack.size(), 1)
       my_stack.push(5)
       my_stack.push(19)
       my_stack.push(99)
       # test the pop function
       my_stack.pop()
       my_stack.push('hello')
       # checks to see if is_empty works with full list
       self.assertFalse(my_stack.is_empty())
       # checks to see if is_full works with full list
       self.assertTrue(my_stack.is_full())
       # checks to see if peek works correctly
       self.assertEqual(my_stack.peek(), 'hello')
       # checks the size
       self.assertEqual(my_stack.size(), 4)
       my_stack.pop()
       my_stack.pop()
       my_stack.pop()
       my_stack.pop()
       # checks to see if is_full works with empty list
       self.assertFalse(my_stack.is_full())
       # checks to see if peek raises an error with empty stack
       with self.assertRaises(IndexError):
           my_stack.peek()
       # checks to see if pop raises an error with empty stack
       with self.assertRaises(IndexError):
           my_stack.pop()
       # checks to see if peek raises an error with empty stack
       with self.assertRaises(IndexError):
           my_stack.peek()
       my_stack.push(9)
       my_stack.push(200)
       my_stack.push(7)
       my_stack.push(12)
       # checks to see if push raises an error if the stack is full
       with self.assertRaises(IndexError):
           my_stack.push(9)
       # checks the size
       self.assertEqual(my_stack.size(), 4)
       # checks to see if is_empty works with full list
       self.assertFalse(my_stack.is_empty())
       # checks to see if is_full works with full list
       self.assertTrue(my_stack.is_full())
       # checks to see if push raises an error if the stack is full even with None being pushed
       with self.assertRaises(IndexError):
           my_stack.push(None)


if __name__ == "__main__":
   unittest.main()
