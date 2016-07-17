import sys
inputs = []
for line in sys.stdin:
    inputs.append(line)
del inputs[0]
#    inputs=["Joe 11", "Bob 123", "NA 101", "Katy 125", "Sam 47", "Mike 59", "NA 23", "Vivek 62", "Fred 0", "Lars 74", "Oscar 86", "Caroline 11", "NA 90", "Erin 11", "Rachel 111", "Nate 125"]
unused=[]
used=[]
duplicates=[]
unemployed=0
for i in range(len(inputs)):
    NA = False
    number =inputs[i]
    if "NA " in inputs[i]:
        NA = True
    number = number.split()[1]
    if NA:
        unused.append(number)
    elif number == "0":
        unemployed+=1
    else:
        if number in used:
            if number not in duplicates:
                duplicates.append(number)
        else:
            used.append(number)
print(len(unused))
print(len(duplicates))
print(unemployed)
