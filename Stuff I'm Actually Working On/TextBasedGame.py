from world2d import *
import re

class RPGObject(Object):
    def __init__(self, tile=None, name="Object", maxhealth=0, attack=0, defense=0, inventory=[]):
        Object.__init__(self, tile=tile, name=name)
        self.maxhealth=maxhealth
        self.defense=defense
        self.attack=attack
        self.inventory=inventory
        self.health=maxhealth
    def setMaxHealth(self, maxhealth):
        self.maxhealth=maxhealth
    def damage(self, damage):
        self.health-=damage-self.defense
        print(self.name + " took " + str(damage) + " damage!")
        if self.health<=0:
            print(self.name + " died!")
            self.tile.removeObject(self)
        else:
            print(self.name + " now has " + str(self.health) + " health.")
    def heal(self, heal):
        print(self.name + " healed " + str(heal) + " health!")
        self.health+=heal
        if self.health>self.maxhealth:
            self.health=maxhealth
        print(self.name + " now has " + str(self.health) + " health.")
    def setDefense(self, defense):
        self.defense=defense
    def setAttack(self, attack):
        self.attack=attack
    def addToInventory(self, item):
        self.inventory.append(item)
    def removeFromInventory(self, index):
        self.inventory.pop(index)
    def getMaxHealth(self):
        return self.maxhealth
    def getHealth(self):
        return self.health
    def getDefense(self):
        return self.defense
    def getAttack(self):
        return self.attack
    def getInventory(self):
        return self.inventory

class Enemy(RPGObject):
    def __init__(self, tile=None, name="Slime", pos=0, maxhealth=20, defense=0, attack=2, inventory=[], exp=20):
        RPGObject.__init__(self, tile=tile, name=name, maxhealth=maxhealth, defense=defense, attack=attack, inventory=inventory)
        self.exp=exp
    def doAttack(self):
        target=None
        for i in self.tile.getObjects():
            if type(i)==Player:
                target=i
                break
        if target:
            print(self.name + " attacked " + target.getName() + "!")
            target.damage(self.attack)
    def turn(self):
        self.doAttack()
    def setExp(self, exp):
        self.exp=exp
    def getExp(self):
        return self.exp

class Player(RPGObject):
    def __init__(self, tile=None, name="You", pos=0, maxhealth=20, defense=0, attack=2, inventory=[], level=1, exp=0, equipment=set()):
        RPGObject.__init__(self, tile=tile, name=name, maxhealth=maxhealth, defense=defense, attack=attack, inventory=inventory)
        self.level=level
        self.exp=exp
        self.equipment=equipment
    def doAttack(self):
        targets=[]
        for i in self.tile.getObjects():
            targets.append(i)
        print("What would you like to attack? 0 to cancel. WARNING: CANCELLING WILL SKIP YOUR TURN")
        for i in range(len(targets)):
            print(str(i+1) + ". " + targets[i].getName() + ", Health: " + str(targets[i].getHealth()))
        targeti=input()
        isnumber = re.match(re.compile('^\d+$'), targeti)
        while (not isnumber) or int(targeti)>len(targets) or int(targeti)<0:
            print("That is not a valid target.")
            targeti=input()
            isnumber = re.match(re.compile('^\d+$'), targeti)
        if targeti==0:
            return
        target=targets[int(targeti)-1]
        print("You attacked " + target.getName() + "!")
        target.damage(self.attack)
        if target in self.tile.getShouldRemove():
            if type(target)==Enemy:
                self.gainExp(target.getExp())
    def turn(self):
        for i in self.tile.getObjects():
            if not i==self:
                print("There is " + i.getName() + " nearby with " + str(i.getHealth()) + " health.")
        commands=["n","s","e","w","a","x"]
        print("What would you like to do?")
        command=input()
        while not command in commands:
            print("That is not a valid command.")
            print("What would you like to do?")
            command=input()
        if command=="n":
            self.moveNorth()
            print("You moved north.")
        elif command=="s":
            self.moveSouth()
            print("You moved south.")
        elif command=="e":
            self.moveEast()
            print("You moved east.")
        elif command=="w":
            self.moveWest()
            print("You moved west.")
        elif command=="a":
            self.doAttack()
        elif command=="x":
            print("You skipped your turn")
    def levelUp(self):
        stats=["h","d","a"]
        self.level+=1
        print("You leveled up!")
        print("Which stat would you like to increase, max health, defense, or attack? Type h for max health, d for defense, and a for attack")
        stat=input()
        while not stat in stats:
            print("That is not a valid stat.")
            print("Which stat would you like to increase, max health, defense, or attack? Type h for max health, d for defense, and a for attack")
            stat=input()
        if stat=="h":
            self.maxhealth+=10
        elif stat=="a":
            self.attack+=1
        elif stat=="d":
            self.defense+=1
    def gainExp(self, exp):
        print("You gained " + str(exp) + " EXP!")
        self.exp+=exp
        while self.exp>=self.level*100:
            self.levelUp()
            self.exp-=self.level*100
    def addEquipment(self, equipment):
        self.equipment.add(equipment)
    def removeEquipment(self, equipment):
        if equipment in self.equipment:
            self.equipment.remove(equipment)
    def getLevel(self):
        return self.level
    def getExp(self):
        return self.exp
    def getEquipment(self):
        return self.exp

class Item(RPGObject):
    def __init__(self, tile=None, name="Potion", pos=0, maxhealth=1, defense=0, attack=0, inventory=[]):
        RPGObject.__init__(self, tile=tile, name=name, maxhealth=maxhealth, defense=defense, attack=attack, inventory=inventory)

class Structure(RPGObject):
    def __init__(self, tile=None, name="House", pos=0, maxhealth=100, defense=10, attack=0, inventory=[]):
        RPGObject.__init__(self, tile=tile, name=name, maxhealth=maxhealth, defense=defense, attack=attack, inventory=inventory)

class Equipment(Item):
    def __init__(self, tile=None, name="Sword", pos=0, maxhealth=1, defense=0, attack=0, inventory=[]):
        Item.__init__(self, tile=tile, name=name, maxhealth=maxhealth, defense=defense, attack=attack, inventory=inventory)

class RPGTile(Tile):
    def __init__(self, world=None, objects=set(), tileType=0):
        Tile.__init__(self, world=world, objects=objects)
        self.tileType=tileType #0 is grass(nothing special), 1 is water(most things can't go on it), 2 is void(nothing can go on it), 3 is poison(most things take damage while on it) I will implement this system later
    def setTileType(self, tileType):
        self.tileType=tileType
    def getTileType(self):
        return self.tileType

class RPGWorld(World):
    def __init__(self, rows, cols, fill=RPGTile(), player=Player(), startPos=(0, 0)):
        World.__init__(self, rows, cols, fill=fill)
        self.player=player
        self.world[startPos[0]][startPos[1]].addObjectShallow(self.player)
        print("Commands: n, s, e, and w to move north south, east and west. a to attack. x to skip your turn.")
    def setTileType(self, r, c, tileType):
        self.world[r][c].setTileType(tileType)

world=RPGWorld(100,100)
world.addObjectToTile(Enemy(), 0, 0)
while True:
    world.turn()
