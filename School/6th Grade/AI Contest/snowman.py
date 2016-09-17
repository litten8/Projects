# a simple AI to play Jigga-Jigga

import random

def ai(arr):
    
    for j in range(0,30):
        x = random.randint(0,9)
        y = random.randint(0,9)
        if arr[x][y] == 0:
            return [x,y]

    for j in range(0,100):
        x = j%10
        y = j/10
        if arr[x][y] == 0:
            return [x,y]
