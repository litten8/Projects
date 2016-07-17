#  Good job, Bernie--except for the missing self. everything is perfect!

class Scoreboard:
    def __init__(self, nameone, nametwo):
        self.team1=TeamScore(nameone)
        self.team2=TeamScore(nametwo)
    def __str__(self):
        return(self.team1.getName() + " " + self.team1.getScore() + ", " + self.team2.getName() + " " + self.team2.getScore())
    def resetToZero(self):
        team1.reset()
        team2.reset()
    def teamOneTouchdown(self):
        team1.addToScore(6)
    def scoreDifference(self):
        return abs(self.team1.getScore()-self.team2.getScore())
    def whoIsWinning(self):
        if self.team1.getScore()-self.team2.getScore>0:
            return self.team1.getName()
        elif self.team2.getScore()-self.team1.getScore>0:
            return self.team2.getName()
        else:
            return("Tie")
    def changeTheWinner(self):
        if self.team1.getScore()-self.team2.getScore>0:
            self.team1.changeName("WINNER")
        elif self.team2.getScore()-self.team1.getScore>0:
            self.team2.changeName("WINNER")
        else:
            self.team1.changeName("WINNER")
            self.team2.changeName("WINNER")
