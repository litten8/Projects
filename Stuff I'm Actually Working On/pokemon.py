import random

def target(arena, params, action, name):
        movecommand=""
        z=0
        while movecommand!="cancel":
            print(arena.toString(z))
            movecommand=input()
            if movecommand=="help":
                print("- means an empty space")
                print("P means there is a pokemon")
                print("V means there is a projectile")
                print("type up to look higher")
                print("type down to look lower")
                print("type back to go back to the main screen")
                print("type " + action + " to " + action + " to a location")
            elif movecommand=="up":
                z+=1
                if z>=arena.height:
                    z-=1
            elif movecommand=="down":
                z-=1
                if z<0:
                    z+=1
            elif movecommand==action:
                print("to what x position would you like to " + action + "?")
                x=input()
                if not x.isdigit():
                    print("that is not a number")
                    continue
                x=int(x)
                print("to what y position would you like to " + action + "?")
                y=input()
                if not y.isdigit():
                    print("that is not a number")
                    continue
                y=int(y)
                print("to what z position would you like to " + action + "?")
                nz=input()
                if not nz.isdigit():
                    print("that is not a number")
                    continue
                nz=int(nz)
                if x>params[0][1] or x<params[0][0] or y>params[1][1] or y<params[1][0] or z>params[2][1] or z<params[2][0]:
                    print(name + " can't " + action + " that far away")
                elif nz>=arena.height or nz<0 or y>=arena.length or y<0 or x>=arena.width or x<0:
                    print("that position is not on the arena")
                else:
                    return (x,y,nz)
                    break

class Pokemon:
    def __init__(self, types, moves, movenames, ability, arena, x=0, y=0, z=0, size=1, weight=10, atk=10, sat=10, dfs=10, sdf=10, mhp=20, speed=2, jump=3, fly=False, acc=1, level=1, name="Pokemon",phys=True):
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
        self.speed=speed
        self.jump=jump
        self.fly=fly
        self.level=level
        self.name=name
        self.fainted=False
        self.phys=phys
        self.effects=[]
    def useMove(self, i):
        self.moves[i](self)
    def damage(self, damage, phys, types):
        if phys:
            self.hp=self.hp-((damage/(self.dfs/10))*self.types.matchup(types))
        else:
            self.hp=self.hp-((damage/(self.sdf/10))*self.types.matchup(types))
        if self.types.matchup(types)==0:
            print("It had no effect")
        elif self.types.matchup(types)<1:
            print("It's not very effective")
        elif self.types.matchup(types)>1:
            print("It's super effective")
        print(self.name + " took " + str((damage/(self.dfs/10))*self.types.matchup(types)) + " damage")
        self.deathCheck()
    def directDamage(self, damage):
        self.hp=self.hp-damage
        self.deathCheck()
    def deathCheck(self):
        if self.hp<1:
            print(self.name + " fainted")
            self.arena.removeObject(self, self.x, self.y, self.z)
            self.fainted=True
    def checkAttack(self, phys):
        if phys:
            return(self.atk)
        else:
            return(self.sat)
    def AITurn(self):
        if not self.fainted:
            self.usedMove=False
            if self.z>0 and not self.fly:
                gravity=True
                for o in self.arena.getArenaPos(self.x,self.y,self.z-1):
                    if o.phys:
                        gravity=False
                if gravity:
                    self.arena.move(self, self.x, self.y, self.z, self.x, self.y, self.z-1)
                    self.z-=1
            for i in range(len(self.effects)):
                effects=self.effects
                effects[i](self)
    def playerTurn(self):
        if not self.fainted:
            command=""
            self.usedMove=False
            if self.z>0 and not self.fly:
                gravity=True
                for o in self.arena.getArenaPos(self.x,self.y,self.z-1):
                    if o.phys:
                        gravity=False
                if gravity:
                    self.arena.move(self, self.x, self.y, self.z, self.x, self.y, self.z-1)
                    self.z-=1
            for i in range(len(self.effects)):
                effects=self.effects
                effects[i](self)
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
                    t=target(self.arena, ((0,self.arena.width),(0,self.arena.length),(0,self.arena.height)), "target", self.name)
                    if not t==None:
                        x,y,z=t
                        self.arena.tileInfo(x,y,z)
                elif command!="end":
                    print("that is not a valid command")
    def getName(self):
        return self.name
    def getHp(self):
        return self.hp

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
        return multiplier
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
    def removeObject(self, o, x, y, z):
        self.arena[x][y][z].remove(o)
    def move(self, o, x1, y1, z1, x2, y2, z2):
        if x1>=0 and x1<self.width and y1>=0 and y1<self.length and z1>=0 and z1<self.height and x2>=0 and x2<self.width and y2>=0 and y2<self.length and z2>=0 and z2<self.height:
            self.arena[x1][y1][z1].remove(o)
            self.arena[x2][y2][z2].add(o)
            return True
        else:
            return False
            #print("can't move, either " + str(x1) + ", " + str(y1) + ", " + str(z1) + " or " + str(x2) + ", " + str(y2) + ", " + str(z2) + " is off the screen")
    def toString(self, z):
        if z<self.height:
            returns=""
            for x in range(self.width):
                line=""
                for y in range(self.height):
                    for o in self.arena[x][y][z]:
                        if type(o)==Pokemon:
                            line+=o.name[0]
                            break
                        elif type(o)==Projectile:
                            line+="^"
                            break
                    if len(self.arena[x][y][z])==0:
                        line+="-"
                returns+=line+"\n"
            return returns
        return "That is above the arena"
    def tileInfo(self, x, y, z):
        print("The following objects are in this tile:")
        for o in self.arena[x][y][z]:
            print(o.getName() + " with " + str(o.getHp()) + " HP")
    def getArenaPos(self,x,y,z):
        if x>=self.width or y>=self.length or z>=self.height or x<0 or y<0 or z<0:
            return ()
        else:
            return self.arena[x][y][z]

