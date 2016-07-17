import SentenceGen
import random
import QuoteFinder
def maxi(a):
    x=-1
    index=-1
    for i in range(len(a)):
        if a[i]>x:
            x=a[i]
            index=i
    return index
wordsestr=QuoteFinder.QuoteFinder("wordsforjane.txt")
wordses=[wordsestr[i].split() for i in range(len(wordsestr))]
oldthing=""
thingtosay=""
print("Start:")
while True:
    sentencestr=input()
    sentence=sentencestr.split()
    wordses.append(sentence)
    wordsestr.append(sentencestr)
    timesivelooped=0
    while thingtosay==oldthing:
        timesivelooped+=1
        percents=[1.0 for i in range(len(wordses)-1)]
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
                        percents[i]=percents[i]*(1/(len(max(wordses))+random.randint(1,4)))
                else:
                    n=0
                    for k in range(len(wordses[i])):
                        if wordses[i][k]==sentence[j] and wordses[i][k-1]==sentence[j-1]:
                            n+=1
                    if n>0:
                        percents[i]=percents[i]*(n/len(wordses[i]))
                    else:
                        percents[i]=percents[i]*(1/(len(max(wordses))+random.randint(1,4)))
        thingtosay=SentenceGen.randomSentence(wordsestr[maxi(percents)+1].split())
        if timesivelooped>20:
            thingtosay=SentenceGen.randomSentence(wordsestr[random.randint(0, len(wordsestr)-1)].split())
            break
    print(thingtosay)
    wordses.append(thingtosay.split())
    wordsestr.append(thingtosay)
    oldthing=thingtosay
