# -*- coding: utf-8 -*-
"""
Created on 10/06/23 10:08pm

@author: Garrett Daily
"""


#####
#####   LOOP STRUCTURES: THE FOR LOOP
#####

"""
    Loop structures like FOR, WHILE
    
    Generally speaking, most programming languages have support for 2 major looping structures for repeating sections of code: for and while loops 
        (a variation of the while is a do while loop for cases where you always want the code in the loop to execute at least once - these can be spelled out in different ways and we will not use them today)
    for loops: are typically used when you have code that you would like to have run a known number of times
    while loops: are typically used when you have code that you would like to have run an UNKNOWN number of times (but not necessarily - we will look at that later)
"""

# as a quick refresher, let's look at a basic example of a list and how we gain access to each item in the list
listOfItems = ["item 1", "item 2", "item 3"]
print(listOfItems[0])
print(listOfItems[1])
print(listOfItems[2])

# now let's look at a basic for loop - notice the structure looks similar to an if statement
# listOfItems has a seqence of values stored in a list, and "item" represents an instance of one of the values within the list, just a variable that lets us access the data
# so the way this code reads: "for each instance of data we find within the listOfItems variable, print out that item; when there are no more items stop the loop and move on to whatever code comes next (or technically, "break" out of the loop)
for item in listOfItems:
    print(item)

# we can also consider ranges - these are helpful when you want to automatically generate a number - a common scenario is a "counter" variable to keep track of how many times the code within the loop runs
# notice how the counter starts at 0 - this is based on how the range works as we have seen before with partial strings; 3 means 0,1,2
for counter in range(3):
    print(counter)

# let's use the counter to provide access to the data within the listOfItems
for counter in range(3):
    print(counter)
    print(listOfItems[counter])

# what about when the range is "out of bounds" - IndexError: list index out of range - this is a problem and we need to deal with it
for counter in range(5):
    print(counter)
    print(listOfItems[counter])


#####
#####   ERROR HANDLING
#####

"""
    Understanding how to deal with error messages is an absolute requirement in all forms of programming
    try: except: finally: clauses are a common approach to dealing with unknown or unexpected problems
    try: to execute some code
    except: deal with what happens when an error does occur
    finally: in case you need some code to run "no matter what" - that is the job of code listed in the "finally" section
        note, finally is optional, and we will not always include a "finally" section, including in the activity today
"""

# first let's look at a simple way to handle errors - this is something critical in all code and will be expected moving forward
# try: except: finally: clauses https://docs.python.org/3/tutorial/errors.html
for counter in range(5):
    print(counter)
    try:
        print(listOfItems[counter])
    except:
        print("error!")

# make the error message a little more useful
for counter in range(5):
    print(counter)
    try:
        print(listOfItems[counter])
    except Exception as ex:
        print("error message: " + str(ex))

# think about what type of error may occur and generally describe it        
for counter in range(5):
    print(counter)
    try:
        print(listOfItems[counter])
    except:
        print("no data for the index value of " + str(counter))

# how do we know what the range should be? use a length function to provide the length of data that you are working with - in this case, the len function returns the number of items in the list
for counter in range(len(listOfItems)):
    print(counter)
    try:
        print(listOfItems[counter])
    except:
        print("no data for the index value of " + str(counter))

# what code runs if you have 0 length for the listOfItems
listOfItems = []
for counter in range(len(listOfItems)):
    print(counter)
    try:
        print(listOfItems[counter])
    except:
        print("no data for the index value of " + str(counter))

# let's consider other structures and see if they behave the same way...
tupleOfItems = ("item 1", "item 2", "item 3")
print(tupleOfItems[0])
print(tupleOfItems[1])
print(tupleOfItems[2])

# don't forget - if you are ever unsure of what the data type or structure is for a variable, always use the type function
type(tupleOfItems)

# iterate through each of the items in the tuple and print each item out
for item in tupleOfItems:
    print(item)

# let's consider a more complex data structure like a dictionary
# consider a dictionary that stores ASCII letters and their associated decimal value
dictionaryWithAsciiTableValues = {"A": 65, "B": 66, "C": 67, "D": 68, "a": 97, "b": 98, "c": 99, "d": 100}

# recall how we can get a list of just the keys:
print(dictionaryWithAsciiTableValues.keys())

# let's iterate over that list of keys to access each individual key
for key in dictionaryWithAsciiTableValues.keys():
    print(key)