class Projectile:
    def __init__(self, arena, x, y, z, turn, types, phys=True, hp=1, name="Projectile"):
        self.arena=arena
        self.x=x
        self.y=y
        self.z=z
        self.arena.addObject(self, self.x, self.y, self.z)
        self.turn=turn
        self.types=types
        self.phys=phys
        self.hp=hp
        self.name=name
    def damage(self, damage, phys, types):
        self.hp-=damage*self.types.matchup(types)
        self.deathCheck()
    def directDamage(self, damage):
        self.hp=self.hp-damage
        self.deathCheck()
    def deathCheck(self):
        if self.hp<1:
            self.arena.removeObject(self, self.x, self.y, self.z)
            self.fainted=True
    def doTurn(self, poke):
        self.turn(self, poke)
    def getHp(self):
        return self.hp
    def getName(self):
        return self.name

class Ability:
    pass

def move(poke):
    t = target(poke.arena, ((poke.x-poke.speed, poke.x+poke.speed), (poke.y-poke.speed, poke.y+poke.speed), (poke.z-poke.jump, poke.z+poke.jump)), "move", poke.name)
    if t==None:
        return
    x,y,z=t
    print(poke.name + " has moved to " + str(x) + ", " + str(y) + ", " + str(z))
    poke.arena.move(poke, poke.x, poke.y, poke.z, x, y, z)
    poke.x=x
    poke.y=y
    poke.z=z

def instantrangedattack(poke, name, radius, effects, params):
    t=target(poke.arena, ((poke.x-radius,poke.x+radius),(poke.y-radius,poke.y+radius),(poke.z-radius,poke.z+radius)), "attack", poke.name)
    if t==None:
        return
    x,y,z=t
    print("The following objects are in that tile:")
    pokestoattack=[]
    i=0
    for o in poke.arena.getArenaPos(x,y,z):
        print(str(i) + ". " + o.getName() + " with " + str(o.getHp()) + " HP")
        i+=1
        pokestoattack.append(o)
    print("enter the number before a pokemon to attack it")
    poketoattack=pokestoattack[int(input())]
    print(poke.name + " used " + name +"!")
    for i in range(len(effects)):
        effects[i](poketoattack, params[i])

