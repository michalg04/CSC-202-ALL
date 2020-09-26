# Michal Golovanevsky
# Project 4
# section 7

import string

class HashTableLinPr:
    def __init__(self, size=251):
        """creates and initializes the hash table size to size"""
        # python list representing the hash table
        self.hash_table = [('', []) for _ in range(size)]
        # the size of the table (int)
        self.table_size = size
        # the number of pairs in the hash table (int)
        self.num_items = 0

    # HashTableLinPr file =>
    # read words from a stop words file and insert them into hash table
    def read_stop(self, filename):
        try:
            # opens the file
            with open(filename, 'r', encoding='utf-8') as file:
                # loops line by line
                for line in file:
                    words = line.split()
                    # inserts the words
                    self.insert(words[0], [])
        # if file doesn't exist
        except IOError:
            return 'file does not exists'

    # HashTableLinPr item =>
    # checks if the item is a number
    def is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    # HashTableLinPr file hashtable =>
    # read words from input file and insert them into hash table
    def read_file(self, filename, stop_table):
        try:
            # opens the file
            with open(filename, 'r', encoding='utf-8') as file:
                # counts lines
                counter = 0
                # loops line by line
                for line in file:
                    counter += 1
                    line = line.lower()
                    # gets rid of puncuation
                    for c in string.punctuation:
                        if c != "'":
                            line = line.replace(c, ' ')
                        else:
                            line = line.replace(c, '')
                    # splits the words
                    words = line.split()
                    for word in words:
                        # inserts all the words that aren't numbers or stop
                        # words
                        if not self.is_number(word) and not stop_table.find(
                                word):
                            self.insert(word, counter)
        # if file doesn't exist
        except IOError:
            return 'file does not exists'

    # HashTableLinPr int => boolean
    # returns true if the key item pair is in the hash table and false otherwise
    def find(self, key):
        hash_value = self.myhash(key, self.table_size)
        for i in range(self.table_size):
            # saves the key item pair at each index
            (key1, items1) = self.hash_table[(hash_value + i) % self.table_size]
            if key1 == '':
                return False
            if key1 == key:
                return True
        return False

    # HashTableLinPr => int
    # returns the size of the hash table
    def get_tablesize(self):
        return self.table_size

    # HashTableLinPr file =>
    # writes the concordance to the output file
    def save_concordance(self, output_filename):
        h_table = sorted(self.hash_table, key=lambda word: word[0])
        try:
            # writes to the output file
            with open(output_filename, 'w', encoding='utf-8') as file:
                # loops through the table
                for i in range(self.table_size):
                    (key, item) = h_table[i]
                    if key != '':
                        lines = ' '.join(map(str, item))
                        if i < self.table_size - 1:
                            file.write(key + ':' + '\t' + lines + '\n')
                        else:
                            # no new line for the last word
                            file.write(key + ':' + '\t' + lines)
        # if file doesn't exist
        except IOError:
            return 'file does not exists'

    # HashTableLinPr => float
    # returns the load factor of the table
    def get_load_fact(self):
        return (self.num_items / self.table_size)

    # HashTableLinPr int int => int
    # return an integer from 0 to the (size of the hash table) - 1
    def myhash(self, key, table_size):
        """Compute the hash value by h_value(str) = ∑𝑛−1 𝑜𝑟𝑑(𝑠𝑡𝑟[𝑖]) ∗ 31𝑛−1−𝑖
        where n = the minimum of len(key) and 8 (e.g., if len (key) > 8 assume n=8) ,
         i = the index of each character of the key."""
        n = min(8, len(key))
        h_value = 0
        for i in range(n):
            h_value += ord(key[i]) * (31 ** (n - 1 - i))
        return h_value % table_size

    # HashTableLinPr int item =>
    # inserts the key-item pair into the hash table
    def insert(self, key, item):
        # creates the load factor
        load_factor = (self.num_items + 1) / self.table_size
        if load_factor > 0.75:
            # rehashes the table
            self.rehash()
        # calls the helper function
        self.insert_helper(key, item)

    # HashTableLinPr int item =>
    # inserts the key-item pair into the hash table
    def insert_helper(self, key, items):
        # creates the hash value
        hash_value = self.myhash(key, self.table_size)
        # print(hash_value)
        for i in range(self.table_size):
            index = (hash_value + i) % self.table_size
            (key1, items1) = self.hash_table[index]
            if key1 == '':
                if items != []:
                    items1.append(items)
                self.hash_table[index] = (key, items1)
                # increases the number of elements
                self.num_items += 1
                return
            if key1 == key:
                if items != []:
                    items1.append(items)
                    # increases the number of elements
                    self.num_items += 1
                    return
        raise ValueError('insert failed ' + key)

    # HashTableLinPr =>
    # rehashes the function
    def rehash(self):
        # creates a new table
        self.table_size = (self.table_size * 2) + 1
        old_hash_table = self.hash_table
        self.hash_table = [('', []) for _ in range(self.table_size)]
        # resets the init variables
        self.num_items = 0
        # loops through the old hash table
        for (key, items) in old_hash_table:
            if key != '':
                # inserts the items into the new table
                self.insert_helper(key, items)
