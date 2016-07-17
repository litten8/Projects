import random
import copy
import math

def score(x, y, arr):
    if arr[y][x] == 0:
        score = what_if(arr, 1, x, y)
        return score
    else:
        return -1

def what_if(aa, val, x, y):
    arr = copy.deepcopy(aa)
    arr[y][x] = val;

    for yy in range(0, len(arr)):
        for xx in range(0, len(arr[0])):
            # if this rectangle has four corners equal to val...
            if (yy != y and xx != x and arr[yy][xx] == val and arr[yy][x] == val and arr[y][xx] == val):
                startx = min(x, xx)
                starty = min(y, yy)
                endx = max(x, xx) + 1
                endy = max(y, yy) + 1

                # flip all the filled entries to val
                for yyy in range(starty, endy):
                    for xxx in range(startx, endx):
                        if (arr[yyy][xxx] != 0):
                            arr[yyy][xxx] = val

    # see how many entries are my val
    score = 0
    for yy in range(0, len(arr)):
        for xx in range(0, len(arr[0])):
            if (arr[yy][xx] == val):
                score = score + 1

    # tiebreaker - how far to walk from the middle of the board to the square we are filling in
    # not regular distance, but left/right + up/down distance
    walking = math.fabs(y - len(arr) / 2) / len(arr) + math.fabs(x - len(arr[0]) / 2) / len(arr[0])

    score = score + walking

    return score

def ai(arr):
    ascore = 0
    max_x = -1
    max_y = -1
    max_score = -1
    for y in range(0, len(arr)):
        for x in range(0, len(arr[0])):
            ascore = score(x, y, arr)
            if ascore >= max_score:
                max_score = ascore
                max_x = x
                max_y = y

    if arr[max_y][max_x] == 0:
        print([max_y, max_x, max_score])
        return [max_y, max_x]
    else:
        print("We have a problem.")
