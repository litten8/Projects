from tkinter import *
from game import GameCanvas
import threading

program = None

class FailureType:
    def __init__(self, e):
        self.error = e

class TerminateType(Exception): pass
terminate = TerminateType()

def interfunction(game, func, state):
    def f():
        try:
            game.function_end(func(state))
        except Exception as e:
            game.function_end(FailureType(e))
    return f

class StoppableThread(threading.Thread):
    def __init__(self, func):
        threading.Thread.__init__(self,target=func)
        self.start()

    def kill(self):
        raise terminate

def reverse(grid):
    output = []
    for x in range(len(grid)):
        column = []
        for y in range(len(grid)):
            if grid[x][y] == 0:
                column.append(0)
            elif grid[x][y] == 1:
                column.append(2)
            else:
                column.append(1)
        output.append(column)
    return output

def getfunc(filename):
    exec("global program\nfrom " + filename + " import ai\nprogram=ai")
    return program

class IntGameCanvas(GameCanvas):
    TIMEOUT_LEN = 500
    MOVE_DELAY = 1000

    def __init__(self, master, rp_file, bp_file):
        GameCanvas.__init__(self, master)
        try:
            rfunc = getfunc(rp_file)
        except ImportError:
            self.import_fail(1)
        else:
            try:
                bfunc = getfunc(bp_file)
            except ImportError:
                self.import_fail(2)
            else:
                self.functions = (None, rfunc, bfunc)
                self.end = False
                self.start()

    def import_fail(self, player):
        self.deactivate()
        self.displ_import_fail(player)

    def displ_import_fail(self, player):
        if player == 1:
            pname = "red"
        else:
            pname = "blue"
        self.show_error("Import failure: invalid " + pname + " file")

    def start(self):
        if not self.end:
            if self.player == 2:
                reversed_state = reverse(self.state)
            else:
                reversed_state = [[cell for cell in column] for column in self.state]
            self.function_start(self.functions[self.player], reversed_state)

    def start_timer(self):
        self.after(IntGameCanvas.TIMEOUT_LEN, self.end_timer)

    def end_timer(self):
        if self.stop_timer:
            return
        try: self.ai_thread.kill()
        except: pass
        self.displ_timeout()
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1
        self.start()

    def function_start(self, func, state):
        self.stop_timer = False
        self.start_timer()
        self.ai_thread = StoppableThread(interfunction(self,func,state))

    def function_end(self, output):
        self.stop_timer = True
        if isinstance(output, FailureType):
            self.displ_err1_label()
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1
            self.after(IntGameCanvas.MOVE_DELAY, self.start)
            return
        try:
            x, y = output
        except:
            self.displ_err2_label()
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1
            self.after(IntGameCanvas.MOVE_DELAY, self.start)
            return
        self.domove(x, y)
        self.after(IntGameCanvas.MOVE_DELAY, self.start)

    def displ_err1_label(self):
        self.show_error("Move failure: function throwed")

    def displ_err2_label(self):
        self.show_error("Move failure: invalid func output")

    def displ_timeout(self):
        self.show_error("Move failure: timeout")

    def deactivate(self):
        GameCanvas.deactivate(self)
        self.end = True

if __name__ == "__main__":
    root = Tk()
    f = Frame(root)
    f.grid()
    c = IntGameCanvas(f, input("Enter first AI: "), input("Enter second AI: "))
    root.mainloop()
