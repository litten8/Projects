from MishaCanvas import *

root = Tk()
f = Frame(root)
f.grid()
scr = MishaCanvas(f, 100, 150, startfill = "white")
scr.fillPoint(0, 75, 'black')
# Loop over all the rest of the rows
for r in range(1, 100):
    # Loop over columns--but skip first and last, since we need three neighbors
    for c in range(1, 150 - 1):
        left = scr.isBlack(r-1,c-1)  # Get colors of the previous row
        middle = scr.isBlack(r-1,c)
        right = scr.isBlack(r-1,c+1)
        if left == True:
            if middle == True:
                if right == True:
                    scr.erasePoint(r,c)
                else:
                    scr.fillPoint(r,c,'black')
            else:   # middle == 'white'
                if right == True:
                    scr.erasePoint(r,c)
                else:
                    scr.fillPoint(r,c,'black')
        else:  # left == 'white'
            if middle == True:
                if right == True:
                    scr.fillPoint(r,c,'black')
                else:
                    scr.erasePoint(r,c)
            else:   # middle == 'white'
                if right == True:
                    scr.fillPoint(r,c,'black')
                else:
                    scr.erasePoint(r,c)
