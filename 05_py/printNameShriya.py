#Shriya Anand and Angela Zhang
# SoftDev
# Classwork- Class Names
# POW WOW SUMMARY: When you call the printName() function, it asks you which period you want the student from. Originally, the code would then provide a random student from the list; after talking to my partner, however, we have changed it so that the user can input which number student they want from the list.

import random

def printName():
    try:
        file = open("pd1.txt", "r")
        contents1 = (file.read())
        pd1 = (contents1.split(", "))
        
        file = open("pd2.txt", "r")
        contents2 = (file.read())
        pd2 = (contents2.split(", "))
        
        dictionary = {}
        dictionary["one"] = pd1
        dictionary["two"] = pd2
        
    except: print ("One or more files are not valid")

      
        
    try:
        
        period = int(input("Period 1 or 2? (only type number)"))
        
        if period == 1:           
            print (dictionary["one"][random.randint(0,len(pd2)-1)])
        elif period == 2:
            print (dictionary["two"][random.randint(0,len(pd2)-1)])
        else:
            print ("This input is not valid")
       
    except: print ("This input is not valid")
