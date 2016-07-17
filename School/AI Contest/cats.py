import random
import copy

def whatIf(aa, val, x, y):
    arr = copy.deepcopy(aa)
    arr[y][x] = val
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if r != y and x != x and arr[y][x] == val and arr[r][c] == val and arr[r][x] == val and arr[y][c] == val:
                startx=min(x, c)
                starty=min(y, r)
                endx=max(x, c)+1
                endy=max(y, r)+1
                for rr in range(starty, endy):
                    for cc in range(startx, endx):
                        if arr[rr][cc] != 0:
                            arr[rr][cc] = val
    score = 0
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == val:
                score+=1
    if (x == 0 and y == 0) or (x == 9 and y == 0) or (x == 0 and y ==9) or (x == 9 and y == 9):
        return score+100
    else:
        return score

def quadrant_score(x1, x2, y1, y2, arr):
    score = 1.0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if arr[y][x]==0:
                score = score * 0.5
            elif arr[y][x]==2:
                score = score * 0.25
            elif arr[y][x]==1:
                score = score * 1.0
    return score

def quadscorescore(x, y, arr):
    if arr[y][x]==0:
        score = -1
        score_q1 = quadrant_score(0, x, 0, y, arr)
        score_q2 = quadrant_score(x, len(arr[0])-1, 0, y, arr)
        score_q3 = quadrant_score(x, len(arr[0])-1, y, len(arr)-1, arr)
        score_q4 = quadran

        t_score(0, x, y, len(arr)-1, arr)
        if score_q1 > score:
            score = score_q1
        elif score_q2 > score:
            score = score_q2
        elif score_q3 > score:
            score = score_q3
        elif score_q4 > score:
            score = score_q4
        if (x == 0 and y == 0) or (x == 9 and y == 0) or (x == 0 and y ==9) or (x == 9 and y == 9):
            return score+100
        if x == 0 or y == 0 or x == 9 or y == 9:
            return score+random.uniform(0.00+(score*0.5), 0.50+(score*0.5))
        else:
            return score+random.uniform(-0.50+(score*0.5), 0.50+(score*0.5))
    else:
        return -1

def score(x, y, arr):
    if arr[y][x] == 0:
        score = whatIf(arr, 1, x, y)
        return score
    else:
        return -1

def ai(arr):
    ascore = 0
    max_x = -1
    max_y = -1
    max_score = -1
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            ascore = score(x, y, arr)
            if ascore > max_score:
                max_score = ascore
                max_x = x
                max_y = y
    if arr[max_y][max_x] == 0:
        return [max_y, max_x]
    else:
        print("We have a problem.")
