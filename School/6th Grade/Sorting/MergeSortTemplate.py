import random

def merge(array, start, middle, end, tempa):
    # Use the tempa array to hold the merge, which will be in sorted order
    #   Then copy the tempa to array, an element at a time
    left = start
    right = middle + 1
    tempi = start
    while tempi <= end:
        if left == middle + 1:   # No more left--fill the rest from right

            

        elif right == end+1:  # No more right--fill the rest from left

            pass

        else:    # Still more from both--find the smallest one and fill

            pass

    #  Copy tempa into array--then we are done
    for i in range(start, end + 1):
        array[i] = tempa[i]


def mergeSortHelper(array, start, end, tempa):
    # print ("MSH called with start = " + str(start) + " and end = " + str(end))
    if (start < end):
        middle = (start + end) // 2
        mergeSortHelper(array, start, middle, tempa)
        mergeSortHelper(array, middle+1, end, tempa)
        merge(array, start, middle, end, tempa)

def mergeSort(array):
    tempa = [0 for i in range(len(array))]
    mergeSortHelper(array, 0, len(array)-1, tempa)

SIZE = 10
array = [i for i in range(1, SIZE+1)]
random.shuffle(array)
print(array)
mergeSort(array)
print(array)
