# FILE DESCRIPTION
#    This file contains code to play the game, human-to-human. This should be
#    used to play individual games, without any interaction with AIs.
# FILE CONTENTS
#    import: tkinter
#    class: InvalidMove, inherits from: Exception
#        <None>
#    class: GameCanvas, inherits from: tkinter.Canvas
#        const. static attr.: CELL_DIMEN at 50
#        const. static attr.: CIRCLE_RAD at 20
#        const. static attr.: BOARD_DIMEN at 8
#        const. static attr.: BACKGROUND at "green"
#        const. static attr.: COLORS at [None, "red", "blue"]
#        method: <self> __init__(<self>, tkiner.Frame)
#        method: <None> draw_grid(<self>)
#        method: <None> draw_circle(<self>, int, int, str)
#        method: <None> domove(<self>, int, int)
#        method: <None> gamemove(<self>, int, int, int)
#        method: <None> check_for_captures(<self>, int, int)
#        method: str won(<self>)
#        method: <None> deactivate(<self>)
#        method: str get_winner(<self>)
#        method: <None> displ_inv_move(<self>)
#        method: <None> del_inv_move(<self>)
#    class TrnCompatGame, inherits from: GameCanvas
#        method: <self> __init__(<self>, tkinter.Frame, str, str)
#        method: str won(<self>), overrides version in: GameCanvas
#    class HPGameCanvas, inherits from: GameCanvas
#        method: <self> __init__(<self>, tkinter.Frame)
#        method: tuple cell_coords(<self>, int, int)
#        method: <None> event_move(<self>, <unknown>)

from tkinter import *

class InvalidMove(Exception):
    ''' Thrown by GameCanvas.gamemove when an invalid move is attempted '''
    pass

