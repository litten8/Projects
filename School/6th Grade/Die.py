from random import *

class Die:
    def __init__(self, sides=6):
        self.sides = sides
        self.timesRolled = 0
    def roll(self):
        self.timesRolled += 1
        return randint(1, self.sides)
    def getTimesRolled(self):
        return self.timesRolled
d=Die(7)
for i in range(100):
    daniel=0
    damon=0
    drV=0
    for i in range(100):
        roll1=d.roll()
        roll2=d.roll()
        roll3=d.roll()
        if roll1 == roll2 or roll2 == roll3 or roll1 == roll3:
            daniel+=1
        elif roll1 > 1 and roll2 > 1 and roll3 > 1:
            damon+=1
        else:
            drV+=1
    print("Daniel got " + str(daniel) + "% of the pizza")
    print("Damon got " + str(damon) + "% of the pizza")
    print("Dr. V got " + str(drV) + "% of the pizza")
    print("")
