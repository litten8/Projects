#  You didn't write a couple of the required methods, Bernie
#    but the ones I see are all correct, except for
#    smallestColumnAverage

class BNBNumberMatrix:
    def __init__(self, rows=3, cols=4, fill=0):
        self.rows = rows
        self.cols = cols
        self.a = [[fill for c in range(self.cols)] for r in range(self.rows)]
    def __str__(self):
        toprint=""
        for i in range(self.rows):
            toprint = toprint + "\n" + str(self.a[i])
        return(toprint)
    def fillArray(self, startvalue):
        for c in range(self.cols):
            for r in range(self.rows):
                self.a[r][c] = startvalue + r + c * self.rows
    def evenColumnSum(self):
        mysum=0
        for c in range(self.cols):
            for r in range(self.rows):
                if c%2 == 0:
                    mysum=mysum+self.a[r][c]
        return mysum
    def smallestColumnAverage(self):
        mysum=0
        for r in range(self.rows):
            mysum += self.a[r][0]
        smallestsumsofar=mysum/self.cols
        # This one doesn't quite work, as you forgot to set
        #   mysum back to zero at the start of the loop
        for c in range(self.cols):
            for r in range(self.rows):
                mysum += self.a[r][c]
            if mysum/self.cols < smallestsumsofar:
                smallestsumsofar=mysum/self.cols
        return smallestsumsofar
    def sumBorders(self):
        mysum=0
        for c in range(self.cols):
            for r in range(self.rows):
                if c == 0 or r == 0 or c == self.cols-1 or r == self.rows-1:
                    mysum=mysum+self.a[r][c]
        return(mysum)
x= BNBNumberMatrix()
print(x)
x.fillArray(5)
print(x)
print(x.evenColumnSum())
print(x.smallestColumnAverage())
print(x.sumBorders())
