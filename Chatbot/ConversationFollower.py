def maxi(a):
    x=-1
    index=-1
    for i in range(len(a)):
        if a[i]>x:
            x=a[i]
            index=i
    return index
perciceness=4
wordsestr=["Good morning.", "Great morning more like it! My day has been great.", "What's so great about it?", "Everything, how do you feel about this morning?", "ot so well.", "Why is that?", "I lost my dog, and I've had posters up for a week, and nobody has found him.", "Well I don't care because I don't have a dog, and hate them. I like cats.", "Well you suck."]
wordses=[wordsestr[i].split() for i in range(len(wordsestr))]
while True:
    percents=[1.0 for i in range(len(wordses)-1)]
    sentence=input().split()
    for i in range(len(wordses)-1):
        for j in range(len(sentence)):
            if j==0:
                n=0
                for k in range(len(wordses[i])):
                    if wordses[i][k]==sentence[j]:
                        n+=1
                if n>0:
                    percents[i]=percents[i]*(n/len(wordses[i]))
                else:
                    percents[i]=percents[i]*(1/(len(wordses[i])+perciceness))
            else:
                n=0
                for k in range(len(wordses[i])):
                    if wordses[i][k]==sentence[j] and wordses[i][k-1]==sentence[j-1]:
                        n+=1
                if n>0:
                    percents[i]=percents[i]*(n/len(wordses[i]))
                else:
                    percents[i]=percents[i]*(1/(len(wordses[i])+perciceness))
    print(percents)
    print(wordsestr[maxi(percents)+1])
