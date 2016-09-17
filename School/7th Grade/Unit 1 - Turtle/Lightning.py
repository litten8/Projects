import turtle
import time as misha
import random

t=turtle.Pen()
ts=t.getscreen()
turtle.colormode(255)
ts.bgcolor(0, 0, 20)

def lightning(x, y, t=t):
    turtle.colormode(255)
    ts.bgcolor(0, 0, 20)
    height=ts.window_height()
    width=ts.window_width()
    t.speed(0)
    ts.tracer(10)
    t.up()
    t.pencolor(255-random.randint(1,100), 255-random.randint(1,100), 255-random.randint(1,100))
    y = height/2
    t.goto(x, y)
    t.down()
    while x < height/2 and x > -height/2 and y < width/2 and y > -width/2:
        if random.randint(0,20)==20:
            t2=turtle.Pen()
            t2.up
            t2.goto(x, y)
            t2.down
            noreclightning(x+random.randint(-20,20), y, t2)
        x += random.randint(-10, 10)
        y += random.randint(-10, 0)
        t.goto(x, y)
    misha.sleep(0.25)
    t.clear()
def noreclightning(x, y, t=t):
    turtle.colormode(255)
    ts.bgcolor(0, 0, 20)
    height=ts.window_height()
    width=ts.window_width()
    t.speed(0)
    ts.tracer(10)
    t.up()
    t.pencolor(255-random.randint(1,100), 255-random.randint(1,100), 255-random.randint(1,100))
    t.goto(x, y)
    t.down()
    while x < height/2 and x > -height/2 and y < width/2 and y > -width/2:
        x += random.randint(-10, 10)
        y += random.randint(-10, 0)
        t.goto(x, y)
    misha.sleep(0.25)
    t.clear()

ts.listen()
ts.onclick(lightning)
