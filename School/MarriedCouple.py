class Person:
    def __init__(self, lastname, sex, age):
        self.lastname = lastname
        self.sex = sex
        self.age = age
    def __str__(self):
       return self.lastname + " is " + str(self.age) + " years old and is " + self.sex
    def getName(self):
        return self.lastname

    def getSex(self):
        return self.sex

    def getAge(self):
        return self.age

    def changeName(self, newname):
        self.lastname = newname

    def makeOlder(self):
        self.age += 1


#  NOTE:  Inside MarriedCouple, you are only allowed to use the METHODS of Person
#  DO NOT refer to the instance variables directly!  That is poor OOP coding style.  
class MarriedCouple:
    def __init__(self, nameone, sexone, ageone, nametwo, sextwo, agetwo):
        self.personone = Person(nameone, sexone, ageone)
        self.persontwo = Person(nametwo, sextwo, agetwo)
    
    def __str__(self):
        return str(self.personone) + " and " + str(self.persontwo)
    
    def changeLastNames(self,typeofchange):
        if typeofchange == "two":
            self.personone.changeName(self.persontwo.getName())
        elif typeofchange == "one":
            self.personone.changeName(self.persontwo.getName())
        elif typeofchange == "hyphen":
            self.personone.changeName(self.personone.getName() + "-" + self.persontwo.getName())
            self.persontwo.changeName(self.personone.getName())
    def ageBoth(self,years):
        for i in range(years):
            self.personone.makeOlder()
            self.persontwo.makeOlder()
    def typeOfMarriage(self):
        if self.personone.getSex() == self.persontwo.getSex():
            return("same-sex")
        else:
            return("opposite-sex")
    def mayDecember(self):
        if abs(self.personone.getAge()-self.persontwo.getAge()) > 19:
            return True
        else:
            return False


#  A sample driver to test your code
mc = MarriedCouple("Smith", "Male", 28, "Brown", "Female", 60)
print(mc)
print(mc.typeOfMarriage())
print(mc.mayDecember())
mc.changeLastNames("hyphen")
print(mc)
mc.ageBoth(10)
print(mc)

    
        