# just for later reference, what if we want the keys printed on the same line delimited with a space?
# from a programming perspective, it is important to understand how data can be "delimited" since that understanding will help you understand how to work with the data - more on that shortly
# the print function default is to include a newline character (think "press enter") which makes your data go to the next line once it is printed
# if you don't want that default behavior, include the optional "end=" parameter in the print function to modify how the print function operates
for key in dictionaryWithAsciiTableValues.keys():
    print(key, end=" ")

# what about dictionary values?
for value in dictionaryWithAsciiTableValues.values():
    print(value)

# dictionaries are made of of a key:value pair which can be accessed using the .items() method of the dictionary
for entry in dictionaryWithAsciiTableValues.items():
    print(entry)

# we can break the entry down automatically by using multiple variables in the for loop declaration
for key, value in dictionaryWithAsciiTableValues.items():
    print("key: " + key + " value: " + str(value))

# what about a more complex dictionary with tuples (or sets, or lists)
# go ahead and define 2 tuples, 2 keyValue variables, and then use those variables to create a dictionary
tupleWithStringData1 = ("a", "b", "c")
tupleWithStringData2 = ("d", "e", "f")
keyValue1 = 1 
keyValue2 = 2 
dictionaryExample = {keyValue1:tupleWithStringData1, keyValue2:tupleWithStringData2}

# just to see what it looks like
print(dictionaryExample)

# also, we could instead have created the empty dictionary and then assigned values to keys like this:
dictionaryExample = {}
dictionaryExample[keyValue1] = tupleWithStringData1
dictionaryExample[keyValue2] = tupleWithStringData2

# note, we could have made this dictionary manually by just doing this:
# dictionaryExample = {1:("a", "b", "c"), 2:("d", "e", "f")}
# it is not likely that you will typically encounter a need to manually construct a dictionary like this manually
# it will be more likely the case that you will construct it programmatically using some type of looping structure - more on that shortly

# let's consider the previous ASCII example, but change it to this more complex dictionary:
for key,  value in dictionaryExample.items():
    print("key: " + str(key) + " value: " + str(value))

# what if we want to break out the tuple so we can get the individual values?
# just like we can next if statements, we can also nest loops
for key,  value in dictionaryExample.items():
    print("key: " + str(key) + " value: " + str(value))
    for item in value:
        print(item, end = " ")
    print()

# we will pause for a second on loops and go back to assignment operators since they can be helpful when working with loops

#####
##### EXTRA ASSIGNMENT OPERATORS (dual purposed for assignment and arithmetic operations)
#####

"""
    We have already been using the most common assignment operator =
    There are some that can come in handy for certain situations; however, some may make your code hard to understand, so use with caution
    note, anything on the right side of the = sign is a "right operand" and anything on the left side of the = sign is the "left operand"
    +=  (add the right operand to the left operand and assign the summation to the left operand)
    -=  (subtract the right operand from the left operand and assign the difference to the left operand)
    ... same comments for each of the following, just change the arithmetic operation: *=  /=  **=  %=  //= (plus others that are less used in analytics)
    
    We will look at an example with only with += for now (+= and -= are more commonly used than the others; especially in loops which will talk about shortly)
"""

# let's look at an earlier example
tip = 5
food = 25
tax = 2.50

# version 1
total = tip + food + tax
print (total)

# if we re-use total in this example, we need to reset total so it has a 0 value (this is typically where errors are introduced in version 2 if you forget to reset what you are using as the left operand)
total = 0

# version 2
total += tip
total += food
total += tax
print(total)

# here is the code commented so you can watch total change after each line and read the comments on what exactly is going on
"""
total = 0               # if we re-use total in this example, we need to reset total so it has a 0 value
print("total = " + str(total))

total += tip            # take the tip (5), add it to the current state of total (0), and assign that new value to total (0 + 5 = 5)
print("total after tip = " + str(total))

total += food           # take the food (25), add it to the current state of total (5), and assign that new value to total (5 + 25 = 30)
print("total after tip and food = " + str(total))

total += tax            # take the tax (2.50), add it to the current state of total (30), and assign that new value to total (30 + 2.50 = 32.50)
print("total after tip and food and tax = " + str(total))

print ("final total: " + str(total))
"""

# continuing on with our loop and now considering an assignment operator to help keep track of where we are in the loop
# this can be incredibly useful when working with complex data structures - we will keep it simple for now and re-introduce the idea of a counter that we construct to help us control conditional logic
for key,  value in dictionaryExample.items():
    print("key: " + str(key) + " value: " + str(value))
    counter = 0
    for item in value:
        counter += 1 
        
        if (counter == 1):
            print("list of values: ", end="")
        print(item, end = " ")
    print()

