#Shriya Anand
#SoftDev
#K06: Divine your Destiny- to read through a file and store the contents in a dictionary; then use weighted averages to randomly select one key
#2021-09-28
import random
file = open("occ.txt", "r")
contents = file.read()
contentList = contents.split("\n")
counter = 1
dictionary ={}
while (counter< len(contentList)-1):
    contentList2 = contentList[counter].split("\t")
    dictionary[str(contentList2[0])] = float(contentList2[1])
    counter+=1

print (dictionary)

print(random.choices(list(dictionary.keys()), weights = dictionary.values(), k = 1))
