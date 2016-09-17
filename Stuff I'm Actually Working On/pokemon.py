class Pokemon:
    def __init__(self, types, moves, ability, arena, x=0, y=0, z=0, size=1, weight=10, atk=10, sat=10, dfs=10, sdf=10, mhp=20, spd=1, acc=1):
        self.types=types
        self.moves=moves
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
    def useMove(i):
        self.moves[i]()
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
        self.arena.move(self.x, self.y, self.z, x, y, z, delay=speed+x+y+z)
    def checkAttack(self, phys):
        if phys:
            return(self.atk)
        else:
            return(self.sat)

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
        arena=[[[set() for k in range(length)] for j in range(height)] for i in range(width)]
    def addObject(self, object):


class Projectile:
    pass

class Ability:
    pass
