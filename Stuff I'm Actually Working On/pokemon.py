class Pokemon:
    def __init__(self, types, moves, movenames, ability, arena, x=0, y=0, z=0, size=1, weight=10, atk=10, sat=10, dfs=10, sdf=10, mhp=20, spd=1, jump=1, fly=False, acc=1, level=1, name="Pokemon"):
        self.types=types
        self.moves=moves
        self.movenames=movenames
        self.ability=ability
        self.arena=arena
        self.x=x
        self.y=y
        self.z=z
        self.arena.addObject(self, self.x, self.y, self.z)
        self.size=size
        self.weight=weight
        self.atk=atk
        self.sat=sat
        self.dfs=dfs
        self.sdf=sdf
        self.mhp=mhp
        self.hp=mhp
        self.spd=spd
        self.jump=jump
        self.fly=fly
        self.level=level
        self.name=name
    def useMove(self, i):
        self.moves[i](self)
    def damage(self, damage, phys, types):
        if phys:
            self.hp=self.hp-((damage-self.dfs)*self.types.matchup(types))
        else:
            self.hp=self.hp-((damage-self.sdf)*self.types.matchup(types))
        self.arena.abilityCheck("damage")
    def directDamage(self, damage):
        self.hp=self.hp-damage
        self.ability.abilityCheck("damage")
    def moveTo(x,y,z):
        self.arena.move(self, self.x, self.y, self.z, x, y, z)
    def checkAttack(self, phys):
        if phys:
            return(self.atk)
        else:
            return(self.sat)
    def AITurn(self):
        pass
    def playerTurn(self):
        command=""
        self.usedMove=False
        while command!="end":
            print("what will " + self.name + " do? (type help for help anytime)")
            command=input()
            if command=="help":
                print("move: use a move")
                print("info: find info on pokemon, the arena, or projectiles")
                print("switch: switch to a different pokemon")
                print("bag: use an item in your bag")
                print("end: end your turn")
            elif command=="move":
                if not self.usedMove:
                    movei=""
                    while movei!="cancel":
                        print("what move would you like to use?")
                        for i in range(len(self.movenames)):
                            print(str(i+1) + ": " + self.movenames[i])
                        movei=input()
                        if movei.isdigit():
                            movei=int(movei)
                            if movei>=1 and movei<=len(self.moves):
                                self.useMove(movei-1)
                                self.usedMove=True
                                break
                            else:
                                print("that number is not valid")
                        elif movei=="help":
                            print("type the number before a move to use it")
                            print("type cancel to go back to the main screen")
                        elif movei!="cancel":
                            print("that isn't even a number")
                else:
                    print("your pokemon can only use one move per turn")
            elif command=="info":
                infocommand=""
                z=0
                while infocommand!="back":
                    print(self.arena.toString(z))
                    infocommand=input()
                    if infocommand=="help":
                        print("- means an empty space")
                        print("P means there is a pokemon")
                        print("V means there is a projectile")
                        print("type up to look higher")
                        print("type down to look lower")
                        print("type back to go back to the main screen")
                        print("type target to target a specific location to get info on")
                    elif infocommand=="up":
                        z+=1
                        if z>=self.arena.height:
                            z-=1
                    elif infocommand=="down":
                        z-=1
                        if z<0:
                            z+=1
                    elif infocommand=="target":
                        print("what x position would you like to target?")
                        x=input()
                        print("what y position would you like to target?")
                        y=input()
                        self.arena.tileInfo(x,y,z)
            else:
                print("that is not a valid command")

class Types:
    def __init__(self, types):
        self.types=types
    def matchup(self,attacker):
        multiplier=1
        for i in self.types:
            for j in attacker.getTypes():
                if i=="fire" and j=="ground":
                    multiplier*=2
                if i=="fire" and j=="rock":
                    multiplier*=2
                if i=="fire" and j=="water":
                    multiplier*=2
                if i=="fire" and j=="bug":
                    multiplier/=2
                if i=="fire" and j=="steel":
                    multiplier/=2
                if i=="fire" and j=="fire":
                    multiplier/=2
                if i=="fire" and j=="grass":
                    multiplier/=2
                if i=="fire" and j=="ice":
                    multiplier/=2
                if i=="fire" and j=="fairy":
                    multiplier/=2
                if i=="ghost" and j=="normal":
                    multiplier*=0
                if i=="ghost" and j=="fighting":
                    multiplier*=0
                if i=="ghost" and j=="poison":
                    multiplier/=2
                if i=="ghost" and j=="bug":
                    multiplier/=2
                if i=="ghost" and j=="ghost":
                    multiplier*=2
                if i=="ghost" and j=="dark":
                    multiplier*=2
    def getTypes(self):
        return self.types

class Arena:
    def __init__(self, width, height, length):
        self.width=width
        self.height=height
        self.length=length
        self.arena=[[[set() for k in range(self.height)] for j in range(self.length)] for i in range(self.width)]
    def addObject(self, o, x, y, z):
        self.arena[x][y][z].add(o)
    def move(self, o, x1, y1, z1, x2, y2, z2):
        self.arena[x1][y1][z1].remove(o)
        self.arena[x2][y2][z2].add(o)
    def toString(self, z):
        returns=""
        for x in range(self.width):
            line=""
            for y in range(self.height):
                for o in self.arena[x][y][z]:
                    if type(o)==Pokemon:
                        line+="P"
                        break
                    elif type(o)==Projectile:
                        line+="V"
                        break
                if len(self.arena[x][y][z])==0:
                    line+="-"
            returns+=line+"\n"
        return returns
    def tileInfo(self, x, y, z):
        

class Projectile:
    pass

class Ability:
    pass

##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################

def move(poke):
    pass

a=Arena(10,10,10)
torracat=Pokemon(Types("fire"),[move],["move"],None,a,x=5,y=5,name="Torracat")
torracat.playerTurn()
