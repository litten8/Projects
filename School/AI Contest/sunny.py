import random

def ai(arr):               
    #  First priority--take a corner
    if arr[0][0] == 0:
        return [0,0]
    if arr[0][9] == 0:
        return [0,9]
    if arr[9][0] == 0:
        return [9,0]
    if arr[9][9] == 0:
        return [9,9]

    #  Second priority--take an edge
    for x in range(10):
        if arr[0][x] == 0:
            return [0,x]
        if arr[x][0] == 0:
            return [x,0]
        if arr[9][x] == 0:
            return [9,x]
        if arr[x][9] == 0:
            return [x,9]

    #  Third priority--complete a rectangle with a corner as a vertex
    for r in range(0,10):
        for c in range(0,10):
            if arr[r][c] == 0:
                if arr[0][0] == 1 and arr[r][0] == 1 and arr[0][c] == 1:
                    return [r,c]
                if arr[9][0] == 1 and arr[r][0] == 1 and arr[9][c] == 1:
                    return [r,c]
                if arr[0][9] == 1 and arr[0][c] == 1 and arr[r][9] == 1:
                    return [r,c]
                if arr[9][9] == 1 and arr[r][9] == 1 and arr[9][c] == 1:
                    return [r,c]
        
    #  Choose randomly if none of these
    emptysquares = []
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 0:
                emptysquares.append([r,c])
    return random.choice(emptysquares)
    
            
