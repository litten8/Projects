#  Nice work, Bernie!  Both of these execute perfectly,
#    and your code is quite easy to read

def makeTranspose(a):
    rows = len(a)
    cols = len(a[0])
    newa = []
    for c in range(cols):
        toadd = []
        for r in range(rows):
            toadd.append(a[r][c])
        newa.append(toadd)
    return(newa)

x=[[1,2],[3,4], [5,6],[7,8]]
print(makeTranspose(x))

def addRowWithColumnSums(a):
    rows = len(a)
    cols = len(a[0])
    newarow = []
    for c in range(cols):
        toadd = 0
        for r in range(rows):
            toadd = toadd+a[r][c]
        newarow.append(toadd)
    a.append(newarow)

addRowWithColumnSums(x)
print(x)
