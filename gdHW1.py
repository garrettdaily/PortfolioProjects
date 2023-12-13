# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 20:34:41 2023

@author: Garrett Daily
"""

#####
# Problem 1
#####

value1 = input("Please enter value 1: ")
value2 = input("Please enter value 2: ")

value1 = float(value1) #remember to cast your string variables into int or float when necessary
value2 = float(value2)

if(value1 < value2):
    print(str(value1) + " is less than " + str(value2))  #you must make the variables string data in order to print them out correctly
elif(value1 == value2):
    print(str(value1) + " is equal to " + str(value2)) #I used an elif function here to account for other outcomes in my conditional logic
else:
    print(str(value1) + " is greater than " + str(value2))

#####
# Problem 2
#####

salesVolume = input("Please enter a value for sales volume to find out how it is classified: ")
salesVolume = float(salesVolume) #make your variables the float type when working with numbers that have decimals

if(salesVolume >= 0 and salesVolume <= 20):
    print(str(salesVolume) + " is classified as small sales volume")
elif(salesVolume > 20 and salesVolume <= 60):
    print(str(salesVolume) + " is classified as medium sales volume")
elif(salesVolume > 60):
    print(str(salesVolume) + " is classified as large sales volume")

    
#####
# Problem 3
#####

question1 = input("Would you like to view sales volume data?")
question1 = question1.lower() #the lower function here helps mitigate wrong outputs 
# if someone were to answer with lowercase "yes"
textData = "yes"

if (question1 == textData):
    print("You are viewing sales volume data")
else: #using the else function gives you an answer when there are any other answers than the one desired
    print("Other data is currently not available")

#####
# Problem 4
#####

question1 = input("Would you like to view sales volume data?")
question1 = question1.lower() #the lower function here helps mitigate wrong outputs 
# if someone were to answer with lowercase "yes"
textData = "yes"

if (question1 == textData):
    salesVolume = input("Enter a value for sales volume: ")
    salesVolume = float(salesVolume)
    if(salesVolume >= 0 and salesVolume <= 20):
        print(str(salesVolume) + " is classified as small sales volume")
    elif(salesVolume > 20 and salesVolume <= 60):
        print(str(salesVolume) + " is classified as medium sales volume")
    elif(salesVolume > 60):
        print(str(salesVolume) + " is classified as large sales volume")
    elif(salesVolume < 0):
        print("Error - Number must be greater than zero.")
else: #the else here is just say something about the data not being available
    print("Other data is currently not available")

#####
# Problem 5
#####

listOfCustomerIds = [1,2,3,4,5,6,7,8,9,10,11]
listOfZipCodes = [43147,30303,30303,54729,43147,30303,43147,11354,49009,30303,45701]
listOfCities = ["Pickerington","Atlanta","Atlanta","Chippewa Falls","Pickerington","Atlanta","Pickerington","Flushing","Kalamazoo","Atlanta","Athens"]
listOfStates = ["OH","GA","GA","WI","OH","GA","OH","NY","MI","GA","OH"]
listOfIncome = [65000,49000,54000,114000,47000,119000,60000,76000,44000,47000,55000]
listOfSalesVolume = [100,20,15,90,120,110,130,50,30,20,60]

dictionaryWithCustomerData = {}
whichIndexValue = 0 #by repeating this statement and chaning the values, this gives use the keys in our dictionary
tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
whichIndexValue = 1
tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
whichIndexValue = 2
tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
whichIndexValue = 3
tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
whichIndexValue = 4
tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
whichIndexValue = 5
tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
whichIndexValue = 6
tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
whichIndexValue = 7
tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
whichIndexValue = 8
tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
whichIndexValue = 9
tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
whichIndexValue = 10
tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData

print("The data associate with key 11 is: " + str(dictionaryWithCustomerData[11]))
print("All keys in the dictionary are: ") #str() function needs to be used with data in order to concatenate it
print(dictionaryWithCustomerData.keys())
print("All values in the dictionary are: ")
print(dictionaryWithCustomerData.values())

#####
# Problem 6
#####

del(dictionaryWithCustomerData) #this deletes the dictionary that was just made

#####
# Problem 7
#####

def createMyDictionary():
    "This function makes a dictionary"
    
    dictionaryWithCustomerData = {}
    whichIndexValue = 0 #by repeating this statement and chaning the values, this gives use the keys in our dictionary
    tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
    dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
    whichIndexValue = 1
    tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
    dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
    whichIndexValue = 2
    tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
    dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
    whichIndexValue = 3
    tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
    dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
    whichIndexValue = 4
    tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
    dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
    whichIndexValue = 5
    tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
    dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
    whichIndexValue = 6
    tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
    dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
    whichIndexValue = 7
    tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
    dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
    whichIndexValue = 8
    tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
    dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
    whichIndexValue = 9
    tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
    dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
    whichIndexValue = 10
    tupleWithCustomerData = (listOfCities[whichIndexValue], listOfStates[whichIndexValue], listOfZipCodes[whichIndexValue], listOfIncome[whichIndexValue], listOfSalesVolume[whichIndexValue])
    dictionaryWithCustomerData[listOfCustomerIds[whichIndexValue]] = tupleWithCustomerData
    
    print("All keys in the dictionary are: ") 
    print(dictionaryWithCustomerData.keys())
    print("All values in the dictionary are: ")
    print(dictionaryWithCustomerData.values())
   
    return dictionaryWithCustomerData #the return function here returns the data from within the function above
createMyDictionary()
dictionaryWithCustomerData = createMyDictionary 

#####
# Problem 8
#####

inputNumber = 10
whichIndexValue = float(input("Enter a customerID: ")) #remember to wrap you variables in the float() function when applicable
if (inputNumber == whichIndexValue):
    print("The data associated with key 10 is: " + str(tupleWithCustomerData))
else:
    print("The data is currently not available for other customers") #this else statement returns if the input number is anything other than 10
    
#####
# problem 9
#####

customerID = int(input("Please enter a customer ID: ")) #wrap you variables in int() functions when neccesary
if (customerID == listOfCustomerIds[0]):
    if (0 <= listOfSalesVolume[0] <= 20): # the first part of code needs to be indented like this line
        print("CustomerID " + str(customerID) + " has small sales volume")
    elif (20 <= listOfSalesVolume[0] <= 60):
        print("CustomerID " + str(customerID) + " has medium sales volume")
    elif (listOfSalesVolume[0] > 60):
        print("CustomerID " + str(customerID) + " has large sales volume")
if (customerID == listOfCustomerIds[1]):
    if (0 <= listOfSalesVolume[1] <= 20):
        print("CustomerID " + str(customerID) + " has small sales volume")
    elif (20 <= listOfSalesVolume[1] <= 60):
        print("CustomerID " + str(customerID) + " has medium sales volume")
    elif (listOfSalesVolume[1] > 60):
        print("CustomerID " + str(customerID) + " has large sales volume")
if (customerID == listOfCustomerIds[2]):
    if (0 <= listOfSalesVolume[2] <= 20):
        print("CustomerID " + str(customerID) + " has small sales volume")
    elif (20 <= listOfSalesVolume[2] <= 60):
        print("CustomerID " + str(customerID) + " has medium sales volume")
    elif (listOfSalesVolume[2] > 60):
        print("CustomerID " + str(customerID) + " has large sales volume")
if (customerID == listOfCustomerIds[3]):
    if (0 <= listOfSalesVolume[3] <= 20):
        print("CustomerID " + str(customerID) + " has small sales volume")
    elif (20 <= listOfSalesVolume[3] <= 60):
        print("CustomerID " + str(customerID) + " has medium sales volume")
    elif (listOfSalesVolume[3] > 60):
        print("CustomerID " + str(customerID) + " has large sales volume")
if (customerID == listOfCustomerIds[4]):
    if (0 <= listOfSalesVolume[4] <= 20):
        print("CustomerID " + str(customerID) + " has small sales volume")
    elif (20 <= listOfSalesVolume[4] <= 60):
        print("CustomerID " + str(customerID) + " has medium sales volume")
    elif (listOfSalesVolume[4] > 60):
        print("CustomerID " + str(customerID) + " has large sales volume")
if (customerID == listOfCustomerIds[5]):
    if (0 <= listOfSalesVolume[5] <= 20):
        print("CustomerID " + str(customerID) + " has small sales volume")
    elif (20 <= listOfSalesVolume[5] <= 60):
        print("CustomerID " + str(customerID) + " has medium sales volume")
    elif (listOfSalesVolume[5] > 60):
        print("CustomerID " + str(customerID) + " has large sales volume")
if (customerID == listOfCustomerIds[6]):
    if (0 <= listOfSalesVolume[6] <= 20):
        print("CustomerID " + str(customerID) + " has small sales volume")
    elif (20 <= listOfSalesVolume[6] <= 60):
        print("CustomerID " + str(customerID) + " has medium sales volume")
    elif (listOfSalesVolume[6] > 60):
        print("CustomerID " + str(customerID) + " has large sales volume")
if (customerID == listOfCustomerIds[7]):
    if (0 <= listOfSalesVolume[7] <= 20):
        print("CustomerID " + str(customerID) + " has small sales volume")
    elif (20 <= listOfSalesVolume[7] <= 60):
        print("CustomerID " + str(customerID) + " has medium sales volume")
    elif (listOfSalesVolume[7] > 60):
        print("CustomerID " + str(customerID) + " has large sales volume")
if (customerID == listOfCustomerIds[8]):
    if (0 <= listOfSalesVolume[8] <= 20):
        print("CustomerID " + str(customerID) + " has small sales volume")
    elif (20 <= listOfSalesVolume[8] <= 60):
        print("CustomerID " + str(customerID) + " has medium sales volume")
    elif (listOfSalesVolume[8] > 60):
        print("CustomerID " + str(customerID) + " has large sales volume")
if (customerID == listOfCustomerIds[9]):
    if (0 <= listOfSalesVolume[9] <= 20):
        print("CustomerID " + str(customerID) + " has small sales volume")
    elif (20 <= listOfSalesVolume[9] <= 60):
        print("CustomerID " + str(customerID) + " has medium sales volume")
    elif (listOfSalesVolume[9] > 60):
        print("CustomerID " + str(customerID) + " has large sales volume")
if (customerID == listOfCustomerIds[10]):
    if (0 <= listOfSalesVolume[10] <= 20):
        print("CustomerID " + str(customerID) + " has small sales volume")
    elif (20 <= listOfSalesVolume[10] <= 60):
        print("CustomerID " + str(customerID) + " has medium sales volume")
    elif (listOfSalesVolume[10] > 60):
        print("CustomerID " + str(customerID) + " has large sales volume")
if (customerID < 0):
    print("Error: The number entered must be greater than zero, please enter another number")
#note that I copied the if statement down to account for each customer ID

#####
# Problem 10
#####

enteredIdMin = min(listOfCustomerIds)
enteredIdMax = max(listOfCustomerIds)
textData = "yes"
textDataQuestion = input("Would you like to view sales volume data? ")
textDataQuestion = textDataQuestion.lower()
if (textDataQuestion == textData):
    customerID = int(input("Please enter a customerId: "))
    if (customerID == listOfCustomerIds[0]): # the first part of code needs to be indented like this line
        if (0 <= listOfSalesVolume[0] <= 20):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[0]) + " and is classified as small sales volume")
        elif (20 <= listOfSalesVolume[0] <= 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[0]) + " and is classified as medium sales volume")
        elif (listOfSalesVolume[0] > 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[0]) + " and is classified as large sales volume")
    if (customerID == listOfCustomerIds[1]):
        if (0 <= listOfSalesVolume[1] <= 20):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[1]) + " and is classified as small sales volume")
        elif (20 <= listOfSalesVolume[1] <= 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[1]) + " and is classified as medium sales volume")
        elif (listOfSalesVolume[1] > 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[1]) + " and is classified as large sales volume")
    if (customerID == listOfCustomerIds[2]):
        if (0 <= listOfSalesVolume[2] <= 20):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[2]) + " and is classified as small sales volume")
        elif (20 <= listOfSalesVolume[2] <= 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[2]) + " and is classified as medium sales volume")
        elif (listOfSalesVolume[2] > 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[2]) + " and is classified as large sales volume")
    if (customerID == listOfCustomerIds[3]):
        if (0 <= listOfSalesVolume[3] <= 20):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[3]) + " and is classified as small sales volume")
        elif (20 <= listOfSalesVolume[3] <= 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[3]) + " and is classified as medium sales volume")
        elif (listOfSalesVolume[3] > 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[3]) + " and is classified as large sales volume")
    if (customerID == listOfCustomerIds[4]):
        if (0 <= listOfSalesVolume[4] <= 20):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[4]) + " and is classified as small sales volume")
        elif (20 <= listOfSalesVolume[4] <= 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[4]) + " and is classified as medium sales volume")
        elif (listOfSalesVolume[4] > 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[4]) + " and is classified as large sales volume")
    if (customerID == listOfCustomerIds[5]):
        if (0 <= listOfSalesVolume[5] <= 20):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[5]) + " and is classified as small sales volume")
        elif (20 <= listOfSalesVolume[5] <= 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[5]) + " and is classified as medium sales volume")
        elif (listOfSalesVolume[5] > 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[5]) + " and is classified as large sales volume")
    if (customerID == listOfCustomerIds[6]):
        if (0 <= listOfSalesVolume[6] <= 20):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[6]) + " and is classified as small sales volume")
        elif (20 <= listOfSalesVolume[6] <= 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[6]) + " and is classified as medium sales volume")
        elif (listOfSalesVolume[6] > 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[6]) + " and is classified as large sales volume")
    if (customerID == listOfCustomerIds[7]):
        if (0 <= listOfSalesVolume[7] <= 20):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[7]) + " and is classified as small sales volume")
        elif (20 <= listOfSalesVolume[7] <= 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[7]) + " and is classified as medium sales volume")
        elif (listOfSalesVolume[7] > 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[7]) + " and is classified as large sales volume")
    if (customerID == listOfCustomerIds[8]):
        if (0 <= listOfSalesVolume[8] <= 20):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[8]) + " and is classified as small sales volume")
        elif (20 <= listOfSalesVolume[8] <= 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[8]) + " and is classified as medium sales volume")
        elif (listOfSalesVolume[8] > 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[8]) + " and is classified as large sales volume")
    if (customerID == listOfCustomerIds[9]):
        if (0 <= listOfSalesVolume[9] <= 20):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[9]) + " and is classified as small sales volume")
        elif (20 <= listOfSalesVolume[9] <= 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[9]) + " and is classified as medium sales volume")
        elif (listOfSalesVolume[9] > 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[9]) + " and is classified as large sales volume")
    if (customerID == listOfCustomerIds[10]):
        if (0 <= listOfSalesVolume[10] <= 20):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[10]) + " and is classified as small sales volume")
        elif (20 <= listOfSalesVolume[10] <= 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[10]) + " and is classified as medium sales volume")
        elif (listOfSalesVolume[10] > 60):
            print("Sales volume data for customerID " + str(customerID) + " is " + str(listOfSalesVolume[10]) + " and is classified as large sales volume")
    if (customerID > enteredIdMax):
        print("CustomerID " + str(customerID) + " is not valid")
    if (customerID < enteredIdMin):
        print("CustomerID " + str(customerID) + " is not valid")    
else:
    print("Other data is currently not available")
#this problem is very similar to 9, I copied down most of the code and changed the print statements to get the desired outcome
