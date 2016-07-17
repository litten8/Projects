import random
def randomSentence(words):
    capitals="Q W E R T Y U I O P A S D F G H J K L Z X C V B N M".split()
    punctuation=[".","!","?",'."','!"','?"']
    capitalwords=[]
    for i in range(len(words)):
        if words[i][0] in capitals:
            capitalwords.append(words[i])
    if len(capitalwords)==0:
        capitalwords.append(words[0])
    for i in range(10):
        firstword=random.choice(capitalwords)
        sentence=firstword
        timesiveloopedsg=0
        while True:
            timesiveloopedsg+=1
            if firstword[-1] in punctuation:
                break
            nextwords=[]
            for i in range(len(words)):
                if words[i]==firstword and len(words)>i+1:
                    nextwords.append(words[i+1])
            if len(nextwords)>0:
                firstword=random.choice(nextwords)
            sentence=sentence+" "+firstword
            if timesiveloopedsg>20:
                sentence=""
                for i in range(len(words)):
                    sentence=sentence+" "+words[i]
                break
        return sentence
