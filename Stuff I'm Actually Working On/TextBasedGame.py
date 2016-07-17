from world2d import *

class RPGObject(Object):
    def __init__(self, tile=None, name="Object", pos=0, health=0, attack=0, defense=0, inventory=[]):
        Object.__init__(self, tile=tile, name=name, pos=pos)
        self.health=health
        self.defense=defense
        self.attack=attack
        self.inventory=inventory
    def setHealth(self, health):
        self.health=health
    def setDefense(self, defense):
        self.defense=defense
    def setAttack(self, attack):
        self.attack=attack
    def addToInventory(self, item):
        self.inventory.append(item)
    def removeFromInventory(self, index):
        self.inventory.pop(index)
    def getHealth(self):
        return self.health
    def getDefense(self):
        return self.defense
    def getAttack(self):
        return self.attack
    def getInventory(self):
        return self.inventory

class Enemy(RPGObject):
    def __init__(self, tile=None, name="Object", pos=0, health=0, defense=0, attack=0, inventory=[]):
        RPGObject.__init__(self, tile=tile, name=name, pos=pos, health=health, defense=defense, attack=attack, inventory=inventory)

class Player(RPGObject):
    def __init__(self, tile=None, name="Object", pos=0, health=0, defense=0, attack=0, inventory=[], level=1):
        RPGObject.__init__(self, tile=tile, name=name, pos=pos, health=health, defense=defense, attack=attack, inventory=inventory)
        self.level=level
    def setLevel(self, level):
        self.level=level
    def getLevel(self):
        return self.level

class Item(RPGObject):
    def __init__(self, tile=None, name="Object", pos=0, health=0, defense=0, attack=0, inventory=[]):
        RPGObject.__init__(self, tile=tile, name=name, pos=pos, health=health, defense=defense, attack=attack, inventory=inventory)

class Structure(RPGObject):
    def __init__(self, tile=None, name="Object", pos=0, health=0, defense=0, attack=0, inventory=[]):
        RPGObject.__init__(self, tile=tile, name=name, pos=pos, health=health, defense=defense, attack=attack, inventory=inventory)

class Equipment(Item):
    def __init__(self, tile=None, name="Object", pos=0, health=0, defense=0, attack=0, inventory=[]):
        Item.__init__(self, tile=tile, name=name, pos=pos, health=health, defense=defense, attack=attack, inventory=inventory)

class RPGTile(Tile):
    def __init__(self, world=None, objects=[], tileType=0):
        Tile.__init__(self, world=world, objects=objects)
        self.tileType=tileType #0 is grass(nothing special), 1 is water(most things can't go on it), 2 is void(nothing can go on it), 3 is poison(most things take damage while on it) I will implement this system later
    def setTileType(self, tileType):
        self.tileType=tileType
    def getTileType(self):
        return self.tileType

class RPGWorld(World):
    def __init__(self, rows, cols, fill=RPGTile(), player=Player(health=20, defense=0, attack=2), startPos=(0, 0)):
        World.__init__(self, rows, cols, fill=fill)
        self.player=player
        self.world[startPos[0]][startPos[1]].addObjectShallow(self.player)
        print("Commands: n, s, e, and w to move north south, east and west. Anything that is not a valid command will cause you to skip your turn.")
    def turn(self):
        print("What would you like to do?")
        command=input()
        if command=="n":
            self.player.moveNorth()
        elif command=="s":
            self.player.moveSouth()
        elif command=="e":
            self.player.moveEast()
        elif command=="w":
            self.player.moveWest()
        else:
            print("That is not a valid command.")
    def setTileType(self, r, c, tileType):
        self.world[r][c].setTileType(tileType)

world=RPGWorld(100,100)
while True:
    world.turn()
