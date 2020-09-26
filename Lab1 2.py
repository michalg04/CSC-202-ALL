# Name: Michal Golovanevsky
# Section: 7

def max_list_iter(tlist):
   """ finds the max of a list of numbers and returns it, not the index"""
   if tlist == [] or len(tlist) == 0: #checks if the list is empty and raises an error if it is
      raise ValueError('empty list')
   else:
      max = tlist[0] #initializes max value
      for i in tlist:
         # checks if the next value in the list is greater than the current max
         if i > max:
            max = i #changes the max value to the current greatest value
      return max #returns greatest value once found

def reverse_rec(tempstr):
   """ recursively reverses a string and returns it """
   if tempstr == "": #checks if string is empty
      return ''
   else:
      #calls reverse_rec starting from the second element and concatinating the first element to it
      return reverse_rec(tempstr[1:]) + tempstr[0]


# Binary Search
def bin_search(target, low, high, list_val):
   """searches for target in list_val[low..high] and returns index if found"""
   # checks and returns None if the list is empty
   if len(list_val) == 0 or list_val is None:
      return None
   # checks and returns None if low is greater than high
   elif low > high:
      return None
   #checks if low or high are correct indexes in list_val
   elif low < 0 or high < 0 or high > (len(list_val) -1) or low > (len(list_val) -1):
      raise ValueError('low or high not in the range of list_val')
   else:
      list_val.sort() #sorts the given list
      midpoint = (low + high) // 2 #initializes a midpoint value
      # checks and returns the midpoint if it's equal to the target
      if target == list_val[midpoint]:
         return midpoint
      elif target > list_val[midpoint]: #checks if the target is in the upper half
         # recursively calls back the funtion with an increased midpoint as the lower bound
         return bin_search(target, midpoint + 1, high, list_val)
      else:
         # recursively calls back the funtion with a decreased midpoint as the upper bound
         return bin_search(target, low, midpoint - 1, list_val)






