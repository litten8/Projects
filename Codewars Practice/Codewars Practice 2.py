import sys
inputs = []
for line in sys.stdin:
    inputs.append(line)
del inputs[-1]
scores={}
for i in range(len(inputs)):
    info = inputs[i].split()
    scores[info[0]] = scores.get(info[0], 0) + int(info[1])
scorelist=[]
teamlist=[]
for k in scores:
    scorelist.append(scores[k])
    teamlist.append(k + " " + scores[k])
scorelist=sorted(scorelist)
for i in range(5):
    print(str(5-i) + " " + str(teamlist))
