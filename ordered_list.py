#Names: Brittani Kealoha and Michal Golovanevsky
#Lab 3
#Section: 07

# head and tail are nodes
class OrderedList:
    """Implements an ordered list using doubly linked list"""
    def __init__(self):
        """creates a new ordered list that is empty"""
        self.head = None
        self.tail = None

    # boiler plate
    def __repr__(self):
        current = self.head
        s = ""
        while current is not None:
            s += str(current.data)
            s += " "
            current = current.next
        return s

        # searches the list from front to back if data is present returns
        # true else returns false
        # item -> boolean
    def search_forward(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

        # searches the list from back to front if data is present returns
        # true else returns false
        # item -> boolean
    def search_backward(self, item):
        current = self.tail
        while current is not None:
            if current.data == item:
                return True
            current = current.prev
        return False

    #It needs the item and returns nothing
    #item =>
    def add(self, item):
        """adds a new item to the list while preserving the order"""
        current = self.head
        prev = None
        stop = False
        while current is not None and not stop:
            if current.data > item:
                stop = True
            else:
                prev = current
                current = current.next
        temp = Node(item, None, None)
        if prev is not None:
            prev.next = temp
        else:
            self.head = temp
        if current is None:
            self.tail = temp
            temp.prev = prev
        else:
            current.prev = temp
            temp.next = current
            temp.prev = prev

    #Return the position of removed item if it is in the list, otherwise return -1 (as not found)
    #item => int
    def remove(self, item):
        """removes the item from the list"""
        if not self.search_forward(item):
            return -1
        current = self.head
        index_counter = -1
        while current is not None:
            index_counter += 1
            if current.data == item:
                prev_node = current.prev
                next_node = current.next
                if prev_node is not None:
                    prev_node.next = next_node
                else:
                    self.head = next_node
                if next_node is not None:
                    next_node.prev = prev_node
                else:
                    self.tail = prev_node
                return index_counter
            current = current.next

    # checks if the list is empty
    # no parameters -> boolean
    def is_empty(self):
        return self.head is None and self.tail is None

    # finds the size of the list
    # no parameter -> int
    def size(self):
        counter = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next
        return counter

    # returns the index of a certain item in the list
    # item -> int
    def index(self, item):
        counter = 0
        current = self.head
        while current is not None:
            if current.data == item:
                return counter
            counter += 1
            current = current.next
        return -1

    # removes and returns the item at position pos.
    # It needs the position and returns the item. If it is not in the item it returns -1 (as not found)
    # int => item or -1
    def pop(self, pos = None):
        """removes and returns the last item in the list"""
        if self.is_empty():
            return -1
        size = self.size()
        if pos is None:
            pos = size - 1
        if pos > (size - 1):
            return -1
        if pos <= (size / 2):
            current = self.head
            index_counter = -1
            while current is not None:
                index_counter += 1
                if index_counter == pos:
                    temp = current.data
                    prev_node = current.prev
                    next_node = current.next
                    if prev_node is not None:
                        prev_node.next = next_node
                    else:
                        self.head = next_node
                    if next_node is not None:
                        next_node.prev = prev_node
                    else:
                        self.tail = prev_node
                    return temp
                current = current.next
        else:
            current = self.tail
            index_counter = self.size()
            while current is not None:
                index_counter -= 1
                if index_counter == pos:
                    temp = current.data
                    prev_node = current.prev
                    next_node = current.next
                    if prev_node is not None:
                        prev_node.next = next_node
                    else:
                        self.head = next_node
                    if next_node is not None:
                        next_node.prev = prev_node
                    else:
                        self.tail = prev_node
                    return temp
                current = current.prev

class Node:
    def __init__(self, data, next, prev):
        """Creates a node with an initial data data and a reference to the next node"""
        self.data = data
        self.next = next
        self.prev = prev