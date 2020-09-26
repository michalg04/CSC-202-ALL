#Name: Michal Golovanevsky
#Section: 7
#test cases for project 3

import unittest
import filecmp
from huffman import *

class TestList(unittest.TestCase):
   def test_cnt_freq(self):
      freqlist	= cnt_freq("file1.txt")
      anslist = [0]*256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0] 
      self.assertListEqual(freqlist[97:104], anslist[97:104])
      #tests empty file
      freqlist = cnt_freq("emptyfile.txt")
      anslist = [0] * 256
      self.assertListEqual(freqlist, anslist)
      #tests file with one char
      freqlist = cnt_freq("onechar.txt")
      anslist = [0] * 256
      anslist[103] = [1]
      self.assertListEqual(freqlist[100:103], anslist[100:103])

   def test_create_huff_tree(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      numchars = 32
      charforroot = "a"
      self.assertEqual(hufftree.freq, 32)
      self.assertEqual(hufftree.char, 97)
      left = hufftree.left
      self.assertEqual(left.freq, 16)
      self.assertEqual(left.char, 97)
      right = hufftree.right
      self.assertEqual(right.freq, 16)
      self.assertEqual(right.char, 100)
      #test if file is empty
      freqlist = cnt_freq("emptyfile.txt")
      hufftree = create_huff_tree(freqlist)
      self.assertEqual(hufftree, None)
      #test file with one char
      freqlist = cnt_freq("onechar.txt")
      hufftree = create_huff_tree(freqlist)
      self.assertEqual(hufftree.freq, 1)
      self.assertEqual(hufftree.char, 103)
      left = hufftree.left
      self.assertEqual(left, None)
      right = hufftree.right
      self.assertEqual(right, None)

   def test_create_code(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('d')], '1')
      self.assertEqual(codes[ord('a')], '0000')
      self.assertEqual(codes[ord('f')], '0001')
      #test empty file
      freqlist = cnt_freq("emptyfile.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      anscodes = [''] * 256
      self.assertEqual(codes, anscodes)
      #test file with one char
      freqlist = cnt_freq("onechar.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('g')], '')

   def test_01_encodefile(self):
      huffman_encode("file1.txt", "output1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("output1.txt", "output1_soln.txt"))


   def test_01_decodefile(self):
      freqlist = cnt_freq("file1.txt")
      huffman_decode(freqlist,"output1.txt", "decodefile1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodefile1.txt", "file1.txt"))


   def test_tree_preord(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      self.assertEqual(tree_preord(hufftree), '00001a1f1b1c1d')
      #tests empty file
      freqlist = cnt_freq("emptyfile.txt")
      hufftree = create_huff_tree(freqlist)
      self.assertEqual(tree_preord(hufftree), '')
      #tests one char file
      freqlist = cnt_freq("onechar.txt")
      hufftree = create_huff_tree(freqlist)
      self.assertEqual(tree_preord(hufftree), '1g')


if __name__ == '__main__': 
   unittest.main()