# copy the previous example and modify it to make the output a little more coherent
for key,  value in dictionaryExample.items():
    # print("key: " + str(key) + " value: " + str(value))
    counter = 0
    for item in value:
        counter += 1 
        if (counter == 1):
            print("key " + str(key) + " contains the following list of values: ", end="")
        print(item, end = " ")
    print()
    
# let's move on to while loops
    
#####
#####   LOOP STRUCTURES: THE WHILE LOOP
#####

"""
    As previously stated: generally, speaking, most programming languages have support for 2 major looping structures for repeating sections of code: for and while loops
    for loops: are typically used when you have code that you would like to have run a known number of times
    while loops: are typically used when you have code that you would like to have run an UNKNOWN number of times (but not necessarily - in theory, they can be used interchangeably, but it won't always make sense to do so or consider doing that)
"""

# consider one of our previous for loops:

listOfItems = ["item 1", "item 2", "item 3"]
for counter in range(len(listOfItems)):
    print(counter)


# our while loop will run code as long as a conditional test evaluates to true
# for example, while the counter is less than 3, execute the code
# since the variable "counter" is in the conditional test of the while loop, the "counter" variable MUST exist prior to the conditional test (this is different than how the FOR loop declaration works)

counter = 0
while (counter < 3):
    print(counter)
    counter += 1

# consider another previous for loop example using the counter to gain access to the data within the listOfItems:

for counter in range(3):
    print(counter)
    print(listOfItems[counter])


# same thing but with a while loop - pay VERY close attention to how the counter is used and at what location in the loop
counter = 0
while (counter < 3):
    print(counter)
    print(listOfItems[counter])
    counter += 1

# introduce a problem with the placement of the counter incrementation
counter = 0
while (counter < 3):
    print(counter)
    counter += 1
    print(listOfItems[counter])

# how could we deal the error?
counter = 0
while (counter < 3):
    try:
        print(counter)
        counter += 1
        print(listOfItems[counter])
    except Exception as ex:
        print("error message: " + str(ex))

# while we could introduce the len(listOfItems) - which we should do - you should always avoid static values when possible - it will still not fix the issue - make sure you understand why
counter = 0
while (counter < len(listOfItems)):
    try:
        print(counter)
        print(listOfItems[counter])
        counter += 1
    except Exception as ex:
        print("error message: " + str(ex))

#####
##### BREAKING LOOPS
#####

"""
    There are many times where you only want the loop to do work until a certain point - that is typically the job of the condition described by the loops declaration;
    However, this may not always be the case - a BREAK keyword can be used to force the loop to terminate
"""
# consider 2 of the previous examples - how do we modify these if we want them to stop (e.g. let the loop run until the main condition is met OR if we find what we are looking for prior to the end of the loop)
counter = 0
while (counter < 3):
  print(counter)
  if (counter == 1):
      break
  counter += 1

for counter in range(3):
    print(counter)
    if (counter == 1):
        break


#####
##### EXTERNAL DATA: FLAT FILES
#####

"""
    Up to this point our data has been manually created by us which is not typically the case
    Instead, we will mostly be dealing with external data (the most common scenario by far) - not to say we won't create new data, store it somewhere, and then use it in some way - we will - but it will be done programmatically and not manually as we have done so far
    Data will typically come from 3 sources:
        1.) databases (likely the repository for any company's data)
        2.) file-based data (e.g. CSV files that are likely generated by pulling data housed within databases or other sources)
        3.) web-based data which may be in various formats (e.g. JSON, customer API, other)
"""

# As we begin to work with external file-based data, we need to make sure that we understand how to find our "working directory"
# Technically, this can be set in other locations, but understanding what it means, how it affects our ability to access/store data, and how to control it programmatically is important
# import the module that will give us access to command that relates to the operating system of our environment
import os

# see what your working directory is
print(os.getcwd())

# change it to the location where your .py file resides - point at your file name, right-click on it and"copy path to clipboard" - put a \ in front of every \ that you see
os.chdir("C:\\Users\\garre\\OneDrive\\Documents\\Desktop\\MIS\\p4")

# verify the change took place
print(os.getcwd())

# BE AWARE that there are a LOT of ways to work with file-based data and a LOT of modules that provide all kinds of different file access/modification/storing options
# Python's built-in CSV module is one that is used very frequently to work with CSV file data (data that is delimited with commas indicating column-based data - comma-delimited values which are stored in the form of a CSV file)
# https://docs.python.org/3.8/library/csv.html
# There are other common modules which we will explore in upcoming modules, but for now we will keep it simple and apply our understanding of loop structures to help us read data from CSV files

