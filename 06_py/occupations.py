#Shriya Anand
#SoftDev
#K06: Divine your Destiny- to read through a file and store the contents in a dictionary; then use weighted averages to randomly select one key
# Approach was to read the file, split it on the line breaks, then go through a while loop for each line and split it on commas and store each line in the dictionary. The keys and values of the dictionary were then inputted as arguments to the random.choice() for weighted choices.
#2021-09-28
import csv
import random
dictionary ={}
with open('occ.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         if (row['Job Class']!= 'Total' and row['Job Class']!= 'Job Class'):
             print(row['Job Class'], row['Percentage'])
             dictionary[row['Job Class']] = float(row['Percentage'])


print(random.choices(list(dictionary.keys()), weights = dictionary.values(), k = 1))
