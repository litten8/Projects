import random
words=["python", "scratch", "hillbrook", "hangman", "programming", "school", "suzanne", "bernie", "coding", "afterschool", "children"]
word=random.choice(words)
goal=0
chancesleft=10
while chancesleft>0:
    print("choose a letter that you think is in the word. It has " + str(len(word)) + " letters. you have " + str(chancesleft) + " chances left.")
    letter=input()
    letterplaces=[]
    for i in range(len(word)):
        if word[i]==letter:
            letterplaces.append(i+1)
    if len(letterplaces)<1:
        chancesleft-=1
        print("That letter is  not in the word!")
        if chancesleft==0:
            print("You lost... The word was " + word + ".")
            break
    else:
        placesstring=""
        for i in range(len(letterplaces)):
            placesstring+=str(letterplaces[i]) + ", "
        print("That letter is in the following places in the word: " + placesstring)
        goal+=len(letterplaces)
        if goal==len(word):
            print("You won! The word was " + word + "!")
            break
