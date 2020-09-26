#Name: Michal Golovanevsky
#Lab5
#Section 7


class TreeNode:
    """Tree node: left and right child + key which can be any object"""
    def __init__(self, key):
        self.key = key #key is any object value in the node
        self.left = None #left is the left node
        self.right = None #right is the right node
        self.parent = None #parent is the parent node

    #Takes a key and inserts the key into the correct position
    #TreeNode object(typically int) =>
    def insert(self, key):
        """inserts a node with key into the correct position if not a duplicate"""
        #checks if key exists
        if self.key:
            #checks if the given key is less than the current node's key
            if key < self.key:
                #checks if node doesn't have a left child
                if self.left is None:
                    #creates a treenode with the key value
                    temp = TreeNode(key)
                    #sets the left child to the temp
                    self.left = temp
                    #sets the parent node to point to the current node
                    temp.parent = self
                #checks if node doesn't have a right child
                else:
                    #recursively calls function insert with the given key
                    self.left.insert(key)
            # checks if the given key is greater than the current node's key
            elif key > self.key:
                #checks if node doesn't have a right child
                if self.right is None:
                    # creates a treenode with the key value
                    temp = TreeNode(key)
                    # sets the right child to the temp
                    self.right = temp
                    # sets the parent node to point to the current node
                    temp.parent = self
                # checks if node doesn't have a left child
                else:
                    # recursively calls function insert with the given key
                    self.right.insert(key)
        # checks if key doesn't exists
        else:
            #sets the root to have the key
            self.key = key

    # returns the node successor of the node
    # TreeNode => TreeNode
    def find_successor(self):
        """returns the node that is the inorder successor of the node"""
        #checks if the right child exists
        if self.right:
            #finds the min value of the tree and returns it
            return self.right.find_min_helper()
        #if there is no right child and there exists a parent
        elif self.parent:
            #if the left child is the node itself
            if self.parent.left == self:
                #return the parent
                return self.parent
            # self.parent.right == self:
            else:
                #returns the grandparent
                return self.parent.parent
        #if the right child doesn't exist
        else:
            return None
    #returns the node with the smallest value
    #TreeNode => TreeNode
    def find_min_helper(self):
        """ returns min node in the tree"""
        #checks if there is no left child
        if self.left is None:
            #returns the current node
            return self
        #if there is a left child
        else:
            #recursively calls the function
            return self.left.find_min_helper()

    # returns the smallest value in tree
    # TreeNode => object
    def find_min(self):
        """ returns min value in the tree"""
        # checks if there is no left child
        if self.left is None:
            #returns the value in the node
            return self.key
        # recursively calls the function if there is a left child
        else:
            return self.left.find_min()

    # returns the largest value in tree
    # TreeNode => object
    def find_max(self):
        """ returns max value in the tree"""
        # checks if there is no right child
        if self.right is None:
            # returns the value in the node
            return self.key
        # recursively calls the function if there is a right child
        else:
            return self.right.find_max()

    #no return value
    #TreeNode =>
    def inorder_print_tree(self):
        """print inorder the subtree of self"""
        #checks if the left child exists
        if self.left is not None:
            # recursively calls the function
            self.left.inorder_print_tree()
        #prints the value in the node
        print(self.key)
        # checks if the right child exists
        if self.right is not None:
            # recursively calls the function
            self.right.inorder_print_tree()

    #no return value
    #TreeNode int =>
    def print_levels_helper(self, level, list_pairs):
        """inorder traversal prints list of pairs, [key, level of the node] where root is level 0"""
        #checks that left child exists
        if self.left is not None:
            #recursively calls the function through the left child
            self.left.print_levels_helper(level + 1, list_pairs)
        list_pairs.append((self.key, level))
        if self.right is not None:
            # recursively calls the function through the right child
            self.right.print_levels_helper(level + 1, list_pairs)

    #no return value
    #TreeNode =>
    def print_levels(self):
        #initializes a list
        list_pairs = []
        # calls on helper function
        self.print_levels_helper(0, list_pairs)
        #prints the list
        print(list_pairs)

