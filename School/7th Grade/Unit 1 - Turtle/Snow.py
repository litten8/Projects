# This is a nice effect. Perhaps using "manual updates" (with the tracer set to 0)
#   would make it run a little faster.  

from turtle import *
import random

tlist = []
slist = []
t = Turtle()
ts = t.getscreen()
ts.setup(width = 800, height = 600)
ts.colormode(255)
ts.bgcolor(200,200,255)
ts.register_shape("snowflake.gif")
ts.register_shape("snowflake2.gif") # This file must be in the same folder as your code
ts.tracer(100)

# Can you make the depth of the snow increase as the program runs?
canv = ts.getcanvas()
snowdepth = 0
# The origin is at the center of the screen, but positive y is DOWN!

t.shape(random.choice(["snowflake.gif", "snowflake2.gif"]))
# Point each snowflake down
t.setheading(270+random.randint(-10,10))
t.up()
t.goto(random.randint(-400,400), random.randint(-300,300))
tlist.append(t)
slist.append(random.randint(1,5))
def createSnowflake(x,y):
    t = Turtle()
    t.shape(random.choice(["snowflake.gif", "snowflake2.gif"]))
    t.setheading(270+random.randint(-10,10))
    tlist.append(t)
    slist.append(random.randint(1,5))
    t.up()
    t.goto(x,y)
for i in range(30):
    createSnowflake(random.randint(-400,400), random.randint(-300,300))
ts.listen()
ts.onclick(createSnowflake)
while True:
    for i in range(len(tlist)):
        tlist[i].forward(slist[i])
        if tlist[i].ycor() < -305+snowdepth:
            tlist[i].goto(random.randint(-400,400), 300)
            tlist[i].setheading(270+random.randint(-10,10))
            slist[i]=random.randint(1,5)
            snowdepth+=0.1
            if snowdepth>=600:
                print("Traceback (most recent call last):\n  File \"/Users/Bernie/Dropbox (Proof School)/Bernie Python/Projects/School/7th Grade/Unit 1 - Turtle/Snow.py\", line 49, in <module>\n    cats+=9001\nNameError: name 'cats' is not defined")
                cats+=9001
    canv.create_rectangle(-400,300-snowdepth,400,300, fill = "white", width = 0)