class GameCanvas(Canvas):
    ''' Base class for all game classes '''

    # static attributes
    CELL_DIMEN = 60 # dimensions of each cell
    CIRCLE_RAD = 26 # radius of game pieces
    BOARD_DIMEN = 10 # board dimensions
    BACKGROUND = "green" # the background color of the Canvas
    COLORS = [None, "red", "blue"] # colors of game pieces
    ERROR_DELAY = 2000

    def __init__(self, master):
        ''' Initialization method '''
        width = GameCanvas.CELL_DIMEN * GameCanvas.BOARD_DIMEN
        Canvas.__init__(self, master, width=width, height=width,
                        borderwidth=0, background=GameCanvas.BACKGROUND)
        self.grid(padx=0, pady=0)
        # set state to a BOARD_DIMEN by BOARD_DIMEN array of 0s
        self.state = [[0 for x in range(GameCanvas.BOARD_DIMEN)] \
                      for y in range(GameCanvas.BOARD_DIMEN)]
        self.circles = [[None for x in range(GameCanvas.BOARD_DIMEN)]
                        for y in range(GameCanvas.BOARD_DIMEN)]
        self.player = 1 # red goes first
        self.moves_left = GameCanvas.BOARD_DIMEN**2 # moves left until the board filles up
        self.draw_grid()

    def draw_grid(self):
        ''' Draws the grid lines on the game board '''
        total_width = GameCanvas.CELL_DIMEN * GameCanvas.BOARD_DIMEN
        for i in range(GameCanvas.BOARD_DIMEN+1):
            # draw horizontal line
            self.create_line(0,i*GameCanvas.CELL_DIMEN,
                             total_width, i*GameCanvas.CELL_DIMEN)
            # draw vertical line
            self.create_line(i*GameCanvas.CELL_DIMEN, 0,
                             i*GameCanvas.CELL_DIMEN, total_width)

    def draw_circle(self, x, y, color):
        ''' Draw a game piece in the cell at (x,y) with color color '''
        xcenter = (x + 0.5) * GameCanvas.CELL_DIMEN
        ycenter = (y + 0.5) * GameCanvas.CELL_DIMEN
        self.circles[x][y] = self.create_oval(xcenter - GameCanvas.CIRCLE_RAD,
                                              ycenter - GameCanvas.CIRCLE_RAD,
                                              xcenter + GameCanvas.CIRCLE_RAD,
                                              ycenter + GameCanvas.CIRCLE_RAD,
                                              fill = color)

    def domove(self, cellx, celly):
        ''' Attempt to place a game piece at (cellx,celly) and respond
            accordingly '''
        try:
            self.gamemove(cellx, celly, self.player)
        except InvalidMove: # move failed
            self.displ_inv_move() # display an "Invalid move" message
            #return # end function call; everything after this assumes that the move succeeded
        self.moves_left -= 1
        if self.moves_left == 0: # if the board is filled completely
            self.won() # find out who won and display a win message
        # swap players
        if self.player==1:
            self.player = 2
        else:
            self.player = 1

    def gamemove(self, x, y, player):
        ''' Attempt to place a game piece at (cellx,celly) '''
        if self.state[x][y] == 0: # if the cell at (cellx,celly) is empty
            self.state[x][y] = player # update the internal state
            self.draw_circle(x, y, GameCanvas.COLORS[player]) # draw a game piece
            self.check_for_captures(x, y) # check for any captures
        else:
            raise InvalidMove()

    def check_for_captures(self, x, y):
        ''' Check for any pieces captured by the piece at (x,y) '''

        captured_pieces = []
        if self.state[x][y] == 1:
            f = "red"
        else:
            f = "blue"

        # for every (ox,oy) other than (x,y)
        for ox in range(GameCanvas.BOARD_DIMEN):
            if ox == x: continue
            for oy in range(GameCanvas.BOARD_DIMEN):
                if oy == y: continue
                # if a rectangle with corners (x,y), (x,oy), (ox,y), and (ox,oy)
                # is completed
                if self.state[x][y] == self.state[x][oy] == \
                   self.state[ox][y] == self.state[ox][oy] != 0:
                    # for every (cx,cy) inside or on the border of that rectangle
                    for cx in range(min(x, ox), max(x, ox)+1):
                        for cy in range(min(y, oy), max(y, oy)+1):
                            if self.state[cx][cy] != 0:
                                # capture the piece
                                captured_pieces.append((cx,cy))

        for coordx, coordy in captured_pieces:
            self.state[coordx][coordy] = self.state[x][y]
            self.itemconfig(self.circles[coordx][coordy], fill=f)

    def won(self):
        ''' Announces the winner of the game '''
        totalwidth = GameCanvas.BOARD_DIMEN * GameCanvas.CELL_DIMEN
        w = self.getwinner() # get the winner of the game
        # announce their accomplishment with big text in the middle of the screen
        self.create_text(totalwidth/2, totalwidth/2, text=w+" won!", font=("Arial",50))
        self.deactivate() # "deactivate" the game
        return w

    def deactivate(self):
        ''' "Deactivates" the game '''
        # Stop listening for mouse clicks
        self.unbind("<Button-1>")

    def get_counts(self):
        redcount = 0
        bluecount = 0
        for column in self.state:
            for cell in column:
                if cell == 1: redcount += 1
                if cell == 2: bluecount += 1
        return (redcount, bluecount)

    def getwinner(self):
        ''' Finds the winner of the game '''
        redcount, bluecount = self.get_counts()
        if redcount > bluecount: return "Red"
        else: return "Blue"

    def show_error(self, msg):
        self.err_lbl = self.create_text(
            GameCanvas.CELL_DIMEN * GameCanvas.BOARD_DIMEN/2, 15,
            text=msg, font=("Arial",20))
        self.after(GameCanvas.ERROR_DELAY, self.del_error)

    def del_error(self):
        self.delete(self.err_lbl)

    def displ_inv_move(self):
        self.show_error("Invalid move")

class TrnCompatGame(GameCanvas):
    ''' Game class which is compatible with tournaments '''
    def __init__(self, master, player1, player2):
        ''' Initialization method '''
        GameCanvas.__init__(self, master)
        self.trnmnt = master
        self.redplayer = player1
        self.blueplayer = player2

    def won(self):
        ''' Called when someone wins; overrides version in GameCanvas '''
        w = GameCanvas.won(self)
        # end current competition
        if w == "Red":
            self.trnmnt.end_comp(self.redplayer)
        if w == "Blue":
            self.trnmnt.end_comp(self.blueplayer)
        return w

class HPGameCanvas(GameCanvas):
    ''' Game for human-to-human playing '''
    def __init__(self, master):
        GameCanvas.__init__(self, master)
        # bind mouse clicks to callback
        self.bind("<Button-1>", self.event_move)

    def cell_coords(self, mousex, mousey):
        ''' Returns the cell in which the pixel position (mousex,mousey) is in '''
        return (mousex//GameCanvas.CELL_DIMEN, mousey//GameCanvas.CELL_DIMEN)

    def event_move(self, event):
        ''' Attempt to do a move in the cell which the mouse clicked '''
        x, y = self.cell_coords(event.x, event.y)
        self.domove(x,y)

if __name__ == "__main__":
    # the following test code is only executed if this module is not imported
    root = Tk()
    f = Frame(root)
    f.grid()
    c = HPGameCanvas(f)
    root.mainloop()
