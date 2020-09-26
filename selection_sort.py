import random

# sorts a list using the selection sort algorithm
# selectionSort list ->
def selectionSort(alist):
    compCount = 0
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            compCount += 1
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    print("Number of Comparisons: " + str(compCount))

# generates a list of random integers
# rand_num int -> list
def rand_num(size):
    alist = []
    for i in range(size):
        n = random.randint(10, 70)
        alist.append(n)
    return alist

# generates a list of numbers in ascending order
# ordered_num int -> list
def ordered_num(size):
    alist = []
    for i in range(size):
        alist.append(i)
    return alist

# tests selectionSort with lists of 100, 500, 1000, 5000, and 10000 random numbers from in range(10, 70)
# listUnordered ->
def listUnordered():
    size = 100
    # variable used to determine whether to multiply size by 2 or 5
    switch = 0
    while size <= 10000:
        # generates the list of random numbers
        alist = rand_num(size)
        print("Size: " + str(size))
        # sorts the list and prints the number of comparisons
        selectionSort(alist)
        print("")
        if switch == 0:
            size = size * 5
            switch = 1
        else:
            size = size * 2
            switch = 0

# tests selectionSort with lists of 100, 500, 1000, 5000, and 10000 numbers in ascending order
# listOrdered ->
def listOrdered():
    size = 100
    # variable used to determine whether to multiply size by 2 or 5
    switch = 0
    while size <= 10000:
        # generates the list of numbers
        alist = ordered_num(size)
        print("Size: " + str(size))
        # sorts the list and prints the number of comparisons
        selectionSort(alist)
        print("")
        if switch == 0:
            size = size * 5
            switch = 1
        else:
            size = size * 2
            switch = 0

print("Selection Sort with Unordered List:")
listUnordered()
print("")

print("Selection Sort with Ordered List:")
listOrdered()