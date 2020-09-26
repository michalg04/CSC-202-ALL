#Name: Michal Golovanevsky
#Section: 7


class HuffmanNode:
    """empty binary tree of HuffmanNodes"""
    def __init__(self, char, freq):
	    self.char = char  # ASCII value of char
	    self.freq = freq #freq is a number
	    self.code = None #code consists of ’0’s and ’1’s
	    self.left = None #left child
	    self.right = None #right child

#HuffmanNode HuffmanNode => boolean
#returns true if tree rooted at node a comes before tree rooted at node b
def comes_before (a, b) :
    #checks which node has the smaller frequency
    if a.freq < b.freq:
        return True
    #checks if the frequencies are equal
    elif a.freq == b.freq:
        #compares ASCII codes
        if a.char < b.char:
            return True
        #if a ASCII is larger
        else:
            return False
    #if a frequency is larger
    else:
        return False

#str => list
#returns the list with the counts of occurrences
def cnt_freq(filename):
    """opens a text file with a given file name
    and counts the frequency of occurrences of all the characters within that file"""
    try:
        #opens the file
        with open(filename, 'r', encoding='utf-8') as file:
            #creates an empty list
            list_line = []
            #creates a list of frequencies
            freq = [0]*256
            #loops line by line
            for line in file:
                #addes to the list of lines
                list_line.extend(list(line))
            #increases the frequencies
            for char in list_line:
                freq[ord(char)] += 1
            return freq
    # if file doesn't exist
    except IOError:
        return 'file does not exists'

#list => node
#returns the smallest node
def findMin(hufftree):
    """finds the smallest node"""
    #initializes the first node as min
    min = hufftree[0]
    #loops through the list of nodes
    for i in hufftree:
        #finds the node that is the smallest
        if comes_before(i, min):
            min = i
    return min

#list => (root) node
#returns the root node of that tree
def create_huff_tree(list_of_freqs):
    """builds a Huffman tree from a given list of the number of occurrences of
    characters returned by cnt_fref()"""
    #creates list of hufftree nodes
    hufftree = []
    #loops inside the list
    for i in range(len(list_of_freqs)):
        #checks that the frequency isn't zero
        if list_of_freqs[i] != 0:
            #creates a new node
            new_node = HuffmanNode(i, list_of_freqs[i])
            #adds to the list
            hufftree.append(new_node)
    if len(hufftree) == 0:
        return None
    #loops until there is only one item left in the list
    while len(hufftree) != 1:
        #finds the first min
        min_first = findMin(hufftree)
        #removes is from the list
        hufftree.remove(min_first)
        #finds the second min
        min_sec = findMin(hufftree)
        #removes is from the list
        hufftree.remove(min_sec)
        #first the min character of the two
        c = min(min_first.char, min_sec.char)
        #creates a new node with the min char and the two frequencies
        new_node = HuffmanNode(c, min_first.freq + min_sec.freq)
        #changes the left and right children
        new_node.left = min_first
        new_node.right = min_sec
        #adds the new node to the list
        hufftree.append(new_node)
    #returns the root
    return hufftree[0]

#(root) node => list
#returns a list containting the codes
def create_code(root_node):
    # initializes the list
    codes = [''] * 256
    # calls on a helper function to preorder using the root and the codes
    if root_node is not None:
        preord_helper(root_node, '', codes)
    return codes

#file file =>
#doesn't return, writes to the ouput file
def huffman_encode(in_file, out_file):
    """reads an input text file and writes, using the Huffman code, the encoded text into an output file"""
    #uses functions to create the needed variables
    freq = cnt_freq(in_file)
    hufftree = create_huff_tree(freq)
    codes = create_code(hufftree)
    try:
        #opens the input file
        with open(in_file, 'r', encoding='utf-8') as file1:
            #writes to output file
            with open(out_file, 'w', encoding='utf-8') as file2:
                #creates an empty list
                list_line = []
                #loops through the first file
                for line in file1:
                    #adds to the list
                    list_line.extend(list(line))
                #loops through the list
                for char in list_line:
                    #writes to the second file
                    file2.write(codes[ord(char)])
    #if file doesn't exist
    except IOError:
        return 'file does not exists'

#decodes encoded file, writes it to decode file
#str file file =>
def huffman_decode(freqs, encoded_file, decode_file):
    hufftree = create_huff_tree(freqs)
    try:
        #opens the input file
        with open(encoded_file, 'r', encoding='utf-8') as file1:
            #writes to output file
            with open(decode_file, 'w', encoding='utf-8') as file2:
                #creates an empty list
                list_line = []
                #loops through the first file
                for line in file1:
                    #adds to the list
                    list_line.extend(list(line))
                #loops through the list
                current = hufftree
                for char in list_line:
                    #if char is 0 goes left
                    if char == '0':
                        current = current.left
                        if current.left is None and current.right is None:
                            file2.write(chr(current.char))
                            current = hufftree
                    #if char is 1 goes right
                    elif char == '1':
                        current = current.right
                        if current.left is None and current.right is None:
                            file2.write(chr(current.char))
                            current = hufftree
                    else:
                        raise ValueError('wrong character')

    #if file doesn't exist
    except IOError:
        return 'file does not exists'

#node str list =>
#doesn't return
def preord_helper(node, code, codes):
    """ Traverse the tree from the root to each leaf node and adding a ’0’ when we go
        ’left’ and a ’1’ when we go ’right’ constructing a string of 0’s and 1’s"""
    node.code = code
    #if the node has no children
    if node.left is None and node.right is None:
        #puts the code in the list
        codes[node.char] = code
    #if there is a left child
    if node.left:
        #recursively adds 0 to the code
        preord_helper(node.left, code + '0', codes)
    # if there is a right child
    if node.right:
        # recursively adds 1 to the code
        preord_helper(node.right, code + '1', codes)

#takes a Huffman tree and produces the tree description
#hufftree str => str
def tree_preorder_helper(node, str):
    #if the node is empty returns the str
    if node is None:
        return str
    #checks if no children
    if node.right is None and node.left is None:
        str += '1' + chr(node.char)
    else:
        #adds 0 if there are children
        str += '0'
        #recursively calls the function wiht the correct child
        if node.left:
            str = tree_preorder_helper(node.left, str)
        if node.right:
            str = tree_preorder_helper(node.right, str)
    return str

#hufftree => str
def tree_preord(root_node):
    #rcalls the helper function with the given root and an empty string
    return tree_preorder_helper(root_node, '')



