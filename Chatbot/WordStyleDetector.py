wordfile1=open("HitchhikersGuide.txt")
wordfile2=open("EndersGame.txt")
words1=""
words2=""
for line in wordfile1:
    words1=words1+(line.rstrip())+" "
words1=words1.split()
for line in wordfile2:
    words2=words2+(line.rstrip())+" "
words2=words2.split()
wordses=[words1,words2]
while True:
    percents=[1 for i in range(len(wordses))]
    sentence=input('enter a sentence: ').split()
    for i in range(len(wordses)):
        for j in range(len(sentence)):
            if j==0:
                n=0
                for k in range(len(wordses[i])):
                    if wordses[i][k]==sentence[j]:
                        n+=1
                if n>0:
                    percents[i]=percents[i]*(n/len(wordses[i]))
                else:
                    percents[i]=percents[i]*(1/len(wordses[i]))
            else:
                n=0
                for k in range(len(wordses[i])):
                    if wordses[i][k]==sentence[j] and wordses[i][k-1]==sentence[j-1]:
                        n+=1
                if n>0:
                    percents[i]=percents[i]*(n/len(wordses[i]))
                else:
                    percents[i]=percents[i]*(1/len(wordses[i]))
    print(percents[0]/percents[1])
