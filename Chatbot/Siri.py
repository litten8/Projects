import random
tosayd={"Siri":"I am not Siri! I just resemble Siri","Hello":"Hello","idiot":"That's mean","face":"I don't have a face","woodchuck":"It would chuck as much wood as a woodchuck could if a woodchuck could chuck wood","hate":"That's not nice","Misha":"Misha time!","there":"Where?","where":"There"}
notsure=["What do you mean?", "I'm not sure what you're saying", "Please say that again"]
commonwords=["","the","The","is","Is","and","And","if","If","of","Of","then","Then","that","That","that's","That's","what","What","do","Do","this","This"]
justsaid=None
tosay=None
while True:
    sentencestr=input()
    sentence=sentencestr.split()
    if tosay:
        newword=random.choice(tosay.split())
        while newword in commonwords:
            newword=random.choice(tosay.split())
        tosayd[newword]=sentencestr
    tosay=None
    for i in range(len(sentence)):
        if sentence[i] in tosayd:
            tosay=tosayd[sentence[i]]
    if not tosay:
        tosay=random.choice(notsure)
    print(tosay)
