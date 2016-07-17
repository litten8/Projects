import time
def binarySearch(array, value):
    low = 0
    high = len(array)-1
    while (low <= high):
        mid = (low + high) // 2
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return -1
def doIt(i, items, credit):
    items=sorted(items)
    for j in range(len(items)):
        need=credit-items[j]
        check=binarySearch(items, need)
        if check >= 0 and j!=check:
            print("Case #{}: {} {}".format(i, items[j], items[check]))
            break
'''    for j in range(len(items)):
        for k in range(j+1, len(items)):
            if items[j]+items[k]==credit:
                print("Case #{}: {} {}".format(i, items[j], items[k]))
                return'''
                

f = open("FindSumTests.txt")
start = time.time()
n = int(f.readline().strip())
for i in range(1, n+1):
    credit = int(f.readline().strip())
    itemno = int(f.readline().strip())
    items = [int(i) for i in f.readline().strip().split()]

    doIt(i, items, credit)                
                
finish = time.time()
print ("It took " + str(finish-start) + " seconds")
