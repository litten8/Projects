class CharacterMatrix:
    def __init__(self, rows, cols, fill, empty):
        self.a = [[empty for c in range(cols)] for r in range(rows)]
        self.rows = rows  # You don't really need these,
        self.cols = cols  #     but they can make life easier
        self.fill = fill
        self.empty = empty
        
    def printArray(self):
        #  Loop if you don't need the row and column indices
        for row in self.a:
            for item in row:
                print(str(item) + ' ', end = "")
            print()
            
    def checkerboard(self):
        #  Loop if you do need the row and column indices
        for r in range(self.rows):
            for c in range(self.cols):
                if (r+c)%2 == 0:
                    self.a[r][c] = self.fill
                else:
                    self.a[r][c] = self.empty
    def addBorder(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if(r == 0 or r == len(self.a[r]) or c == 0 or c == len(self.a[c])):
                    self.a[r][c] = self.fill
        

tm = CharacterMatrix(4,6,'X',' ')
tm.printArray()
print()
tm.checkerboard()
tm.printArray()
tm.addBorder()
