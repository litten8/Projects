from world2d import *
import random

class EcoObject(Object):
    def __init__(self, tile=None, name="Rock", size=1.0, shade=0, ground=True):
        Object.__init__(self, tile=tile, name=name)
        self.size=size
        self.ground=ground
    def setSize(self, size):
        self.size=size
    def setShade(self, shade):
        self.shade=shade
    def setGround(self, ground):
        self.ground=ground
    def getSize(self):
        return self.size
    def getShade(self):
        return self.shade
    def getGround(self):
        return self.ground

class Cloud(EcoObject):
    def __init__(self, tile=None, name="Cloud", size=1.0, shade=0, ground=False):
        EcoObject.__init__(self, tile, name, size, shade, ground)
        self.raining=False
    def turn(self):
        self.shade=self.size
        move=random.randint(1,4)
        if move==1:
            self.moveNorth()
        if move==2:
            self.moveSouth()
        if move==3:
            self.moveEast()
        if move==4:
            self.moveWest()
        if self.raining:
            self.size-=0.5
            self.tile.setNewMoisture(self.tile.getNewMoisture()+5)
        elif self.size>=10.0:
            self.raining=True
        if self.size<=0.0:
            self.tile.removeObject(self)
            self.tile=None
    def getRaining(self):
        return self.raining

class Plant(EcoObject):
    def __init__(self, tile=None, name="Weed", size=1.0, shade=0, ground=True):
        EcoObject.__init__(self, tile=tile, name=name, size=size, shade=shade, ground=ground)

class Animal(EcoObject):
    def __init__(self, tile=None, name="Mouse", size=1.0, shade=0, ground=True):
        EcoObject.__init__(self, tile=tile, name=name, size=size, shade=shade, ground=ground)

class Fungus(EcoObject):
    def __init__(self, tile=None, name="Mushroom", size=1.0, shade=0, ground=True):
        EcoObject.__init__(self, tile=tile, name=name, size=size, shade=shade, ground=ground)

class EcoTile(Tile):
    def __init__(self, tileType, maxSize=10, world=None, objects=set(), elevation=0):
        self.tileType=tileType #tile types: 0=dirt 1=sand 2=rock 3=dirt water 4=sand water, 5=rock water
        self.maxSize=maxSize
        self.tooBig=False
        self.newMoisture=0
        self.isWater=False
        if self.tileType>2 and self.tileType<6:
            self.moisture=1000000
            self.isWater=True
        else:
            self.moisture=0
        self.elevation=elevation
        Tile.__init__(self, world, objects)
    def setTileType(self, tileType):
        self.tileType=tileType
    def setMoisture(self, moisture):
        self.moisture+=moisture
    def setNewMoisture(self, moisture):
        self.newMoisture=moisture
    def addObject(self, object):
        if not (self.tooBig and object.getGround()):
            self.objects.add(object)
            self.calibrate()
    def turn(self):
        if self.isWater:
            if self.moisture<500000:
                self.tileType=self.tileType-3
                self.isWater=False
        else:
            if self.moisture>500000:
                self.tileType=self.tileType+3
                self.isWater=True
        self.evaporate()
        Tile.turn(self)
        self.moisture+=self.newMoisture
        self.newMoisture=0
    def calibrate(self):
        totalSize=0
        for i in self.objects:
            i.setTile(self)
            if i.getGround():
                totalSize+=i.getSize()
        if totalSize>self.maxSize:
            self.tooBig=True
    def evaporate(self):
        clouds=set()
        for i in self.objects:
            if type(i) is Cloud:
                clouds.add(i)
        cloudsize=0.0
        for i in clouds:
            self.removeObject(i)
            cloudsize+=i.getSize()
        if self.moisture>=1.0:
            cloudsize+=0.1
            self.moisture-=1.0
        self.addObject(Cloud(size=cloudsize))
    def getTileType(self):
        return self.tileType
    def getMaxSize(self):
        return self.maxSize
    def getMoisture(self):
        return self.moisture
    def getNewMoisture(self):
        return self.newMoisture
    def getIsWater(self):
        return self.isWater

class Ecosystem(World):
    def __init__(self, rows, cols, fill=EcoTile(0)):
        World.__init__(self, rows, cols, fill)
    def setTileType(self, row, col, tileType):
        self.world[row%self.rows][col%self.cols].setTileType(tileType)
    def setTileMoisture(self, row, col, moisture):
        self.world[row%self.rows][col%self.cols].setMoisture(moisture)
    def setTileNewMoisture(self, row, col, moisture):
        self.world[row%self.rows][col%self.cols].setNewMoisture(moisture)

#################################################
#################################################
#################################################
#################################################
############## ALL TEST CODE BELOW ##############
#################################################
#################################################
#################################################
#################################################


e=Ecosystem(10,10)
for r in range(int(e.getRows()/2)):
    for c in range(int(e.getCols()/2)):
        e.fillPos(r, c, EcoTile(1))
for r in range(int(e.getRows()/2), e.getRows()):
    for c in range(int(e.getCols()/2)):
        e.fillPos(r, c, EcoTile(2))
    for c in range(int(e.getCols()/2), e.getCols()):
        e.fillPos(r, c, EcoTile(3))
e.turn(times=5)

a=[]
for r in range(e.getRows()):
    a.append([])
    for c in range(e.getCols()):
        a[r].append(e.getWorld()[r][c].getMoisture())
b=[]
for r in range(e.getRows()):
    for c in range(e.getCols()):
        b.append(a[r][c])
print(str(sum(b)))
