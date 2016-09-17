from turtle import *
import random
import turtle
import time
class BNBTurtle(Turtle):
    def __init__(self):
        Turtle.__init__(self)
    def poly(self, sideLength, sides, rotates):
        for i in range(sides):
            self.forward(sideLength)
            self.right((360/sides)*rotates)
    def tree(self, levels, sidelength):
        if (levels == 1):
            self.color(0, 200, 0)
            self.width(sidelength)
            self.forward(sidelength)
            self.backward(sidelength)
            self.width(levels)
            self.color(200, 100, 0)
        else:
            self.color(200, 100, 0)
            self.width(levels)
            self.forward(sidelength)
            self.left(15)
            self.tree(levels-1, 2*sidelength/3)
            self.right(30)
            self.tree(levels-1, 2*sidelength/3)
            self.left(15)
            self.backward(sidelength)
    def snowflake(self, levels, sidelength, sides):
        if (levels == 1):
            self.forward(sidelength)
        else:
            self.snowflake(levels-1, sidelength/3, sides)
            self.left(180-(360/sides))
            for i in range(0, sides-2):
                self.snowflake(levels-1, sidelength/3, sides)
                self.right(360/sides)
            self.snowflake(levels-1, sidelength/3, sides)
            self.left(180-(360/sides))
            self.snowflake(levels-1, sidelength/3, sides)

win = turtle.Screen()
win.colormode(255)
t = BNBTurtle()
t.speed(0)
t.setheading(90)
t.up()
t.goto(0,-250)
t.down()
win.tracer(100)
t.snowflake(6, 200, 3)
win.update()
time.sleep(3)
t.clear()
t.speed(0)
t.setheading(90)
t.up()
t.goto(0,-250)
t.down()
win.tracer(100)
t.tree(6, 200)
win.update()
time.sleep(3)
t.clear()

