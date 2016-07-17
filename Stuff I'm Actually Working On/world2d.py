import copy

class Object:
    def __init__(self, tile=None, name="Object", pos=0):
        self.tile=tile
        self.name=name
        self.pos=pos
    def setTile(self, tile):
        self.tile=tile
    def setName(self, name):
        self.name=name
    def setSize(self, size):
        self.size=size
    def setPos(self, pos):
        self.pos=pos
    def turn(self):
        pass
    def moveNorth(self):
        self.tile.removeObject(self.pos)
        self.tile.getWorld().getPos(self.tile.getPos()[0]-1, self.tile.getPos()[1]).addObject(self)
    def moveSouth(self):
        self.tile.removeObject(self.pos)
        self.tile.getWorld().getPos(self.tile.getPos()[0]+1, self.tile.getPos()[1]).addObject(self)
    def moveEast(self):
        for i in range(len(self.tile.getObjects())):
            if self.tile.getObjects()[i]==self:
                self.tile.removeObject(self.pos)
                break
        self.tile.getWorld().getPos(self.tile.getPos()[0], self.tile.getPos()[1]+1).addObject(self)
    def moveWest(self):
        self.tile.removeObject(self.pos)
        self.tile.getWorld().getPos(self.tile.getPos()[0], self.tile.getPos()[1]-1).addObject(self)
    def getTile(self):
        return self.tile
    def getName(self):
        return self.name
    def getSize(self):
        return self.size
    def getPos(self):
        return self.pos

class Tile:
    def __init__(self, world=None, objects=[]):
        self.world=world
        self.objects=objects
        self.pos=(0,0)
        self.calibrate()
    def setPos(self, row, col):
        self.pos=(row,col)
        self.calibrate()
    def setWorld(self, world):
        self.world=world
        self.calibrate()
    def turn(self):
        for i in range(len(self.objects)):
            self.objects[i].turn()
        self.calibrate()
    def addObject(self, obj):
        self.objects.append(copy.deepcopy(obj))
        self.calibrate()
    def removeObject(self, pos):
        self.objects.pop(pos)
        self.calibrate()
    def calibrate(self):
        for i in range(len(self.objects)):
            self.objects[i].setTile(self)
            self.objects[i].setPos(i)
    def getWorld(self):
        return self.world
    def getPos(self):
        return self.pos
    def getObjects(self):
        return self.objects

class World:
    def __init__(self, rows, cols, fill=Tile()):
        self.rows=rows
        self.cols=cols
        self.world=[[copy.deepcopy(fill) for i in range(self.cols)] for j in range(self.rows)]
        self.calibrate()
    def fill(self, fill):
        self.world=[[copy.deepcopy(fill) for i in range(self.cols)] for j in range(self.rows)]
        self.calibrate()
    def fillPos(self, row, col, fill):
        self.world[row%self.rows][col%self.cols]=copy.deepcopy(fill)
        self.calibrate()
    def delRow(self, row):
        self.world.pop(row%self.rows)
        self.calibrate()
    def delCol(self, col):
        for i in range(self.rows):
            self.world[i].pop(col%self.cols)
        self.calibrate()
    def addRow(self, fill=Tile()):
        self.world.append([copy.deepcopy(fill) for i in range(self.cols)])
        self.calibrate()
    def addCol(self, fill=Tile()):
        for i in range(self.rows):
            self.world[i].append(copy.deepcopy(fill))
        self.calibrate()
    def calibrate(self):
        self.rows=len(self.world)
        self.cols=len(self.world[0])
        for r in range(self.rows):
            for c in range(self.cols):
                self.world[r][c].setPos(r,c)
                self.world[r][c].setWorld(self)
    def turn(self, times=1):
        for i in range(times):
            for r in range(self.rows):
                for c in range(self.cols):
                    self.world[r][c].turn()
        self.calibrate()
    def addObjectToTile(self, obj, row, col):
        self.world[row%self.rows][col%self.cols].addObject(copy.deepcopy(obj))
        self.calibrate()
    def removeObjectFromTile(self, pos,row, col):
        self.world[row][col].removeObject(pos)
        self.calibrate()
    def swap(self, r1, c1, r2, c2):
        temp=self.world[r2%self.rows][c2%self.cols]
        self.world[r2%self.rows][c2%self.cols]=self.world[r1%self.rows][c1%self.cols]
        self.world[r1%self.rows][c1%self.cols]=temp
        self.calibrate()
    def getWorld(self):
        return self.world
    def getPos(self, row, col):
        return self.world[row%self.rows][col%self.cols]
    def getRows(self):
        return self.rows
    def getCols(self):
        return self.cols
