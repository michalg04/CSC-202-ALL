# Name: Michal Golovanevsky
# Section: 7
#Lab3

#QueueArray represents a queue of items
#capacity is a number
#queue is a list of items
#num_queue is a number
#front is a number
#rear is a number

class QueueArray:
    """Implements an efficient first-in first-out Abstract Data Type using a Python List"""
    def __init__(self, capacity):
        # the maximum number of items that can be stored in queue
        self.capacity = capacity
        # the number of items in queue
        self.num_queue = 0
        #the list of items in the queue
        self.queue = [None] * capacity
        #the index of the front of the queue
        self.front = 0
        #the index of the rear of the queue
        self.rear = 0

    # boiler plate
    def __repr__(self):
        return "A queue array with capacity {} with {} items in it, " \
                "and with {} number of items currently. " \
               "The queue's front item is indexed at {}, " \
                "and its last is at {}" \
            .format(self.capacity, self.queue, self.num_queue, self.front, self.rear)

    # QueueArray => boolean
    def is_empty(self):
        """Returns true if the queue is empty and false otherwise"""
        return self.num_queue == 0

    # QueueArray => boolean
    def is_full(self):
        """Returns true if the queue is full and false otherwise"""
        return self.num_queue == self.capacity

    # QueueArray item =>
    def enqueue(self, item):
        """adds a new item to the rear of the queue and returns nothing"""
        # checks if queue is full
        if self.is_full():
            #raise an index error
            raise IndexError('Queue is full')
        #put the item in the queue
        self.queue[self.rear] = item
        #increase the index of rear by 1
        self.rear = (self.rear + 1)% self.capacity
        #increase the number of items in the queue by 1
        self.num_queue +=1

    # QueueArray => item
    def dequeue(self):
        """removes the front item from the queue and returns the item"""
        # checks if queue is empty
        if self.is_empty():
            #raises an index error
            raise IndexError('Queue is empty')
        #saves the item in the front
        front_item = self.queue[self.front]
        #deletes the front item
        self.queue[self.front] = None
        #decrements the number of items in the queue
        self.num_queue -=1
        # increase the index of front by 1
        self.front = (self.front + 1)% self.capacity
        #returns the original front item
        return front_item

    # QueueArray => int
    def num_in_queue(self):
        """returns the number of items in the queue"""
        return self.num_queue

class Node:
    def __init__(self, value, next):
        """Creates a node with an initial data value and a reference to the next node"""
        self.value = value
        self.next = next

    # boiler plate
    def __repr__(self):
        return "A node with an initial value {} " \
            .format(self.value)

    def __eq__(self, other):
        return (type(other) == Node) \
                and self.value == other.value

    def get_data(self):
        """returns the node data"""
        return self.value

    def get_next(self):
        """returns the next node"""
        return self.next

    def set_data(self, new_data):
        """allocates the data in the node into a new node"""
        self.value = new_data

    def set_next(self, new_next):
        """allocates the data in the next node into a new next node"""
        self.next = new_next


#QueueLinked represents a queue of items
#capacity is a number
#items is a list of items
#num_queue is a number
#front is a node
#rear is a node

class QueueLinked:
    """Implements an efficient first-in first-out Abstract Data Type using a simple linked data structure"""
    def __init__(self, capacity):
        #the maximum number of items that can be stored in queue
        self.capacity = capacity
        # the number of items in queue
        self.num_queue = 0
        # the index of the front of the queue
        self.front = None
        # the index of the rear of the queue
        self.rear = None
        # the list of items in the queue
        self.queue = Node(None, None)

    # boiler plate
    def __repr__(self):
        return "A queue linked with capacity {} with {} items in it, " \
                "and with {} number of items currently. " \
            .format(self.capacity, self.queue, self.num_queue)

    # QueueLinked => boolean
    def is_empty(self):
        """Returns true if the queue is empty and false otherwise"""
        return self.num_queue == 0

    # QueueLinked => boolean
    def is_full(self):
        """Returns true if the queue is full and false otherwise"""
        return self.num_queue == self.capacity

    # QueueLinked item =>
    def enqueue(self, item):
        """adds a new item to the rear of the queue and returns nothing"""
        # checks if queue is full
        if self.is_full():
            # raises an index error if enqueue is called on a full queue
            raise IndexError('Queue is full')
        # allocates a new node
        new_node = Node(item, self.queue.get_next())
        #increases rear value
        self.rear = new_node
        # adds a new item to the queue
        self.queue.set_next(new_node)
        # increases the number of items
        self.num_queue +=1
        #checks if the front node is empty
        if self.front is None:
            #update front
            self.front = new_node

    # QueueLinked => item
    def dequeue(self):
        """removes the front item from the queue and returns the item"""
        # checks if queue is empty
        if self.is_empty():
            #raises an index error
            raise IndexError('Queue is empty')
        #saves the next node in the queue
        current = self.queue.get_next()
        #sets the previous node to None
        previous = None
        #loops in the nodes to get to the last node
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        #ensures that the node after the previous is set to None
        if previous is not None:
            previous.set_next(None)
        else:
            #removes the rear
            self.rear = None
            #sets the next node to None
            self.queue.set_next(None)
        #decreases the number of items in teh queue
        self.num_queue -=1
        #sets the front node to equal the previous
        self.front = previous
        #returns the item in the current node
        return current.get_data()

    # QueueLinked => int
    def num_in_queue(self):
        """returns the number of items in the queue"""
        return self.num_queue