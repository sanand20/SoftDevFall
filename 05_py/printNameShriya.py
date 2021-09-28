#Shriya Anand and Angela Zhang

# Trio Discussion:
# When you call the printName() function, it asks you which period you want the student from.
# After working with Angela, we incorporated a means of reading a text file for the names and storing it in a dictionary.
# During our amalgamation, we decided that it would be efficient to type cast the input in the same line; we also used my try and except approach to catch errors that could potentially arise.

# Discoveries:
# I refreshed my memory on dictionaries as well as reading a text file in python. I am realizing how much easier it is to do so in python as compared to java.

# Questions:
# Is it fine that we are reading the data from a text file into a list and then storing it in a dictionary? I am afraid it might defeat the purpose of the dictionary.
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
