# Name: Michal Golovanevsky
# Section: 7

#orig_string is a string
#string => list
def perm_gen_lex(orig_string):
    """generate all the permutations of the characters in a string and returns them in a lexicographic ordered list"""
    if len(orig_string) == 0: #checks if string is empty
        #returns an empty list
        return []
    elif len(orig_string) == 1: #checks if the string is one letter
        list_str = [orig_string]
        return list_str #returns a list with the letter
    else:
        # initializes a list
        list_str = []
        # goes over all elements of the original string
        for i in range(len(orig_string)):
            # keeps the character
            ch = orig_string[i]
            # construct a string that contains all character in original string except the one at position i
            simpler_string = ""
            for j in range(len(orig_string)):
                if j != i:
                    simpler_string += orig_string[j]
            # gets all permutations of the simpler_string
            perms = perm_gen_lex(simpler_string)
            # adds kth element of original list to the front of each permutation
            for k in range(len(perms)):
                string = perms[k]
                string = ch + string
                list_str.append(string) #adds the new string to the list
        #returns the final list with all the permutations
        return list_str


