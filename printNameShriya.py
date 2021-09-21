
import random
pd1 = ['emma', 'shriya', 'william']
pd2 = ['a', 'b', 'c']
def printName():
    period = int(input("Period 1 or 2? (only type number)"))
    if period == 1:
        print(pd1[random.randint(0,len(pd1)-1)])
    elif period == 2:
        print (pd2[random.randint(0,len(pd2)-1)])
