import copy

class Anagrammer:
    def __init__(self,filename):
        self.filename = filename
    def dictToString(self, d):
        str=""
        for k in d:
            str = str+(k*d[k])
        return str
    def stringToDict(self,str):
        d={}
        for c in str:
            d[c] = d.get(c, 0) + 1
        return d
    def containedIn(self,d1,d2):
        for k in d2:
            if not (k in d1 and d2[k] > d1[k]):
                return False
        return True
    def removeFrom(self, d1, d2):
        d1copy = copy.deepcopy(d1)
        for k in d2:
            if k in d1copy:
                if d2[k] < d1copy[k]:
                    d1copy[k]-=d2[k]
                else:
                    del d1copy[k]
        return d1copy
    def sameAs(self, d1, d2):
        if self.containedIn(d1,d2) and self.containedIn(d2,d1):
            return True
        return False
    def printAllAnagrams(self, phrase):
        f = open(self.filename)
        wordlist = [line.strip().lower() for line in f]
        f.close()
        for i in range(len(wordlist)):
            strword = wordlist[i]
            word = self.stringToDict(strword)
            if self.containedIn(phrase, word):
                leftover = self.removeFrom(phrase, word)
                tryit = self.findAnAnagram(wordlist,leftover, i+1)
                if not (tryit is None):
                    print (strword + " " + tryit)
    def findAnAnagram(self,wordlist,dbig,index):
        for i in range(index, len(wordlist)):
            word = wordlist[i]
            dsmall = self.stringToDict(word)
            if self.sameAs(dsmall, dbig):
                return word
            elif self.containedIn(dbig, dsmall):
                leftover = self.removeFrom(dbig, dsmall)
                recurse = self.findAnAnagram(wordlist,leftover, i+1)
                if not (recurse is None):
                    return word + " " + recurse
        return None
a = Anagrammer("commonwords.txt")
a.printAllAnagrams(a.stringToDict("tehfo"))
