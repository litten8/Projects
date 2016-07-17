import turtle
import random
t = turtle.Pen()
win=turtle.Screen()
win.tracer(1000)
ptlist = [(-250, -250),(250, -250),(-250, 250)]
tpos = (-250, -250)
t.up()
t.speed(0)
while True:
    thept = random.choice(ptlist)
    newpos = ((tpos[0]+thept[0])/2, (tpos[1]+thept[1])/2)
    t.goto(tpos[0], tpos[1])
    t.dot(1)
    tpos = newpos
