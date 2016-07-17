import time
class GameOfLife:
    def __init__(self, game):
        self.game=game
    def check(self):
        oldgame = list(self.game)
        for i in range(len(self.game)):
            if oldgame[i] == "X" and (oldgame[(i-1)%len(oldgame)] == " " and oldgame[(i+1)%len(oldgame)] == "X") or (oldgame[(i-1)%len(oldgame)] == " " and oldgame[(i+1)%len(oldgame)] == " "):
                self.game[i] = " "
            if oldgame[i] == " " and ((oldgame[(i-1)%len(oldgame)] == "X" or oldgame[(i+1)%len(oldgame)] == "X") and not (oldgame[(i-1)%len(oldgame)] == "X" and oldgame[(i+1)%len(oldgame)] == "X")):
                self.game[i] = "X"
    def print(self):
        #print("\n"*50)
        print(self.game)
game=GameOfLife(["X", "X", " ", " ", " ", " ", " ", " "])
while True:
    game.print()
    game.check()
    time.sleep(0.5)
