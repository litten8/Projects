from tkinter import *
import time

class MishaCanvas(Canvas):

    def __init__(self, master, rows, cols, cellsize = 10, startfill = "white"):
        self.rows = rows
        self.cols = cols
        self.cellsize = cellsize
        self.width = self.cellsize * cols
        self.height = self.cellsize * rows
        Canvas.__init__(self, master, width = self.width, height = self.height,
                        borderwidth=0, background='white')
        self.grid(padx=0, pady=0)
        if startfill == "white":
            self.bind("<Button-1>", self.makeBlack)
        else:
            self.bind("<Button-1>", self.makeWhite)

        self.color = [[startfill for x in range(cols)] 
                      for y in range(rows)]
#        self.draw_grid()
        self.rects = self.makeRectangles(startfill)

    def draw_grid(self):
        total_width = self.cellsize * self.cols
        total_height = self.cellsize * self.rows
        for i in range(self.rows+1):
            self.create_line(0,i*self.cellsize,
                             total_width, i*self.cellsize)
        for j in range(self.cols+1):
            self.create_line(j*self.cellsize, 0,
                             j*self.cellsize, total_height)

    def makeRectangles(self, fillcolor = "black"):
        returnme = [[0 for x in range(self.cols)] for y in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                xup = r  * self.cellsize
                yleft = c  * self.cellsize
                returnme[r][c] = self.create_rectangle(yleft, xup, yleft + self.cellsize,
                         xup + self.cellsize,
                         fill = fillcolor, outline="white")
        return returnme
    

    def fillPoint(self, x, y, fillcolor = "black"):
        xup = x  * self.cellsize
        yleft = y  * self.cellsize
        '''
        self.create_rectangle(yleft, xup, yleft + self.cellsize,
                         xup + self.cellsize,
                         fill = fillcolor)
        '''
        self.itemconfig(self.rects[x][y], fill = fillcolor, outline = fillcolor)
        self.color[x][y] = fillcolor

    def erasePoint(self, x, y):
        xup = x  * self.cellsize
        yleft = y  * self.cellsize
        '''
        self.create_rectangle(yleft, xup, yleft + self.cellsize,
                         xup + self.cellsize,
                         fill = "white")
        '''
        self.itemconfig(self.rects[x][y], fill = "white", outline = "white")
        self.color[x][y] = "white"
        
    def cell_coords(self, mousex, mousey):
        return (mousex//self.cellsize, mousey//self.cellsize)
    
    def makeWhite(self, event):
        x, y = self.cell_coords(event.x, event.y)
        self.erasePoint(y,x)   # To change to row/column form

    def makeBlack(self, event):
        x, y = self.cell_coords(event.x, event.y)
        self.fillPoint(y,x)   # To change to row/column form

    def isColor(self, x, y, color):
        if self.color[x][y] == color:
            return True
        return False

    def isBlack(self, x, y):
        if self.color[x][y] == "black":
            return True
        return False

    def isFilled(self, x, y):
        if self.color[x][y] != "white":
            return True
        return False

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols

    def getCellSize(self):
        return self.cellsize







    
