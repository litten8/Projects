class MovieGoersOne:
    def __init__(self):
        self.d={}
    def hasSeen(self, person, movie):
        if movie in self.d[person]:
            return True
        else:
            return False
    def printMoviesSeen(self):
        for key, value in self.d.items():
            print(key + " has seen:")
            for i in value:
                print(i)
    def peopleSeeingMovie(self, movie):
        s=set()
        for key, value in self.d.items():
            if movie in value:
                s.add(key)
        return(s)
    def addMovie(self, movie, attendees):
        for i in attendees:
            self.d[i] = self.d.get(i, set())
            self.d[i].add(movie)

'''
# Part One test added by SLG.  Ran perfectly--good job!

mg = MovieGoersOne()
mg.addMovie("2001", ["Steve"])
mg.addMovie("2001", ["Steve","Rochelle","Sara","Alex"])
mg.addMovie("LOA",["Steve", "Rochelle"])
mg.addMovie("Ben Hur",["Steve", "Sara"])
mg.addMovie("Ben Hur", ["Allison"])
mg.addMovie("Ben Hur", ["Allison"])

mg.printMoviesSeen()
print (mg.hasSeen("Steve","2001"))
print (mg.hasSeen("Sara", "LOA"))
print (mg.peopleSeeingMovie("2001"))
print (mg.peopleSeeingMovie("Ben Hur"))
print (mg.peopleSeeingMovie("LOA"))
'''

class MovieGoersTwo:
    def __init__(self):
        self.d={}
    def hasSeen(self, person, movie):
        if movie in self.d[person]:
            return self.d[person][movie]
        else:
            return 0
    def printMoviesSeen(self):
        for key, value in self.d.items():
            print(key + " has seen:")
            for key2, value2 in self.d[key].items():
                print(key2 + " " + str(value2) + " times.")
    def peopleSeeingMovie(self, movie):
        s=set()
        for key, value in self.d.items():
            if movie in value:
                s.add(key)
        return(s)
    def addMovie(self, movie, attendees):
        for i in attendees:
            self.d[i] = self.d.get(i, dict())
            self.d[i][movie] = self.d[i].get(i, 0)
            self.d[i][movie]+=1

# Part Two test added by SLG
#   Keep working on this, Bernie--the test program below didn't run correctly

mg = MovieGoersTwo()
mg.addMovie("2001", ["Steve"])
mg.addMovie("2001", ["Steve","Rochelle","Sara","Alex"])
mg.addMovie("2001", ["Steve", "Alex"])
mg.addMovie("LOA",["Steve", "Rochelle"])
mg.addMovie("Ben Hur",["Steve", "Sara"])
mg.addMovie("Ben Hur", ["Allison"])
mg.addMovie("Ben Hur", ["Allison"])

mg.printMoviesSeen()
print (mg.hasSeen("Steve","2001"))
print (mg.hasSeen("Alex","2001"))
print (mg.hasSeen("Sara","2001"))
print (mg.hasSeen("Allison","Ben Hur"))
print (mg.hasSeen("Steve","Ben Hur"))
print (mg.hasSeen("Sara", "LOA"))
print (mg.hasSeen("Alex", "Ben Hur"))
print (mg.peopleSeeingMovie("2001"))
print (mg.peopleSeeingMovie("Ben Hur"))
print (mg.peopleSeeingMovie("LOA"))
