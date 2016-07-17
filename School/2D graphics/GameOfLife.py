from MishaCanvas import *
import random

class BlackAndWhiteCanvas(MishaCanvas):
    def __init__(self, master, rows, cols, cellsize, startfill):
        MishaCanvas.__init__(self, master, rows, cols, cellsize, startfill)
        self.spacepause=False
        self.focus_set()
        self.bind("<space>", self.space)
    def space(self, event):
        if self.spacepause:
            self.spacepause=False
        else:
            self.spacepause=True
    def neighboringFilledCellCount(self, x, y):
        count=0
        for dr in range(-1,2):
            for dc in range(-1,2):
                if (dr != 0 or dc != 0):
                    r = x + dr
                    c = y + dc
                    if r < 0:
                        r = self.getRows()-1
                    elif r >= self.getRows():
                        r = 0
                    if c < 0:
                        c = self.getCols() - 1
                    elif c >= self.getCols():
                        c = 0
                    if self.isFilled(r,c):
                        count+=1
        return count

root = Tk()
f = Frame(root)
f.grid()
c = BlackAndWhiteCanvas(f, 100, 150, 10, "white")
c.grid()


for rows in range(c.getRows()):
    for cols in range (c.getCols()):
        if random.randint(1,4)==1:
            c.fillPoint(rows, cols)

c.update()
while True:
    if not c.spacepause:
        newc = [[False for c in range(150)] for r in range(100)]
        for rows in range(c.getRows()):
            for cols in range (c.getCols()):
                if c.neighboringFilledCellCount(rows, cols)==3:
                    newc[rows][cols]=True
                elif c.neighboringFilledCellCount(rows, cols)==2 and c.isBlack(rows, cols):
                    newc[rows][cols]=True
        for rows in range(c.getRows()):
            for cols in range (c.getCols()):
                if newc[rows][cols]:
                    c.fillPoint(rows,cols)
                else:
                    c.erasePoint(rows,cols)
    c.update()

