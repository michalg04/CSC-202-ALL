#Michal Golovanevsky
#lab 7
#section 7


class MaxHeap:
    """a max heap that contains integers that represent both the priority and name of the object"""
    def __init__(self, capacity=50):
        # a number (int), the max number of elements allowed
        self.capacity = capacity
        # list containting items
        self.items = [0]* (self.capacity + 1)
        #current number of items
        self.num = 0

    #boiler plate
    def __repr__(self):
        return "heap containts {} and capacity {}"\
            .format(self.heap_contents(), self.capacity - 1)

    def __eq__(self, other):
        return self.capacity == other.capacity and \
               self.num == other.num and \
               self.items[:] == other.items[:]

    #MaxHeap int =>
    #moves the element down to its proper place in the heap while rearranging elements
    def perc_down(self, i):
        #checks that index is greater than current num
        if i > self.num:
            return
        else:
            #left child
            left = i*2
            #right child
            right = i*2 + 1
            largest = i
            #if the left child is less than the number of items and the items of it are larger than the largest
            if (left <= self.num and self.items[left] > self.items[largest]):
                largest = left
            # if the right child is less than the number of items and the
            # items of it are larger than the largest
            if (right <= self.num and self.items[right] > self.items[largest]):
                largest = right
            #if the largest is not the index
            if (largest != i):
                #swap largest and the item at index i
                temp = self.items[i]
                self.items[i] = self.items[largest]
                self.items[largest] = temp
                #recursively perculate down with the largest
                self.perc_down(largest)

    # MaxHeap int =>
    # moves the element up to its proper place in the heap while rearranging elements
    def perc_up(self, i):
        # checks that index is greater than current num
        if i > self.num:
            return
        else:
            parent = i//2
            #if parent index is greater than 0 and the parent value is less than the index value
            if parent > 0 and self.items[parent] < self.items[i]:
                #swap parent with current
                temp = self.items[i]
                self.items[i] = self.items[parent]
                self.items[parent] = temp
                #recursively purculate up
                self.perc_up(parent)


    #inserts “item” into the heap, returns true if successful, false if there is no room in the heap
    #MaxHeap item => boolean
    def insert(self, item):
        #checks that there's room
        if (self.num + 1) <= self.capacity:
            #increases the number of items
            self.num += 1
            #assigns the new item
            self.items[self.num] = item
            #perculates it to the right place
            self.perc_up(self.num)
            return True
        else:
            return False

    #returns max without changing the heap and return None if not found
    #MaxHeap => value
    def find_max(self):
        #checks if empty
        if self.num == 0:
            return None
        else:
            #returns the max
            return self.items[1]

    #returns a list of contents of the heap in the order it is stored internal to the heap
    #MaxHeap => list
    def heap_contents(self):
        return self.items[1: self.num + 1]

    #return True if the build was successful and False if the capacity of the MaxHeap object is not large enough
    #MaxHeap list => boolean
    def build_heap(self, alist):
        #checks if empty
        if alist == []:
            return False
        #checks not large enough
        if len(alist) > self.capacity:
            return False
        # height of tree
        i = len(alist) // 2
        #current size
        self.num = len(alist)
        #loops thourhg the list
        for k in range(len(alist)):
            self.items[k + 1] = alist[k]
        #perculates down
        while (i > 0):
            self.perc_down(i)
            #decrements the index
            i -= 1
        return True

    # returns max and removes it from the heap and restores the heap property
    # return None if heap is empty
    # MaxHeap => value
    def del_max(self):
        #checks if no items
        if self.num < 1:
            return None
        #saves max
        res = self.items[1]
        #swtiches max with last item
        self.items[1] = self.items[self.num]
        #decrements the number of items
        self.num -= 1
        #perculates it to the right place
        self.perc_down(1)
        return res

    #HeapMax => boolean
    #returns True if the heap is empty, false otherwise
    def is_empty(self):
        return self.num == 0

    #HeapMax => boolean
    #returns True if the heap is full, false otherwise
    def is_full(self):
        return self.num == self.capacity

    #HeapMax => int
    # max number of a entries the heap can hold
    def get_heap_cap(self):
        return self.capacity

    #HeapMax => int
    #the actual number of elements in the heap, not the capacity
    def get_heap_size(self):
        return self.num

    #MaxHeap list => list
    #returns a list containing the integers in nondecreasing order using the Heap Sort algorithm
    def heap_sort_increase(self, alist):
        #builds heap
        self.build_heap(alist)
        #saves original number of items
        nums = self.num
        #loops wihle the number of items is not zero
        while self.num > 0:
            #gets the max item using del_max
            max = self.del_max()
            #puts the max in a new place
            self.items[self.num + 1] = max
        #returns the list in nondecreasing order
        return self.items[1:nums + 1]


