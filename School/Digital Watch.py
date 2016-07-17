from NumberDisplay import *

class DigitalWatch:
    def __init__(self):
        self.minutes = NumberDisplay(59)
        self.hours = NumberDisplay(23)
    def __str__(self):
        return str(str(self.hours)+":"+str(self.minutes))
    def timeTick(self):
        self.minutes.increment()
        if(not int(self.minutes)):
            self.hours.increment()
dw=DigitalWatch()
while(True):
    print(dw)
    dw.timeTick()
