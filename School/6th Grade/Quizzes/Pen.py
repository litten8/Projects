#Bernie
class Pen:
    def __init__(self, capacity):
        self.status = "Closed"
        self.inkLeft = capacity
        self.capacity = capacity
    def getStatus(self):
        return(self.status)
    def click(self):
        if(self.status=="Open"):
            self.status =  "Closed"
        else:
            self.status = "Open"
    def write(self, text):
        if(self.status=="Open" and self.inkLeft):
            print(text)
            self.inkLeft -=1
        elif(self.status=="Closed"):
            print("Cannot Write, Pen is Closed")
        else:
            print("Out of Ink, Please Refill")
    def refill(self):
        self.inkLeft = self.capacity
