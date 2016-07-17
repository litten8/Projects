import random
class Plant:
    def __init__(self, name, lifespan, seedingage, seeds, size, ecosystem):
        self.name=name
        self.maxlifespan=lifespan
        self.lifespan=self.maxlifespan
        self.seedingage=seedingage
        self.seeds=seeds
        self.size=size
        self.ecosystem=ecosystem
        self.ecosystem.addPlant(self)
        self.age=0
        self.self=self
        self.alive=True
        self.children=[]
        #print("There is a new plant named " + self.name + " with stats " +  str(self.maxlifespan) + " maxlifespan, " + str(self.seedingage) + " seedingage, " + str(self.seeds) + " seeds, " + str(self.size) + " size")
    def ageup(self):
        if self.alive:
            self.age+=1
            self.lifespan-=1
            if self.age == self.seedingage:
                self.seed()
            if self.lifespan == 0:
                self.alive=False
                print(self.name + " the plant died with stats " +  str(self.maxlifespan) + " maxlifespan, " + str(self.seedingage) + " seedingage, " + str(self.seeds) + " seeds, " + str(self.size) + " size")
    def seed(self):
        for i in range(self.seeds):
            newp=Plant(self.name, self.maxlifespan+random.randint(-1,1), self.seedingage+random.randint(-1,1), self.seeds+random.randint(-1,1), self.size+random.randint(-1,1), self.ecosystem)
            self.children.append(newp)
            self.ecosystem.addPlant(newp)
    def eaten(self, a):
        self.alive=False
        #print(self.name + " the plant was eaten by " + a.getName() + " the animal with stats " +  str(self.maxlifespan) + " maxlifespan, " + str(self.seedingage) + " seedingage, " + str(self.seeds) + " seeds, " + str(self.size) + " size")
    def isAlive(self):
        return self.alive
    def childList(self):
        return self.children
    def getName(self):
        return self.name
    def getSize(self):
        return self.size
class Animal:
    def __init__(self, name, lifespan, birthage, kidsperbirth, size, nutrition, gender, ecosystem):
        self.name=name
        self.maxlifespan=lifespan
        self.lifespan=self.maxlifespan
        self.birthage=birthage
        self.kidsperbirth=kidsperbirth
        self.size=size
        self.nutrition=nutrition
        self.gender=gender
        self.ecosystem=ecosystem
        self.ecosystem.addAnimal(self)
        self.age=0
        self.alive=True
        self.self=self
        self.children=[]
        #print("There is a new animal named " + self.name + " with stats " +  str(self.maxlifespan) + " lifespan, " + str(self.birthage) + " birthage, " + str(self.kidsperbirth) + " kidsperbirth, " + str(self.size) + " size, " + str(self.nutrition) + " nutrition, " + self.gender + " gender")
    def ageup(self):
        if self.alive:
            self.maxfoodperturn=((self.size/(self.nutrition+0.1))*10)
            self.age+=1
            self.lifespan-=1
            self.nutrition-=1.0+(self.age/10)
            if self.nutrition<=2*(1.0+(self.age/10)) and self.nutrition>0:
                for i in range(len(self.ecosystem.getPlants())):
                    if self.size>self.ecosystem.getPlants()[i].getSize() and self.ecosystem.getPlants()[i].isAlive() and self.maxfoodperturn>0 and len(self.ecosystem.getAlivePlants())>1:
                        self.eat(self.ecosystem.getPlants()[i])
            if self.age == self.birthage:
                self.ecosystem.findMate(self)
            if self.lifespan == 0 or self.nutrition<=0:
                self.alive=False
                print(self.name + " the animal died with stats " +  str(self.maxlifespan) + " lifespan, " + str(self.birthage) + " birthage, " + str(self.kidsperbirth) + " kidsperbirth, " + str(self.size) + " size, " + str(self.nutrition) + " nutrition, " + self.gender + " gender")
    def eat(self, p):
        self.nutrition+=p.getSize()/10
        self.maxfoodperturn-=p.getSize()
        p.eaten(self)
    def addChild(self, c):
        self.children.append(c)
    def getGender(self):
        return self.gender
    def getMaxLifespan(self):
        return self.maxlifespan
    def getBirthAge(self):
        return self.birthage
    def canMate(self):
        if self.age >= self.birthage and self.alive:
            return True
        else:
            return False
    def getKidsPerBirth(self):
        return self.kidsperbirth
    def isAlive(self):
        return self.alive
    def childList(self):
        return self.children
    def getName(self):
        return self.name
    def getSize(self):
        return self.size
    def getNutrition(self):
        return self.nutrition
class Ecosystem:
    def __init__(self):
        self.plants=[]
        self.animals=[]
        self.everything=[]
        self.turn=1
    def getAlive(self):
        alive=[]
        for i in range(len(self.everything)):
            if self.everything[i].isAlive():
                alive.append(self.everything[i])
        return alive
    def getAliveAnimals(self):
        alive=[]
        for i in range(len(self.animals)):
            if self.animals[i].isAlive():
                alive.append(self.animals[i])
        return alive
    def getAlivePlants(self):
        alive=[]
        for i in range(len(self.plants)):
            if self.plants[i].isAlive():
                alive.append(self.plants[i])
        return alive
    def addPlant(self, p):
        self.plants.append(p)
        self.everything.append(p)
    def addAnimal(self, a):
        self.animals.append(a)
        self.everything.append(a)
    def getAnimals(self):
        return self.animals
    def getPlants(self):
        return self.plants
    def findMate(self, a):
        for i in range(len(self.animals)):
            if not (a.getGender() == self.animals[i].getGender()) and self.animals[i].canMate() and a.getName() == self.animals[i].getName():
                for j in range(int(((a.getKidsPerBirth()+(a.getNutrition()/5)-1)+(self.animals[i].getKidsPerBirth()+(a.getNutrition()/5)-1))/2)):
                    newchild=Animal(a.getName(), (a.getMaxLifespan()+self.animals[i].getMaxLifespan())/2+random.randint(-1,1), (a.getBirthAge()+self.animals[i].getBirthAge())/2+random.randint(-1,1), (a.getKidsPerBirth()+self.animals[i].getKidsPerBirth())/2+random.randint(-1,1), (a.getSize()+self.animals[i].getSize())/2+random.randint(-1,1), (a.getNutrition()+self.animals[i].getNutrition())/2+random.randint(-1,1) ,random.choice(["Male", "Female"]), self)
                    self.addAnimal(newchild)
                    a.addChild(newchild)
                    self.animals[i].addChild(newchild)
                break
    def mainloop(self):
        for i in range(len(self.everything)):
            self.everything[i].ageup()
        print("End of Turn " + str(self.turn) + ". There are " + str(len(self.getAlive())) + " things. " + str(len(self.getAlivePlants())) + " plants, " + str(len(self.getAliveAnimals())) + " animals.")
        self.turn+=1
e=Ecosystem()
for i in range(50):
    e.addPlant(Plant("Flowey",30, 10, 5, 10, e))
e.addAnimal(Animal("Temmie",120,10,10,30,15.0, "Male",e))
e.addAnimal(Animal("Temmie",120,10,10,30,15.0, "Female",e))
while True:
    e.mainloop()
    if len(e.getAlive())<1:
        break
print("Everything is extinct.")
