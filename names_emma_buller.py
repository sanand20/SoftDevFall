#Question: What do you mean by "print a name"

import random
pd1 = ["emma","shriya","william","aaron"]
pd2 = ["andrew", "yuqing","michael"]

def printName():
    period = int(input('Pick a period (Input 1 or 2): '))
    if period == 1:
        print(pd1[random.randint(0,len(pd1)-1)])
    elif period == 2:
        print(pd2[random.randint(0,len(pd2)-1)])
    
