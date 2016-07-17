class NumberDisplay:
    def __init__(self, maxValue):
        self.value = 0
        self.maxValue = maxValue
        
    def __str__(self):
        return str(self.value)
    
    def increment(self):
        self.value=(self.value+1)%self.maxValue

    def getValue(self):
        return self.value

class DigitalWatch:
    def __init__(self):
        self.minutes = NumberDisplay(60)
        self.hours = NumberDisplay(23)

    def timeTick(self):
        if (self.minutes.getValue() < 59):
            self.minutes.increment()
        else:
            self.hours.increment()
            self.minutes.increment()

    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes)
        
dw = DigitalWatch()
for i in range(100):
    print(dw)
    dw.timeTick()
    
