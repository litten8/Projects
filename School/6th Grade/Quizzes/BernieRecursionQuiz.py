#Bernie

#  Good job, Bernie--this code is perfect.
def revAndDouble(str):
    if len(str) == 0:
        return ""
    else:
        return revAndDouble(str[1:]) + 2 * str[0]

def countPairs(str):
    if len(str) < 2:
        return 0
    if str[0] == str[1]:
        return 1 + countPairs(str[1:])
    else:
        return countPairs(str[1:])
