# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:37:09 2023

@author: Garrett Daily
"""

#####
# Problem 1
#####

import pandas # you must import pandas before starting
import os # you must import os before starting
print(os.getcwd())
os.chdir("C:\\Users\\garre\\OneDrive\\Documents\\Desktop\\MIS\\hw5") #this brings in the csv we are wanting to read

dataFrameWithTrumpTweets = pandas.read_csv("realDonaldTrump.csv", encoding = "ISO-8859-1") #this reads the csv 
dataFrameWithObamaTweets = pandas.read_csv("BarackObama.csv", encoding = "ISO-8859-1") # this reads the csv

print("The rows and columns for the dataFrameWithTrumpTweets are: " + str(dataFrameWithTrumpTweets.shape))
print("The rows and columns for the dataFrameWithObamaTweets are: " + str(dataFrameWithObamaTweets.shape))

#####
# Problem 2
#####

dataFrameWithObamaTweets["whichFile"] = "BarackObama.csv"
dataFrameWithTrumpTweets["whichFile"] = "DonaldTrump.csv"

dataFrameWithCombinedTweets = pandas.DataFrame() # this creates an empty data frame
dataFrameWithCombinedTweets = pandas.concat([dataFrameWithObamaTweets, dataFrameWithTrumpTweets], ignore_index=False) #the concat function here
# joins together the two csv files
dataFrameWithCombinedTweets.info() # the .info() function gives us the expected output

#####
# Problem 3
##### 

pandas.set_option("display.max_columns", 8) # this sets the max columns
pandas.set_option("display.max_rows", 10) # this sets the max rows

print(dataFrameWithCombinedTweets.loc[0])

#####
# Problem 4
#####

dataFrameWithCombinedTweets = dataFrameWithCombinedTweets.reset_index() # this function resets the index
minIndexValue = dataFrameWithCombinedTweets.index.min() # this variable holds them minimum index value
maxIndexValue = dataFrameWithCombinedTweets.index.max() # this variable holds the max index value

print("The data at the minimum index (0) is: \n" + str(dataFrameWithCombinedTweets.loc[minIndexValue]) + "\n" + "The data at the maximum index (6438) is: \n" + str(dataFrameWithCombinedTweets.loc[maxIndexValue])) 

#####
# Problem 5
#####

del(dataFrameWithCombinedTweets["index"]) #this deletes the index row in the output
print("The data at the minimum index (0) is: \n" + str(dataFrameWithCombinedTweets.loc[minIndexValue]) + "\n" + "The data at the maximum index (6438) is: \n" + str(dataFrameWithCombinedTweets.loc[maxIndexValue])) 

#####
# Problem 6
#####

dataFrameWithCombinedTweets.isna().sum() # this shows you where there are missing values

dataFrameWithCombinedTweets["url"] = dataFrameWithCombinedTweets["url"].fillna("no url provided")
dataFrameWithCombinedTweets["replies"] = dataFrameWithCombinedTweets["replies"].fillna(0) # the .fillna(0) function here makes the missing values "0"
dataFrameWithCombinedTweets["retweets"] = dataFrameWithCombinedTweets["retweets"].fillna(0)
dataFrameWithCombinedTweets["favorites"] = dataFrameWithCombinedTweets["favorites"].fillna(0)

dataFrameWithCombinedTweets.isna().sum() # this shows you where there are missing values

#####
# Problem 7
#####

newDataFrame = dataFrameWithCombinedTweets[(dataFrameWithCombinedTweets["url"] != "bad data") & (dataFrameWithCombinedTweets["replies"] != "bad data") & (dataFrameWithCombinedTweets["replies"] != "bad data") & (dataFrameWithCombinedTweets["retweets"] != "bad data") & (dataFrameWithCombinedTweets["favorites"] != "bad data")]
# this returns a dataframe where there are no columns with "bad data" in them
newDataFrame.info()

#####
# Problem 8
#####

import re # you must import the re package before starting
def returnAnInteger(data):
    
    data = str(data) # this turns that data that passes through into string data
    dataThatHasBeenCleaned = re.sub("[^0-9]", "", data)
    return dataThatHasBeenCleaned # this returns the cleaned data
newDataFrame["replies"] = newDataFrame["replies"].apply(returnAnInteger).astype("int") # this converts the data into an integer
newDataFrame["retweets"] = newDataFrame["retweets"].apply(returnAnInteger).astype("int")
newDataFrame["favorites"] = newDataFrame["favorites"].apply(returnAnInteger).astype("int")

newDataFrame["replies"] = newDataFrame["replies"].apply(returnAnInteger).astype("int32") # this makes the data here into int32
newDataFrame["retweets"] = newDataFrame["retweets"].apply(returnAnInteger).astype("int32")
newDataFrame["favorites"] = newDataFrame["favorites"].apply(returnAnInteger).astype("int32")

print("replies max: " + str(newDataFrame["replies"].max())) #these print functions will calculate the max/mean for each and will give the desired output
print("replies mean: " + str(newDataFrame["replies"].mean()))
print("retweets max: " + str(newDataFrame["retweets"].max()))
print("retweets mean: " + str(newDataFrame["retweets"].mean()))
print("favorites max: " + str(newDataFrame["favorites"].max()))
print("favorites mean: " + str(newDataFrame["favorites"].mean()))

#####
# Problem 9
#####

newDataFrame.loc[0:2].head() #this will display the data before the function
def returnNoHtml(data):
    
    data = str(data) # this turns the data into string type
    dataThatHasBeenCleaned = re.sub("<.*?>", "", data)
    return dataThatHasBeenCleaned # this returns the cleaned data
newDataFrame["text"] = newDataFrame["text"].apply(returnNoHtml)
newDataFrame.loc[0:2].head() # this will display the data after the html data has been removed

#####
# Problem 10
#####

dataFrameSubset = pandas.DataFrame() #this creates a new empty data frame
dataFrameSubset = newDataFrame
del(dataFrameSubset["url"]) #this deletes the url column
del(dataFrameSubset["user"]) #this deletes the user column
dataFrameSubset = dataFrameSubset[(dataFrameSubset["replies"] > 50000)]
dataFrameSubset.loc[0:2].head()
dataFrameSubset.to_excel("dataFrameSubset.xlsx") #this exports the new data set as an Excel file

