#Test Cases for Lab8
#Name: Michal Golovanevsky
#Section: 7

from sep_chain_ht import *

import unittest

class TestCase(unittest.TestCase):
    def test_insert(self):
        hashtable = MyHashTable()
        hashtable.insert(16, 'cat')
        hashtable.insert(10, 'dog')
        hashtable.insert(97, 'pig')
        self.assertEqual(hashtable.collisions(), 0)
        self.assertEqual(hashtable.get(10), (10, 'dog'))
        self.assertEqual(hashtable.size(), 3)
        self.assertAlmostEqual(hashtable.load_factor(), 0.2727272727272727)
        hashtable.insert(27, 'bird')
        self.assertEqual(hashtable.collisions(), 1)
        #test duplicate key
        hashtable.insert(97, 'bird')
        self.assertEqual(hashtable.get(97), (97, 'bird'))


    def test_get(self):
        hashtable = MyHashTable()
        hashtable.insert(16, 'cat')
        hashtable.insert(10, 'dog')
        hashtable.insert(97, 'pig')
        self.assertEqual(hashtable.get(10), (10, 'dog'))
        self.assertEqual(hashtable.get(16), (16, 'cat'))
        self.assertEqual(hashtable.get(97), (97, 'pig'))
        hashtable.insert(35, 'lizard')
        hashtable.insert(1000, 'snake')
        self.assertEqual(hashtable.get(35), (35, 'lizard'))
        self.assertEqual(hashtable.get(1000), (1000, 'snake'))
        #checks a key that doesn't exist
        with self.assertRaises(LookupError):
            hashtable.get(45)

    def test_remove(self):
        hashtable = MyHashTable()
        hashtable.insert(16, 'cat')
        hashtable.insert(10, 'dog')
        hashtable.insert(97, 'pig')
        self.assertEqual(hashtable.size(), 3)
        self.assertEqual(hashtable.remove(10), (10, 'dog'))
        self.assertEqual(hashtable.size(), 2)
        # checks that the deleted item doesn't exist
        with self.assertRaises(LookupError):
            hashtable.get(10)
        #checks remove with a key that doesn't exist
        with self.assertRaises(LookupError):
            hashtable.get(85)
        self.assertEqual(hashtable.remove(16), (16, 'cat'))
        self.assertEqual(hashtable.size(), 1)
        self.assertEqual(hashtable.remove(97), (97, 'pig'))
        self.assertEqual(hashtable.size(), 0)

    def test_size(self):
        hashtable = MyHashTable()
        hashtable.insert(16, 'cat')
        hashtable.insert(10, 'dog')
        hashtable.insert(97, 'pig')
        self.assertEqual(hashtable.size(), 3)
        self.assertEqual(hashtable.remove(16), (16, 'cat'))
        self.assertEqual(hashtable.size(), 2)
        self.assertEqual(hashtable.remove(97), (97, 'pig'))
        self.assertEqual(hashtable.size(), 1)
        hashtable.insert(35, 'lizard')
        hashtable.insert(1000, 'snake')
        self.assertEqual(hashtable.size(), 3)

    def test_load_factor(self):
        hashtable = MyHashTable()
        hashtable.insert(16, 'cat')
        hashtable.insert(10, 'dog')
        hashtable.insert(97, 'pig')
        self.assertAlmostEqual(hashtable.load_factor(), 0.2727272727272727)
        self.assertEqual(hashtable.remove(16), (16, 'cat'))
        self.assertAlmostEqual(hashtable.load_factor(), 0.1818181818181818)
        self.assertEqual(hashtable.remove(97), (97, 'pig'))
        self.assertAlmostEqual(hashtable.load_factor(), 0.0909090909090909)
        self.assertEqual(hashtable.remove(10), (10, 'dog'))
        self.assertAlmostEqual(hashtable.load_factor(), 0.0)
        #tests with smaller hash table
        hashtable1 = MyHashTable(3)
        hashtable1.insert(16, 'cat')
        hashtable1.insert(10, 'dog')
        hashtable1.insert(97, 'pig')
        self.assertAlmostEqual(hashtable1.load_factor(), 1.0)
        self.assertEqual(hashtable1.remove(16), (16, 'cat'))
        self.assertAlmostEqual(hashtable1.load_factor(), 0.666666666666667)
        self.assertEqual(hashtable1.remove(97), (97, 'pig'))
        self.assertAlmostEqual(hashtable1.load_factor(), 0.3333333333333333)
        self.assertEqual(hashtable1.remove(10), (10, 'dog'))
        self.assertAlmostEqual(hashtable1.load_factor(), 0.0)
        hashtable1.insert(100, 'bird')
        hashtable1.insert(16, 'cat')
        hashtable1.insert(10, 'dog')
        hashtable1.insert(97, 'pig')
        self.assertAlmostEqual(hashtable1.load_factor(), 1.3333333333333333)
        # tests with larger hash table
        hashtable2 = MyHashTable(30)
        hashtable2.insert(16, 'cat')
        hashtable2.insert(10, 'dog')
        hashtable2.insert(97, 'pig')
        self.assertAlmostEqual(hashtable2.load_factor(), 0.1)
        self.assertEqual(hashtable2.remove(16), (16, 'cat'))
        self.assertAlmostEqual(hashtable2.load_factor(), 0.0666666666666667)
        self.assertEqual(hashtable2.remove(97), (97, 'pig'))
        self.assertAlmostEqual(hashtable2.load_factor(), 0.03333333333333333)
        self.assertEqual(hashtable2.remove(10), (10, 'dog'))
        self.assertAlmostEqual(hashtable2.load_factor(), 0.0)
        #tests rehashing
        hashtable1 = MyHashTable(3)
        hashtable1.insert(100, 'bird')
        hashtable1.insert(16, 'cat')
        hashtable1.insert(10, 'dog')
        hashtable1.insert(97, 'pig')
        hashtable1.insert(60, 'snake')
        self.assertAlmostEqual(hashtable1.load_factor(), 5/7)


    def test_collisions(self):
        hashtable = MyHashTable()
        hashtable.insert(16, 'cat')
        hashtable.insert(10, 'dog')
        hashtable.insert(97, 'pig')
        self.assertEqual(hashtable.collisions(), 0)
        hashtable.insert(27, 'bird')
        self.assertEqual(hashtable.collisions(), 1)
        hashtable.insert(9, 'bunny')
        self.assertEqual(hashtable.collisions(), 2)
        #checks to see that the collisions don't decremeant if the item removed didn't collide
        self.assertEqual(hashtable.remove(97), (97, 'pig'))
        self.assertEqual(hashtable.collisions(), 1)
        # checks to see that the collisions decremeant if the item removed collided
        self.assertEqual(hashtable.remove(27), (27, 'bird'))
        self.assertEqual(hashtable.collisions(), 0)



if (__name__ == '__main__'):
    unittest.main()
