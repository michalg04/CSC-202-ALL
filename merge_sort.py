'''
merge_sort: list -> list
    Takes a list and returns a sorted list
    Splits the list into a tree by cutting it in half and recursively applying
    merge_sort to the split lists
    Then sorts the lists as it moves back up the tree
    Sorts in O(nlog(n))
'''
def merge_sort(alist):
    if len(alist)>1:
        #splits list into sublists
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        #recursively calls merge_sort on the split lists
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        #compares items in lists to determine smaller item
        while i < len(lefthalf) and j < len(righthalf):
            print(1)
            #places smaller item in correct spot
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