class BinarySearchTree:
    """ binary search tree class with a root that can be any object"""
    def __init__(self):
        self.root = None #root is any object that is the head of the tree

    #returns true or false
    #BinarySearchTree value => boolean
    def find(self, key):
        """returns True if key is in a node of the tree, else False"""
        # current node
        temp = self.root
        #loops until the current node is None and until the node's key matches the given key
        while temp is not None and temp.key != key:
            #checks if the given key is smaller than the node's key
            if key < temp.key:
                #sets the current node to its left child
                temp = temp.left
            # checks if the given key is larger than the node's key
            else:
                #sets the current node to its right child
                temp = temp.right
        #checks if the node is empty
        if temp is None:
            #return False because no key was found
            return False
        else:
            #returns True since the key was found
            return True

    #returns node which contains the key
    #BinarySearchTree object => TreeNode or None
    def find_helper(self, key):
        """returns the node of the key if key is found, else returns None"""
        temp = self.root  # current node
        # loops until the current node is None and until the node's key matches the given key
        while temp is not None and temp.key != key:
            if key < temp.key:
                temp = temp.left
            else:
                temp = temp.right
        # checks if the node is empty
        if temp is None:
            #returns None since Node wasn't found
            return None
        else:
            #returns node since it has the key which we were looking for
            return temp

    # Takes a new key and inserts the key into the correct position in tree
    # TreeNode object(typically int) =>
    def insert(self, newkey):
        # if tree is empty
        if self.is_empty():
            #set the root to a new treenode with the new key
            self.root = TreeNode(newkey)
            return
        else:
            #set a temp to the root
            temp = self.root
            #checks if the node key is greater than the new key
            if temp.key > newkey:
                #checks if there no left child
                if temp.left is None:
                    #sets a new treenode with the key
                    node = TreeNode(newkey)
                    #assigns the left child to the new node
                    temp.left = node
                    #assigns the parent of the node to the current node
                    node.parent = temp
                else:
                    #recursively calls the function if there is a left child
                    temp.left.insert(newkey)
            else:
                #checks if there is no right child
                if temp.right is None:
                    # sets a new treenode with the key
                    node = TreeNode(newkey)
                    # assigns the right child to the new node
                    temp.right = node
                    # assigns the parent of the node to the current node
                    node.parent = temp
                else:
                    # recursively calls the function if there is a right child
                    temp.right.insert(newkey)

    #no return value
    #BinarySearchTree object =>
    def delete(self, key):
        """ deletes the node containing key, assumes such a node exists"""
        #finds the node containing the key
        del_node = self.find_helper(key)
        #calls on the delete helper function with the node
        self.delete_helper(del_node)

    # no return value
    # BinarySearchTree TreeNode =>
    def delete_helper(self, del_node):
        """ deletes the node containing key, assumes such a node exists"""
        #case 1: node has no children
        if (del_node.right is None) and (del_node.left is None):
            #if parent exists
            if del_node.parent:
                #if the node we want to delete is the right child
                if del_node == del_node.parent.right:
                    #set the pointer for the right child to None
                    del_node.parent.right = None
                else:
                    #set the pointer for the left child to None
                    del_node.parent.left = None
            #node is the root
            else:
                #sets the root to None
                self.root = None
        #case 2: if the node has 1 child
        elif del_node.right is None or del_node.left is None:
            #if right child exists
            if del_node.right:
                #saves the right child
                child = del_node.right
            else:
                #saves the left child
                child = del_node.left
            #if there exsits a parent
            if del_node.parent:
                #if the node we want to delete is the right child
                if del_node == del_node.parent.right:
                    #set the node to be the right child
                    del_node.parent.right = child
                else:
                    # set the node to be the left child
                    del_node.parent.left = child
            else:
                #sets the root to be equal the currect child
                self.root = child
        #case 3: if the node has 2 children
        else:
            successor = del_node.find_successor()
            del_node.key = successor.key
            #delete_helper can be called only with case 1 or 2
            self.delete_helper(successor)

    # print inorder the entire tree
    #BST =>
    def print_tree(self):
        #calls on the node function that prints inorder using the root
        self.root.inorder_print_tree()

    # returns True if tree is empty, else False
    #BST => boolean
    def is_empty(self):
        #if the root is empty there is no tree
        return self.root is None


