from turtle import Turtle
from turtle import Screen
import time
import random
from fractions import gcd

class TurtleScreen:

    def __init__(self, rows, cols):
        self.win = Screen()
        self.t = Turtle()
        self.rows = rows
        self.cols = cols
        self.win.setup(cols+100, rows+100)
        self.win.colormode(255)
        self.win.tracer(0)
        self.t.width(2)
        self.t.hideturtle()
        self.t.up()
        self.t.goto(-cols/2, rows/2)
        self.t.down()
        self.t.speed(0)
        for i in range(2):
            self.t.forward(cols)
            self.t.right(90)
            self.t.forward(rows)
            self.t.right(90)
        self.a = [['white' for i in range(cols)] for j in range(rows)]

    def erasePoint(self,x,y):
        self.t.up()
        self.t.goto(y-self.cols/2,-x+self.rows/2)
        self.t.down()
        self.t.pencolor("white")
        self.t.dot(1)
        self.a[x][y] = "white"

    def fillPoint(self,x,y,colorst="black"):
        self.t.up()
        self.t.goto(y-self.cols/2,-x+self.rows/2)
        self.t.down()
        self.t.pencolor(colorst)
        self.t.dot(1)
        self.a[x][y] = colorst

    def getColor(self,x,y):
        return self.a[x][y]

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols

    def update(self):
        self.win.update()

rows = 250
cols = 250
scr = TurtleScreen(rows,cols)

'''
for i in range(rows):
    scr.fillPoint(i,i)

for i in range(rows):
    scr.erasePoint(i,i)


for r in range(0,rows):
    for c in range(0,cols):
        if r%5 == 0 and c%5 == 0:
            scr.fillPoint(r,c,'red')

for r in range(0,rows):
    for c in range(0,cols):
        if scr.getColor(r,c)=='red':
            scr.fillPoint(r,c,'blue')
        else:
            scr.fillPoint(r,c,'red')
'''
for r in range(rows):
    for c in range(cols):
        rnd = random.randint(0,2)
        if rnd == 0:
            scr.fillPoint(r,c,'green')
        elif rnd == 1:
            scr.fillPoint(r,c,'black')
    scr.update()
'''

for r in range(1,rows):
    for c in range(1,cols):
        if gcd(r,c) == 1:
            scr.fillPoint(r,c,'red')
        else:
            scr.fillPoint(r,c,'blue')
    scr.update()


corna = 28
cornb = 28
side = 8
for r in range(0,rows):
    for c in range(0,cols):
        x = corna + (side * (r/rows))
        y = cornb + (side * (c/cols))
        z = x*x + y*y
        d = int(z)
        if d%3 == 0:
            scr.fillPoint(r,c,'red')
        elif d%3 == 1:
            scr.fillPoint(r,c,'blue')
        else:
            scr.fillPoint(r,c,'white')
            
    scr.update()
'''


            


             
        
        
