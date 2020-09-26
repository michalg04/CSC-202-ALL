#Michal Golovanevsky, Brandon Lyday, Sean Nesbit
#Lab 6

import random

# generates a list of random integers
# int -> list
def rand_num(size):
   alist = []
   for i in range(size):
       #integer random numbers between 10 and 70
       n = random.randint(10,70)
       alist.append(n)
   return alist

# generates a list of numbers in ascending order
# int -> list
def ordered_num(size):
    alist = []
    for i in range(size):
        alist.append(i)
    return alist

# sorts a list using the insertion sort algorithm
# list ->
def insert_sort(alist):
    counter = 0
    # loops from the first index in the list to the last
    for index in range(1,len(alist)):
        counter += 1
        # saves the current value
        currentvalue = alist[index]
        # saves the position
        position = index
        # loops while the position is not zero and the list value is above current value
        while position > 0 and alist[position - 1] > currentvalue:
            counter += 1
            # incriments the counter for every comparison made
            # changes the list value to the previous one
            alist[position] = alist[position - 1]
            # decrements the position
            position = position - 1
        alist[position] = currentvalue
    print(counter)

# sorts a list using the selection sort algorithm and prints the number of comparisons
# list ->
def select_sort(alist):
    # variable that keeps track of the number of comparisons
    compCount = 0
    # goes through every index in the list
    for fillslot in range(len(alist)-1,0,-1):
        # sets first index as maximum
        positionOfMax=0
        # goes through every value up to fillslot to find the maximum in that section of the list
        for location in range(1,fillslot+1):
            # counts the number of comparisons
            compCount += 1
            # finds index of maximum
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
        # swaps the values in indexes fillslot and positionOfMax
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    print(compCount)

'''
merge_sort: list -> list
    Takes a list and returns a sorted list
    Splits the list into a tree by cutting it in half and recursively applying
    merge_sort to the split lists
    Then sorts the lists as it moves back up the tree
    Sorts in O(nlog(n))
'''
def merge_sort(alist):
    count = 0
    if len(alist)>1:
        count += 1
        #splits list into sublists
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        #recursively calls merge_sort on the split lists
        count +=merge_sort(lefthalf)
        count +=merge_sort(righthalf)
        i=0
        j=0
        k=0
        #compares items in lists to determine smaller item
        while i < len(lefthalf) and j < len(righthalf):
            count+=3
            #places smaller item in correct spot
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        count+=1
        while i < len(lefthalf):
            count+=1
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        count+=1
        while j < len(righthalf):
            count+=1
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
        count+=1
    return count

# tests selectionSort, insertionSort, and mergeSort with lists of 100, 500, 1000, 5000, and 10000 random numbers
# list ->
def listUnordered():
    size = 100
    # variable used to determine whether to multiply size by 2 or 5
    switch = 0
    while size <= 50000:
        # generates the list of random numbers and creates two copies of it
        alist = rand_num(size)
        blist = list(alist)
        clist = list(alist)
        print("Size: " + str(size))
        # sorts the list and prints the number of comparisons using selection sort, insertion sort, and merge sort
        print("Selection Sort:")
        select_sort(alist)
        print("Insertion Sort:")
        insert_sort(blist)
        print("Merge Sort:")
        print(merge_sort(clist))
        print("")
        if switch == 0:
            size = size * 5
            switch = 1
        else:
            size = size * 2
            switch = 0

# tests selectionSort, insertionSort, and mergeSort with lists of 100, 500, 1000, 5000, and 10000 numbers in ascending order
# list ->
def listOrdered():
    size = 100
    # variable used to determine whether to multiply size by 2 or 5
    switch = 0
    while size <= 50000:
        # generates the list of numbers and two copies of it
        alist = ordered_num(size)
        blist = list(alist)
        clist = list(alist)
        print("Size: " + str(size))
        # sorts the list and prints the number of comparisons using selection sort, insertion sort, and merge sort
        print("Selection Sort:")
        select_sort(alist)
        print("Insertion Sort:")
        insert_sort(blist)
        print("Merge Sort:")
        print(merge_sort(clist))
        print("")
        if switch == 0:
            size = size * 5
            switch = 1
        else:
            size = size * 2
            switch = 0


print("Unordered Lists:")
listUnordered()
print("")

print("Ordered Lists:")
listOrdered()