def projectilerangedattackturn(poke, poke2):
    if poke.dead:
        return
    if poke.z>0 and not poke.fly:
        gravity=True
        for o in poke.arena.getArenaPos(poke.x,poke.y,poke.z-1):
            if o.phys:
                gravity=False
        if gravity:
            poke.arena.move(poke, poke.x, poke.y, poke.z, poke.x, poke.y, poke.z-1)
            poke.z-=1
    for i in range(poke.speed):
        if poke.dead:
            return
        poke.t += 1
        if poke.t == poke.turns:
            poke.arena.move(poke, poke.x, poke.y, poke.z, poke.targetx, poke.targety, poke.targetz)
            poke.x=poke.targetx
            poke.y=poke.targety
            poke.z=poke.targetz
        else:
            x=round(poke.startx+poke.t*poke.vx)
            y=round(poke.starty+poke.t*poke.vy)
            z=round(poke.startz+poke.t*poke.vz)
            w=poke.arena.move(poke, poke.x, poke.y, poke.z, x, y, z)
            if w:
                poke.x=x
                poke.y=y
                poke.z=z
            else:
                poke.arena.removeObject(poke, poke.x, poke.y, poke.z)
                poke.dead=True
                targetpokes=[]
                for x in range(poke.x-(poke.radius-1), poke.x+poke.radius):
                    for y in range(poke.y-(poke.radius-1), poke.y+poke.radius):
                        for z in range(poke.z-(poke.radius-1), poke.z+poke.radius):
                            for o in poke.arena.getArenaPos(x,y,z):
                                targetpokes.append(o)
                for o in targetpokes:
                    for i in range(len(poke.effects)):
                        if not (not poke.affectuser and o==poke2):
                            poke.effects[i](o, poke.params[i])
        if poke.t<2:
            continue
        targetpokes=[]
        for x in range(poke.x-(poke.radius-1), poke.x+poke.radius):
            for y in range(poke.y-(poke.radius-1), poke.y+poke.radius):
                for z in range(poke.z-(poke.radius-1), poke.z+poke.radius):
                    for o in poke.arena.getArenaPos(x,y,z):
                        if not o==poke:
                            targetpokes.append(o)
        if poke2 in targetpokes:
            testgreater=1
        else:
            testgreater=0
        if len(targetpokes)>testgreater:
            poke.arena.removeObject(poke, poke.x, poke.y, poke.z)
            poke.dead=True
            for o in targetpokes:
                for i in range(len(poke.effects)):
                    if not (not poke.affectuser and o==poke2):
                        poke.effects[i](o, poke.params[i])

def projectilerangedattack(pparams, poke, name, effects, params, affectuser=True):
    t=target(poke.arena, ((0,poke.arena.width),(0,poke.arena.length),(0,poke.arena.height)), "attack", poke.name)
    if t==None:
        return
    x,y,z=t
    speed,types,hp,phys,radius,fly,name=pparams
    p=Projectile(poke.arena, poke.x, poke.y, poke.z, projectilerangedattackturn, types, phys=phys, hp=hp,name=name)
    poke.effects.append(p.doTurn)
    p.speed=speed
    p.radius=radius
    p.effects=effects
    p.params=params
    p.dead=False
    p.atk=poke.atk
    p.affectuser=affectuser
    p.fly=fly

    p.startx=p.x
    p.starty=p.y
    p.startz=p.z

    p.targetx=x
    p.targety=y
    p.targetz=z

    a = p.targetx - p.startx
    b = p.targety - p.starty
    c = p.targetz - p.startz

    dist = (a*a + b*b + c*c)**0.5

    p.turns = dist
    p.turns=round(p.turns)
    if p.turns<1:
        p.turns=1
    p.t = 0

    a = abs(p.targetx - p.startx)
    b = abs(p.targety - p.starty)
    c = abs(p.targetz - p.startz)
    abc = a+b+c

    if p.targetx - p.startx > 0:
        sa = 1
    else:
        sa = -1
    if p.targety - p.starty > 0:
        sb = 1
    else:
        sb = -1
    if p.targetz - p.startz > 0:
        sc = 1
    else:
        sc = -1

    p.vx=sa * a / abc
    p.vy=sb * b / abc
    p.vz=sc * c / abc
    p.doTurn(poke)

