import time
start=1
divide=float(input("divide"))
add=float(input("add"))
def func(start, divide, add):
    return((start/divide)+add)
while True:
    oldstart=start
    start=func(start,divide,add)
    print(start)
    if start==oldstart:
        break
