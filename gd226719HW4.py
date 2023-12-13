# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:43:29 2023

@author: Garrett Daily
"""

#####
# Problem 1
#####

start = 65 #65 through 91 outputs A - Z based on the ASCII table
end = 91
for value in range(start, end): #ranges are non-inclusive of the last value. This is why I had to go through 91 to output Z
    print(chr(value))

#####
# Problem 2
#####

start = 65  #65 through 91 outputs A - Z based on the ASCII table
end = 91    

for value in range(start, end):
    if value < end - 1: #this checks to make sure the current value is not the last one
        print(chr(value) + ",", end="")
    else:
        print(chr(value) + ",")

#####
# Problem 3
#####

start = 65  
end = 91    
value = start #I added a variable before the lines of code to run the while loop

while (value < end): #this while loop runs as long as 'value' is less than the end
    if value < end - 1: #this checks to make sure the current value is not the last one (which would be the end)
        print(chr(value) + ",", end="")
    else:
        print(chr(value) + ",")
    value += 1

#####
# Problem 4
#####

start = 65  #65 through 91 outputs A - Z based on the ASCII table
end = 91
myString = "" 

for value in range(start, end):
    if value < end - 1: #this checks to make sure the current value is not the last one
        myString += chr(value) + "," 
    else:
        myString += chr(value) + ","
lenValue = len(myString) -1 

print(myString[0:lenValue]) #the len() function here on the string substracts 1 to get the desired output

#####
# Problem 5
#####

myDictionary = {} # a dictionary uses a key to store the value for the key
start = 65
end = 91

for value in range(start, end):
    myDictionary[chr(value)] = value
    
print(str(myDictionary.keys())) # the letter A comes from: chr(value)
print(str(myDictionary.values())) # the 65 comes from: value
    
#####
# Problem 6
#####

start = 65
end = 91
while (value > end): #this while loop runs as long as 'value' is less than the end
    myDictionary = {}
    myDictionary[chr(value)] = value
    value += 1
for key, value in myDictionary.items():
    print("key: " + key + " value: " + str(value)) # this print function gives the desired output 
    
#####
# Problem 7
#####

import os
os.chdir("C:\\Users\\garre\\OneDrive\\Documents\\Desktop\\MIS\\p4")   #this is the path for the csv data
print(os.getcwd())
rowCounter = 0 #created two variables here for the following problem
rowNumber = 0
import csv
fileToOpen = "wineData.csv"
if(os.path.exists(fileToOpen)):
    try:
        with open(fileToOpen, encoding="utf-8-sig") as fileWithData:
            allOfTheRowsOfData = csv.reader(fileWithData, delimiter=",", quotechar="\"") 
            for row in allOfTheRowsOfData:
                rowCounter += 1
                rowNumber += 1
                if (rowCounter <= 10):
                    print("Row #" + str(rowNumber) + ": " + str(row))
    except Exception as ex:
        print("error message: " + str(ex)) #try/except should be used for error handling
          
#####
# Problem 8
#####

rowCounter = 0
fileToOpen = "wineData.csv"
if(os.path.exists(fileToOpen)):
    try:
        with open(fileToOpen, encoding="utf-8-sig") as fileWithData:
            allOfTheRowsOfData = csv.reader(fileWithData, delimiter=",", quotechar="\"") 
            for row in allOfTheRowsOfData:
                rowCounter += 1 # remember to keep track of a counter inside of a loop
        print(rowCounter-1)
    except Exception as ex:
        print("error message: " + str(ex)) #try/except should be used for error handling
# this will print out only the final answer instead of all rows

#####
# Problem 9
#####

listWithPoints = [] #similar to the problem in P4 but instead of a set use a list
listWithPrices = []
fileToOpen = "wineData.csv"
if(os.path.exists(fileToOpen)):
    try:
        with open(fileToOpen, encoding="utf-8-sig") as fileWithData:
            allOfTheRowsOfData = csv.reader(fileWithData, delimiter=",", quotechar="\"")
            thisCounter = 0
            for row in allOfTheRowsOfData:
                thisCounter += 1
                if (thisCounter == 1):
                    continue
                listWithPoints.append(float(row[1])) #had to change to float for the decimal values (similar to how we used string in the P4)
                listWithPrices.append(float(row[2]))
        lowPoint = min(listWithPoints) #these calculations will give the desired output for the problem
        highPoint = max(listWithPoints)
        avgPoint = (sum(listWithPoints) / len(listWithPoints))
        lowPrice = min(listWithPrices)
        highPrice = max(listWithPrices)
        avgPrice = (sum(listWithPrices) / len(listWithPrices))
        print("lowest points awarded: " + format(lowPoint, ",.0f")) 
        print("average points awarded: " + format(avgPoint, ",.1f"))
        print("highest points awarded: " + format(highPoint, ",.0f"))
        print("lowest price: " + "$" + format(lowPrice, ",.2f")) #this formatting needs to be used when dealing with money
        print("average price: " + "$" + format(avgPrice, ",.2f"))
        print("highest price: " + "$" + format(highPrice, ",.2f"))
    except Exception as ex:
        print("error message: " + str(ex)) #try/except should be used for error handling