# import Python's CSV module
import csv
"""
    Per https://docs.python.org/3.8/tutorial/inputoutput.html:
    It is good practice to use the "with" keyword when dealing with file objects. The advantage is that the file is properly closed after you are finished working with it (including when an exception occurs)
"""
with open("data.csv") as fileWithData:
    allOfTheRowsOfData = csv.reader(fileWithData, delimiter=",", quotechar="\"")
    for row in allOfTheRowsOfData:
        print(row)

# let's get access to a specific column based on our understanding of index values - income is 5th column, but its index value is 4
with open("data.csv") as fileWithData:
    allOfTheRowsOfData = csv.reader(fileWithData, delimiter=",", quotechar="\"")
    for row in allOfTheRowsOfData:
        print(row[4])

# let's create a list to store the income data so we can do some basic stats on it        
listWithIncomeData = []
with open("data.csv") as fileWithData:
    allOfTheRowsOfData = csv.reader(fileWithData, delimiter=",", quotechar="\"")
    for row in allOfTheRowsOfData:
        print(row[4])
        listWithIncomeData.append(row[4])

# try again and convert the data to integer data as we store it
listWithIncomeData = []
with open("data.csv") as fileWithData:
    allOfTheRowsOfData = csv.reader(fileWithData, delimiter=",", quotechar="\"")
    for row in allOfTheRowsOfData:
        print(row[4])
        listWithIncomeData.append(int(row[4]))

# how do we address it - multiple ways, but let's consider a CONTINUE command - this will require that we keep track of which row we are working in by introducing a counter variable
rowCounter = 0
listWithIncomeData = []
with open("data.csv") as fileWithData:
    allOfTheRowsOfData = csv.reader(fileWithData, delimiter=",", quotechar="\"")
    for row in allOfTheRowsOfData:
        rowCounter += 1 
        if (rowCounter == 1):
            continue
        listWithIncomeData.append(int(row[4]))


print(listWithIncomeData)

# now start using functions that we have seen before on the data, like the mean from the statistics module:
import statistics
theMeanIncome = statistics.mean(listWithIncomeData)
theMeanIncomeRounded = round(theMeanIncome, 2)
print("mean: " + str(theMeanIncomeRounded))
print("mean: " + str(round(theMeanIncome, 2)))

# what if we wanted to produce a list of zip codes with duplicates removed? Recall the purpose of a set vs a list - a set produces an unordered list of data and does not allow duplicates
# note the difference here for creating an empty set - you may expect to create a new empty set like this: setWithZipCodes = {} - but that does not work since the default for an empty dictionary has the same structure, so if we execute setWithZipCodes = {} we are creating an empty dictionary, not a set
setWithZipCodes = set()
rowCounter = 0
listWithIncomeData = []
with open("data.csv") as fileWithData:
    allOfTheRowsOfData = csv.reader(fileWithData, delimiter=",", quotechar="\"")
    for row in allOfTheRowsOfData:
        rowCounter += 1 
        if (rowCounter == 1):
            continue
        listWithIncomeData.append(int(row[4]))
        setWithZipCodes.add(int(row[1]))



# print out the new datasets
print(listWithIncomeData)
print(setWithZipCodes)
print(sorted(setWithZipCodes))

# think about error handling when working with files - for example what if the file does not exist
with open("dataBAD.csv") as fileWithData:
    allOfTheRowsOfData = csv.reader(fileWithData, delimiter=",", quotechar="\"")
    for row in allOfTheRowsOfData:
        print(row)

# we can test to see if the file exists first, then work with the file if it does
if(os.path.exists("dataBAD.csv")):
    with open("dataBAD.csv") as fileWithData:
        allOfTheRowsOfData = csv.reader(fileWithData, delimiter=",", quotechar="\"")
        for row in allOfTheRowsOfData:
            print(row)
else: 
    print("file not found")

# if the file does exist, there is always the possibility of some unexpected error in which case, try/except is a good solution for general problems
fileThatWeWantToOpen = "data.csv"
if(os.path.exists(fileThatWeWantToOpen)):
    try:
        with open(fileThatWeWantToOpen) as fileWithData:
            allOfTheRowsOfData = csv.reader(fileWithData, delimiter=",", quotechar="\"")
            for row in allOfTheRowsOfData:
                print(row)
                print(int(row[2]))
    except Exception as ex:
        print("error message: " + str(ex))
else: 
    print("file not found")

