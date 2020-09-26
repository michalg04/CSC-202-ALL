#Michal Golovanevsky
#lab 8
#section 7

class MyHashTable:
    """ hashtable that supports separate chaining collision resolution"""
    def __init__(self, table_size=11):
        # python list representing the hash table
        self.hash_table = [[] for _ in range(table_size)]
        #the size of the table (int)
        self.table_size = table_size
        #the number of pairs in the hash table (int)
        self.num_items = 0
        #number of collisions (int)
        self.num_collisions = 0

    # boiler plate
    def __repr__(self):
        return "hashtable with table size {}, containts {} elements and collided {} times" \
            .format(self.table_size, self.num_items(), self.num_collisions)

    def __eq__(self, other):
        return self.num_items == other.num_items and \
                self.num_collisions == other.num_collisions and \
                self.table_size == other.table_size and \
                self.hash_table[:] == other.hash_table[:]

    # MyHashTable int item =>
    # inserts the key-item pair into the hash table
    def insert(self, key, item):
        #creates the load factor
        load_factor = (self.num_items + 1) / self.table_size
        if load_factor > 1.5:
            #rehashes the table
            self.rehash()
        #calls the helper function
        self.insert_helper(key, item)

    # MyHashTable int item =>
    # inserts the key-item pair into the hash table
    def insert_helper(self, key, item):
        #creates the hash value
        hash_value = key % self.table_size
        #creates a bucket that contains elements of the same hash value
        bucket = self.hash_table[hash_value]
        #checks that the bucket is not empty
        if len(bucket) != 0:
            #increases the number of collisions
            self.num_collisions += 1
            #removes the key
            self.remove_helper(key)
        #adds the item to the bottom of the bucket
        bucket.append((key, item))
        #increases the number of elements
        self.num_items += 1

    # MyHashTable =>
    # need to set the collisons to zero and then recount them with the new table
    def rehash(self):
        #creates a new table
        self.table_size = (self.table_size * 2) + 1
        old_hash_table = self.hash_table
        self.hash_table = [[] for _ in range(self.table_size)]
        #resets the init variables
        self.num_collisions = 0
        self.num_items = 0
        #loops through the old hash table
        for items in old_hash_table:
            if len(items) != 0:
                for (key, item) in items:
                    #inserts the items into the new table
                    self.insert_helper(key, item)


    # MyHashTable int => touple
    # takes a key and returns the item (key, item) pair associated with the key
    # If no key-item pair is associated with the key, the function raises a LookupError exception
    def get(self, key):
        hash_value = key % self.table_size
        bucket = self.hash_table[hash_value]
        #checks that the bucket is not empty
        if len(bucket) != 0:
            #loops through the pairs in the bucket
            for (key1, item1) in bucket:
                #checks if the key matches one from the bucket
                if key1 == key:
                    return (key1, item1)
        #else
        raise LookupError('no key-item pair is associated with ' + str(key))

    # MyHashTable int => touple
    # removes the key-item pair from the hash table and returns the key-item pair
    def remove_helper(self, key):
        hash_value = key % self.table_size
        bucket = self.hash_table[hash_value]
        if len(bucket) != 0:
            #loops through the pairs in the bucket
            for (key1, item1) in bucket:
                #finds the matching key
                if key1 == key:
                    #decrements the number of items
                    self.num_items -= 1
                    if len(bucket) > 1:
                        #decremeants the collision if the item collided
                        self.num_collisions -= 1
                    #calls the remove function
                    bucket.remove((key1, item1))
                    return (key1, item1)
        #pair not found
        return (None, None)


    # MyHashTable int => touple
    # removes the key-item pair from the hash table and returns the key-item pair
    def remove(self, key):
        #calls helper function
        (key, item) = self.remove_helper(key)
        #if the key is not found raise error
        if (key, item) == (None, None):
            raise LookupError('no key-item pair is associated with ' + str(key))
        return (key, item)


    #MyHashTable => int
    #returns the number of key-item pairs currently stored in the hash table
    def size(self):
        return self.num_items

    #MyHashTable => float
    #returns the current load factor of the hash table
    def load_factor(self):
        return (self.num_items / self.table_size)

    #MyHashTable =>
    #returns the number of collisions that have occurred during insertions into the hash table
    def collisions(self):
        return self.num_collisions

