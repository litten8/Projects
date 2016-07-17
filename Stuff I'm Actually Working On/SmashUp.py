import random
import copy
class Card:
    def __init__(self, name, faction, owner=None):
        self.name=name
        self.faction=faction
        self.owner=owner
        self.controller=owner
        self.base=None
    def discard(self):
        if self in self.controller.getHand():
            for i in range(len(self.controller.getHand())):
                if self.controller.getHand()[i]==self:
                    self.controller.removeFromHand(i)
                    break
        if self in self.controller.getDeck():
            for i in range(len(self.controller.getDeck())):
                if self.controller.getDeck()[i]==self:
                    self.controller.removeFromDeck(i)
                    break
        if self.base != None:
            if self in self.base.getMinions():
                for i in range(len(self.base.getMinions())):
                    if self.base.getMinions()[i]==self:
                        self.base.removeMinion(i)
                        break
            elif self in self.base.getActions():
                for i in range(len(self.base.getActions())):
                    if self.base.getActions()[i]==self:
                        self.base.removeAction(i)
                        break
        self.controller.addToDiscard(self)
        print(self.name + " has been discarded to " + self.controller.getName() + "'s discard pile.")
    def setOwner(self, owner):
        self.owner=owner
        self.controller=owner
    def setController(self, controller):
        self.controller=controller
    def setBase(self, base):
        self.base=base
    def getName(self):
        return self.name
    def getFaction(self):
        return self.faction
    def getOwner(self):
        return self.owner
    def getController(self):
        return self.controller
    def getBase(self):
        return self.base
class Action(Card):
    def __init__(self, name, faction, owner):
        Card.__init__(self, name, faction, owner)
        self.minion=None
    def action(self):
        pass
    def discard(self):
        Card.discard(self)
        if self.minion:
            for i in range(len(self.minion.getActions())):
                if self.minion.getActions()[i]==self:
                    self.minion.removeAction(i)
                    break
            self.minion=None
    def setMinion(self, minion):
        self.minion=minion
        if minion:
            self.minion.addAction(self)
    def getMinion(self):
        return self.minion
class Minion(Card):
    def __init__(self, name, faction, owner, power):
        Card.__init__(self, name, faction, owner)
        self.power=power
        self.actions=[]
    def action(self):
        pass
    def discard(self):
        Card.discard(self)
        for i in range(len(actions)):
            self.actions[0].discard()
    def setPower(self, power):
        self.power=power
    def addAction(self, action):
        self.actions.append(action)
    def removeAction(self, index):
        self.actions.pop(index)
    def getPower(self):
        return self.power
    def getActions(self):
        return self.actions
class Base:
    def __init__(self, name, rewards, breakpoint, monsters=0):
        self.name=name
        self.rewards=rewards
        self.breakpoint=breakpoint
        self.monsters=monsters
        self.actions=[]
        self.minions=[]
    def checkForScore(self):
        totalpower=0
        for i in range(len(self.minions)):
            totalpower+=self.minions[i]
        if totalpower>=self.breakpoint:
            for i in range(len(self.actions)):
                self.actions[i].discard()
            for i in range(len(self.minions)):
                self.minions[i].discard()
    def setName(self, name):
        self.name=name
    def setFirstReward(self, reward):
        self.rewards[0]=reward
    def setSecondReward(self, reward):
        self.rewards[1]=reward
    def setThirdReward(self, reward):
        self.rewards[2]=reward
    def setBreakpoint(self, breakpoint):
        self.breakpoint=breakpoint
    def setMonsters(self, monsters):
        self.monsters=monsters
    def addAction(self, action):
        self.actions.append(actions)
    def removeAction(self, index):
        self.actions.pop(index)
    def addMinion(self, minion):
        self.minions.append(minion)
    def removeMinion(self, index):
        self.minions.pop(index)
    def getName(self):
        return self.name
    def getBreakpoint(self):
        return self.breakpoint
    def getRewards(self):
        return self.rewards
    def getMonsters(self):
        return self.monsters
    def getActions(self):
        return self.actions
    def getMinions(self):
        return self.minions
class Faction:
    def __init__(self, name, deck):
        self.name=name
        self.deck=deck
    def setName(self, name):
        self.name=name
    def addToDeck(self, card, n=1):
        for i in range(n):
            self.deck.append(card)
    def removeFromDeck(self, index):
        self.deck.pop(index)
    def getName(self):
        return self.name
    def getDeck(self):
        return self.deck
class Player:
    def __init__(self, factions, name):
        self.factions=factions
        self.deck=[]
        for i in range(len(self.factions)):
            self.deck=self.deck+self.factions[i]
        random.shuffle(self.deck)
        self.discard=[]
        self.hand=[]
        self.vp=0
        self.name=name
    def draw(self, cards):
        for i in range(cards):
            if len(self.deck)<1:
                self.deck=self.discard
                self.discard=[]
                random.shuffle(self.deck)
            if len(self.deck)>0:
                print("You drew " + self.deck[0].getName() + ".")
                self.hand.append(self.deck[0])
                self.deck.pop(0)
    def addToDeck(self, card):
        self.deck.append(card)
    def removeFromDeck(self, index):
        self.deck.pop(index)
    def addToDiscard(self, card):
        self.discard.append(card)
    def removeFromDiscard(self, index):
        self.discard.pop(index)
    def addToHand(self, card):
        self.hand.append(card)
    def removeFromHand(self, index):
        self.hand.pop(index)
    def setVP(self, vp):
        self.vp=vp
    def setName(self, name):
        self.name=name
    def getFactions(self):
        return self.factions
    def getDeck(self):
        return self.deck
    def getDiscard(self):
        return self.discard
    def getHand(self):
        return self.hand
    def getVP(self):
        return self.vp
    def getName(self):
        return self.name
