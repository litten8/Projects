from tkinter import *
from time import *

tk = Tk()
f = Frame(tk)
f.pack()
c = Canvas(f, width=500, height=500)
c.pack()
x1=[0,0,0,0,0]
x2=[0,0,0,0,0]
x3=[0,0,0,0,0]
x4=[0,0,0,0,0]
x5=[0,0,0,0,0]
x6=[0,0,0,0,0]
xy=[x1,x2,x3,x4,x5,x6]
def fallingRectangle(event):
    xPos = int(event.keysym)
    j = c.create_rectangle((xPos-1)*100, -100, xPos*100, 0, fill="green")
    yPos=0
    for i in range(0, 5):
        sleep(0.1)
        if (not xy[yPos+1][xPos-1] == 1):
            yPos+=1
            c.move(j, 0, 100)
            tk.update()
        xy[yPos][xPos-1] = 1
        xy[yPos-1][xPos-1] = 0

c.bind_all("1", fallingRectangle)
c.bind_all("2", fallingRectangle)
c.bind_all("3", fallingRectangle)
c.bind_all("4", fallingRectangle)
c.bind_all("5", fallingRectangle)
