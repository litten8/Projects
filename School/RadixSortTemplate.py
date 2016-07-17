import random

# This code assumes all integers in the array have no more than 4 digits
#   Try chanxging the code so that it works for integers of any size
def radixSort(array):
    for i in range(4):     # Four passes needed, since all numbers have 4 digits
        bins = [[] for i in range(10)]
        for num in array:
            copy = numx
            for j in range(i):
                copy = copy//10
            digit = copy % 10
            bins[digit].append(num)
        for i in range(len(bins)):
            for j in range(len(bins[i])):
                array.append(bins[i][j])
SIZE = 10
array = [random.randint(0,9999) for i in range(SIZE)]
print(array)
radixSort(array)
print(array)
