from random import *
from time import *
class TalkingDoll:
    def __init__(self, phrase):
        self.phrase = phrase
    def speak(self):
        print(self.phrase)
class RandomTalkingDoll:
    def __init__(self, phrases):
        self.phrases = phrases
    def speak(self):
        print(choice(self.phrases))
class CycleTalkingDoll:
    def __init__ (self, phrases):
        self.phrases = phrases
        self.cycle = 0
    def speak(self):
        self.cycle = self.cycle + 1
        print(self.phrases[self.cycle%len(self.phrases)])
class BatteryTalkingDoll:
    def __init__ (self, phrase, timestotalk):
        self.phrase = phrase
        self.timestalked = 0
        self.timestotalk = timestotalk
    def speak(self):
        if self.timestalked <= self.timestotalk:
            print(self.phrase)
            self.timestalked += 1
        else:
            print("Out of Power. Please Recharge.")
    def recharge(self):
        print("Recharging...")
        sleep(5)
        self.timestalked = 0
        print("Recharged!")

x = TalkingDoll("Oh No!")
x.speak()
x.speak()
x.speak()
x.speak()
x.speak()
x.speak()
x.speak()
y = RandomTalkingDoll(["Meow!", "Purr...", "Hiss!"])
y.speak()
y.speak()
y.speak()
y.speak()
y.speak()
y.speak()
y.speak()
z = CycleTalkingDoll(["I Agree!", "Pure Genius!", "How Do You Do It?"])
z.speak()
z.speak()
z.speak()
z.speak()
z.speak()
z.speak()
z.speak()
a = BatteryTalkingDoll("Oh No!", 6)
a.speak()
a.speak()
a.speak()
a.speak()
a.speak()
a.speak()
a.speak()
a.speak()
a.recharge()
a.speak()
