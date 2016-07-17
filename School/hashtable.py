import math
class ItemPrice:
    def __init__(self, upc, price):
        self.upc=upc
        self.price=price
    def getUPC(self):
        return self.upc
    def getPrice(self):
        return self.price
    def setPrice(self):
        self.price=price
    def __hash__(self):
        return self.upc+16
class BarScanner:
    def __init__(self):
        hashtable==[[] for i in range(20)]
    def findPrice(self, upc):
        price=-1
        a=hashtable[hash(ItemPrice(upc,0)%20)]
        for i in range(len(a)):
            if a[i].getUPC()==upc:
                price=a[i].getPrice()
                break
        return price
    def addItemToStore(self, upc, price):
        ip=ItemPrice(upc,price)
        inArray=False
        for i in range(len(hashtable[hash(ip)%20])):
            if hashtable[hash(ip)%20][i].getUPC()==ip.getUPC():
                inx=i
                inArray=True
                break
        if inArray:
            hashtable[hash(ip)%20][inx].setPrice()
        else:
            hashtable[hash(ip)%20].append(ip)
