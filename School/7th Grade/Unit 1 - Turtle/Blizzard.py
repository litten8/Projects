# This one is nice too, with the flakes blowing sideways

from turtle import *
import random

tlist = []
t = Turtle()
ts = t.getscreen()
ts.setup(width = 800, height = 600)
ts.colormode(255)
ts.bgcolor(230,230,255)
ts.register_shape("snowflake.gif")  # This file must be in the same folder as your code
ts.tracer(10)

# Can you make the depth of the snow increase as the program runs?
canv = ts.getcanvas()
snowdepth = 20
# The origin is at the center of the screen, but positive y is DOWN!

t.shape("snowflake.gif")
# Point each snowflake down
t.setheading(270)
t.up()
t.goto(random.randint(-400,400), random.randint(-300,300))
tlist.append(t)
for i in range(500):
    t = Turtle()
    t.shape("snowflake.gif")
    t.setheading(330)
    tlist.append(t)
    t.up()
    t.goto(random.randint(-800,400), random.randint(-300,300))
while True:
    for flake in tlist:
        flake.forward(random.randint(10,50))
        if flake.ycor() < -300:
            flake.goto(random.randint(-800,400), 300)
            snowdepth+=0.1
    canv.create_rectangle(-400,300-snowdepth,400,300, fill = "white", width = 0)

    
    
