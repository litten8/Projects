import random

d = {}
for i in range(36):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    rollpower = roll1**roll2
    d[rollpower] = d.get(rollpower, 0) + 1
        
for key, value in d.items():
    print (str(key) + " occurred " + str(value) + " times ")
