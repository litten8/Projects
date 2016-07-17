from tkinter import *
import random
import time

SIZE = 8
array = [i for i in range(1,SIZE+1)]
comparisons = 0
swaps = 0

root = Tk()
frame = Frame(root)
frame.pack()
complabel = Label(frame, text = "Comparisons = 0")
swaplabel = Label(frame, text = "Swaps = 0")


def drawBars(canv, greens = [], blues = []):
    global array
    global comparisons
    global swaps
    canv.delete("all")
    bottomy = 24 * SIZE - 20
    startx = 10
    for i in range(SIZE):
        height = 20*array[i]
        if i in greens:
            canv.create_rectangle(startx, bottomy, startx + 10, bottomy - height, fill = "green")
        elif i in blues:
            canv.create_rectangle(startx, bottomy, startx + 10, bottomy - height, fill = "blue")
        else:
            canv.create_rectangle(startx, bottomy, startx + 10, bottomy - height, fill = "red")

        startx += 30
    complabel.config(text = "Comparisons = " + str(comparisons))
    swaplabel.config(text = "Swaps = " + str(swaps))

def isSorted():
    global array
    for i in range(SIZE-1):
        if array[i] > array[i+1]:
            return False
    return True

def swap(one, two):
    global array
    global swaps
    drawBars(sc, blues = [one,two])
    root.update()
    time.sleep(0.2)
    temp = array[one]
    array[one] = array[two]
    array[two] = temp
    swaps += 1
    drawBars(sc, blues = [one,two])
    root.update()
    time.sleep(0.2)
def dosort():
    global array
    global comparisons
    global swaps
    random.shuffle(array)
    drawBars(sc)
    # Put your sort code here, with the code
    #        drawBars(sc, blues = [], greens = [])
    #        root.update()
    #        time.sleep(0.7)
    #    whenever you want the bars to update
    #
    # Also, increment the comparison and swap variables as appropriate
    '''
    #######  BOGO SORT (run with SIZE < 10)  #######
    while not isSorted():
        one = random.randint(0,SIZE-1)
        while True:
            two = random.randint(0,SIZE-1)
            if one != two:
                break
        swap(one, two)
    drawBars(sc)
    ###########################
    '''
    '''
    #######  BUBBLE SORT (run with SIZE < 50)  #######
    for p in range(len(array)-1):
        for i in range(len(array)-1):
            comparisons+=1
            if array[i]>array[i+1]:
                swap(i, i+1)
    '''
    '''
    #######  SELECTION SORT #######
    for p in range(len(array)-1):
        smallest=p
        root.update()
        for i in range(len(array)-1):
            comparisons+=1
            if array[i]<array[smallest]:
                smallest=i
        swap(smallest,p)
    '''
    #######  INSERTION SORT ####
    

b = Button(frame, text = "Press to start sort", command = dosort)
b.pack()
sc = Canvas(frame, width = 30 * SIZE, height = 24 * SIZE)
sc.pack()

complabel.pack()
swaplabel.pack()
