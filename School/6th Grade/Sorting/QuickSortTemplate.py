import random

def quickSort(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        newa = [array[0]]
        return newa
    if len(array) == 2:
        newa = []
        newa.append(min(array[0], array[1]))
        newa.append(max(array[0], array[1]))
        return newa
    else:       # The partitioning step
        pivot = array[0]
        newa = [0 for i in range(len(array))]
        
        l=0
        r=1
        for i in range(1, len(array)):
            if array[i]<pivot:
                newa[l]=array[i]
                l+=1
            else:
                newa[-1*r]=array[i]
                r+=1
        newa[l]=pivot

        left = quickSort(newa[0:l])
        right = quickSort(newa[l+1: len(newa)])
        return left + [pivot] + right

print (quickSort([random.randint(1,100000) for i in range(10000)]))
        
