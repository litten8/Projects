from time import *
class Flashlight:
    def __init__(self, battery=10):
        self.status = False
        self.battery = battery
        self.maxBattery = battery
    def powerButton(self):
        if (self.status or not self.battery):
            self.status = False
        else:
            self.status = True
            self.battery -= 1
    def getStatus(self):
        return(self.status)
    def recharge(self):
        print("Recharging...")
        sleep(5)
        self.battery = self.maxBattery
        print("Recharged!")
x = Flashlight()
i=1/2
j=0
while(i):
    sleep(i)
    x.powerButton()
    i /=2
    j +=1
print(x.getStatus())
print(j)
