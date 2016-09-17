# a simple AI to play Jigga-Jigga

def ai(arr):
    if arr[0][0] == 0:
        return [0,0]
    if arr[0][9] == 0:
        return [0,9]
    if arr[9][0] == 0:
        return [9,0]
    if arr[9][9] == 0:
        return [9,9]
    for j in range(3,27,3):
        x = j%10
        if arr[x][0] == 0:
            return [x,0]
        if arr[x][9] == 0:
            return [x,9]
        if arr[0][x] == 0:
            return [0,x]
        if arr[9][x] == 0:
            return [9,x]
    for j in range(0,100):
        x = int((j*53)/10)%10
        y = (j*53)%10
        if arr[x][y] == 0:
            return [x,y]