import random
import sys
import time
wordfile=open("wordsforjane.txt")
words=""
for line in wordfile:
    words=words+(line.rstrip())+" "
words=words.split()
while True:
    firstword=input()
    nextwords=[]
    for i in range(len(words)):
        if words[i]==firstword:
            nextwords.append(words[i+1])
    print(nextwords)