def changestat(poke, params):
    stat,change,types=params
    if poke.types.matchup(types)>0:
        exec("poke." + stat + "+=" + str(change))
        print(poke.name + "'s " + str(stat) + " changed by " + str(change))

def flinch(poke):
    poke.usedMove=True
    print(poke.name+" flinched!")
    for i in range(len(poke.effects)):
        if poke.effects[i]==flinchEffect:
            poke.effects.pop(i)

def flinchChance(poke, params):
    if random.randint(1,100)<=params[0] and poke.types.matchup(params[1])>0:
        poke.effects.append(flinchEffect)

def attackdamage(poke, params):
    types,damage,phys=params
    poke.damage(damage*poke.atk,phys,types)

##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################

def flamethrower(poke):
    projectilerangedattack((10,Types(["fire"]),100,False,1,True,"Flamethrower"), poke, "flamethrower",  [attackdamage], [(Types(["fire"]), 2, True)])

def crunch(poke):
    instantrangedattack(poke, "crunch", 1, [attackdamage, changestat, changestat], ((Types(["dark","normal"]), 3, True), ("dfs", -1,Types(["dark","normal"])), ("sdf", -1,Types(["dark","normal"]))))

def extremespeed(poke):
    print("you may move before you use extremespeed")
    move(poke)
    instantrangedattack(poke, "extremespeed", 1, [attackdamage], ((Types(["normal"]), 2, True)))

def growl(poke):
    projectilerangedattack((10,Types(["normal"]),100,False,10,True,"Growl"), poke, "growl",  [changestat], [("atk", -5,Types(["normal"]))],affectuser=False)

def shadowsneak(poke):
    print("you may move before you use shadow sneak")
    move(poke)
    instantrangedattack(poke, "shadow sneak", 1, [attackdamage], ((Types(["ghost"]), 2, True)))

def shadowpunch(poke):
    instantrangedattack(poke, "shadow punch", 1, [attackdamage], ((Types(["ghost", "fighting"]), 3, True)))

def shadowball(poke):
    projectilerangedattack((3,Types(["ghost"]),100,True,2,False,"Shadow Ball"), poke, "shadow ball",  [attackdamage], [(Types(["ghost"]), 3, False)])

def willowisp(poke):
    projectilerangedattack((3,Types(["ghost","fire"]),100,False,2,True,"Will-o-Wisps"), poke, "will-o-wisp",  [attackdamage for i in range(8)], [(Types(["ghost","fire"]), 0.25, True) for i in range(8)])

a=Arena(10,10,10)
torracat=Pokemon(Types(["fire"]),[move, flamethrower, crunch, extremespeed, growl],["move", "flamethrower", "crunch", "extremespeed", "growl"],None,a,x=5,y=0,z=0,name="Torracat", atk=20, dfs=15, speed=3, sat=15, sdf=10, mhp=60)
dusclops=Pokemon(Types(["ghost"]),[move, shadowball, shadowpunch, shadowsneak, willowisp],["move", "shadow ball", "shadow punch", "shadow sneak", "will-o-wisp"],None,a,x=5,y=9,z=0,name="Dusclops", fly=True, jump=2, atk=20, dfs=20, sat=20, sdf=20, mhp=70)
while True:
    torracat.playerTurn()
    dusclops.playerTurn()
    if torracat.fainted:
        print("dusclops wins!")
        break
    if dusclops.fainted:
        print("torracat wins!")
        break
