def QuoteFinder(f):
    wordfile=open(f)
    words=""
    for line in wordfile:
        words=words+(line.rstrip())+" "
    inquote=False
    quotes=[]
    for i in range(len(words)):
        if inquote:
            if words[i]=='"':
                inquote=False
            else:
                quotes[-1]=quotes[-1]+words[i]
        else:
            if words[i]=='"':
                inquote=True
                quotes.append('')
    return quotes
