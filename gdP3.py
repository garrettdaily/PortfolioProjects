# -*- coding: utf-8 -*-
"""
Created on 10/20/23 8:49pm

@author: Garrett Daily
"""


#####
##### USING PANDAS TO WORK WITH DATA
#####

"""
    We have previously seen how we can work with external data (csv module) and use our understanding of various code structures (like loops) to work with that data.
    Working with external data has become such a common requirement there are a significant number of modules that have been created to make working with data easier.
    One of the most popular data modules is pandas which provides easy-to-use data structures and data analysis tools
    
    pandas user guide: https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html
"""

# to better understand the pandas data structure, let's start with an example that we have previously worked with, a dictionary
# in this case the dictionary is set up to contain customerIds, zip codes, and state data

dictionaryWithCustomerData = {"customerId":[1,2,3], "zip":[43147,30303,30303], "state":["OH","GA","WI"]}

# we can list the keys and values:
dictionaryWithCustomerData.keys()
dictionaryWithCustomerData.values()

# and get data for a specific key:
dictionaryWithCustomerData["customerId"]

# to use pandas, we will import the module:
import pandas

# take a look at what functions are available
dir(pandas)

# in pandas, the dictionary can be used to create a data frame which is one of the most common structures that we will work with
dataFrameWithCustomerData = pandas.DataFrame(dictionaryWithCustomerData)
type(dataFrameWithCustomerData)

# and get data for a specific column (which was the key for our dictionary):
dataFrameWithCustomerData["customerId"]

# just as a reminder about how to create an alias for a module
# note, in pandas own documentation and examples, it is very common for the "as" operator to be used in the import command
import pandas as pd
dataFrameWithCustomerData = pd.DataFrame(dictionaryWithCustomerData)
dataFrameWithCustomerData["customerId"]

# just a reminder - set our working directory
import os
print(os.getcwd())
os.chdir("C:\\Users\\garre\\OneDrive\\Documents\\Desktop\\MIS\\p5")

#####
##### READING IN EXTERNAL DATA INTO DATAFRAMES
#####

"""
    pandas has support for a LARGE number of external data sources including CSV, JSON, Excel, SQL databases, and many more
    check them out here: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
"""

# read in the external CSV data
dataFrameWithSalesData = pandas.read_csv("data.csv")
# read in the Excel based data (just the same dataset)
dataFrameWithSalesData = pandas.read_excel("data.xlsx")

# display the contents of the dataframe
print(dataFrameWithSalesData)

# display the contents based on the index column value using the zero-based index value of the first record
print(dataFrameWithSalesData.loc[0])

# or if we want to set an index column based on a column in the data
dataFrameWithSalesData = pandas.read_csv("data.csv", index_col=0)
dataFrameWithSalesData = pandas.read_csv("data.csv", index_col="customerId")

# notice how the index value is now the customerId - which is not zero-based
print(dataFrameWithSalesData)

# this will produce a KeyError since we do not have a customerId = 0
print(dataFrameWithSalesData.loc[0])

# we have to reference a valid customerId
print(dataFrameWithSalesData.loc[1])

# let's let the index be created automatically
dataFrameWithSalesData = pandas.read_csv("data.csv")

# now notice the limited output
print(dataFrameWithSalesData)

# we can override the output
pandas.set_option("display.max_columns", None)
pandas.set_option("display.max_rows", None)
print(dataFrameWithSalesData)

# or restrict it - up to you
pandas.set_option("display.max_columns", 5)
pandas.set_option("display.max_rows", 10)
print(dataFrameWithSalesData)

# look at an individual column of data - this is referred to as a series in pandas terminology
dataFrameWithSalesData["salesVolume"]
type(dataFrameWithSalesData["salesVolume"])

# stat functions - just some example - look here for a bigger list: https://pandas.pydata.org/pandas-docs/stable/user_guide/computation.html#statistical-functions
dataFrameWithSalesData["salesVolume"].min()
dataFrameWithSalesData["salesVolume"].max()
dataFrameWithSalesData["salesVolume"].sum()
dataFrameWithSalesData["salesVolume"].mean()
dataFrameWithSalesData["salesVolume"].median()
dataFrameWithSalesData["salesVolume"].mode()

# take a look at functions available on the dataframe
dir(dataFrameWithSalesData)
dataFrameWithSalesData.columns
dataFrameWithSalesData.dtypes
dataFrameWithSalesData.info()
dataFrameWithSalesData.head()
dataFrameWithSalesData.tail()
dataFrameWithSalesData.shape
dataFrameWithSalesData.describe()
dataFrameWithSalesData["income"].describe()
dataFrameWithSalesData["city"].describe()
dataFrameWithSalesData["city"].value_counts()
# compute covariance and correlation matrices - https://pandas.pydata.org/pandas-docs/stable/user_guide/computation.html#statistical-functions
dataFrameWithSalesData.cov()
dataFrameWithSalesData.corr()

# if we want to identify missing values: https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
dataFrameWithSalesData.isna().sum()
dataFrameWithSalesData.notna().sum()

# use this with caution - if you want to remove rows with missing values
# notice this just displays the dataset with any rows that have missing values removed
dataFrameWithSalesData.dropna()

# if we wanted to make this the data set moving forward we need to create a new dataframe, or reassign it
dataFrameWithSalesDataVersion2 = dataFrameWithSalesData.dropna()
dataFrameWithSalesDataVersion2

# this would be re-assigning the dataset with the removed rows
dataFrameWithSalesData = dataFrameWithSalesData.dropna()

# we don't want to do that so go ahead and re-load the dataset
dataFrameWithSalesData = pandas.read_csv("data.csv")

# if you want to build a new dataframe from a subset of the data
dataFrameSubset = dataFrameWithSalesData[['city', 'state', 'zip']]
dataFrameSubset

# if you want to manually add data to a dataframe - this would not be something that you would likely construct manually like this
# it would very likely be something that you would only build within a loop that was programmatically pulling the data from some location
# I am providing it only as an example that you can uncomment to test it out

dataFrameWithNewData = pandas.DataFrame({
    "customerId":13,
    "zip":[45701],
    "city":["Athens"],
    "state":["Ohio"],
    "income":[40000],
    "salesVolume":[70],
    "preferredCustomerStatus":["x"]})

# we can use an append function to add the new dataframe to our existing one
dataFrameWithSalesData = dataFrameWithSalesData.append(dataFrameWithNewData, ignore_index = True)
# verify that it was added
dataFrameWithSalesData



#####
##### CONDITIONALLY FINDING DATA
#####

"""
    A huge benefit to working with pandas is how it allows you to find data - rather than having to create a loop to look for data, we can just ask the dataframe to return data conditionally (or not)    
    here we can rely on our understanding of conditional tests and comparison operators that we have previously looked at (e.g. == != > <)
    https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
"""

# we already saw how we can use the index number:
dataFrameWithSalesData.loc[0]

# we can also return data based on a range:
dataFrameWithSalesData.loc[0:4]

# retrieving data based on a conditional test - this is not useful by itself
dataFrameWithSalesData["city"] == "Athens"

# but it is in the context of the dataframe - show all data where the city is Athens
dataFrameWithSalesData[dataFrameWithSalesData["city"] == "Athens"]

# and where the city is not Athens
dataFrameWithSalesData[dataFrameWithSalesData["city"] == "Athens"]

# where the sales volume is greater than 50
dataFrameWithSalesData[dataFrameWithSalesData["salesVolume"] > 50]

# compound conditional statements - this is where it is a little different, but not much
# the operators for compound conditional test are "&" (which means "and")
# and "|" (which means "or" - that is the pipe operator found above your enter key)

# return a dataframe where the city is Athens and the state is Ohio
dataFrameWithSalesData[(dataFrameWithSalesData["city"] == "Athens") & (dataFrameWithSalesData["state"] == "Ohio")]

# return a dataframe where the city is Athens and the state is GA
dataFrameWithSalesData[(dataFrameWithSalesData["city"] == "Athens") & (dataFrameWithSalesData["state"] == "GA")]

# return a dataframe where the city is not Athens and the state is not Ohio and the salesVolume is greater than 50
dataFrameWithSalesData[(dataFrameWithSalesData["city"] != "Athens") & (dataFrameWithSalesData["state"] != "Ohio") & (dataFrameWithSalesData["salesVolume"] > 50)]


#####
##### TRANSFORMING DATA
#####

"""
    Understanding how to manipulate and transform your dataset is an important aspect of any data analysis.
    With a little programming and some help from functions available to our dataframe, pandas makes transforming data much easier than manually looping through the data and performing inline data conversions.
"""

# in order to understand how to transform data, we will start with the .astype method of the dataframe
# first take a look at the data types again:
dataFrameWithSalesData.info()
dataFrameWithSalesData["zip"] = dataFrameWithSalesData["zip"].astype('int')
dataFrameWithSalesData.info()
dataFrameWithSalesData["zip"] = dataFrameWithSalesData["zip"].astype('int64')
dataFrameWithSalesData.info()
dataFrameWithSalesData["zip"] = dataFrameWithSalesData["zip"].astype('int32')
dataFrameWithSalesData.info()

# notice how income is an "obect" - basically in contained non-numeric data, so it was classified as a string, which pandas datatype is an "object"
dataFrameWithSalesData["income"] = dataFrameWithSalesData["income"].astype("int")

# missing data is not an issue, it is the "$" and "," that are in the data
dataFrameWithSalesData["income"]

# so we have a problem from an analysis perspective - we can use the statistical functions on the income data
dataFrameWithSalesData["income"].mean()

# we could use the variable explore to manually fix the data - but this is not going to work for very large dataset


##### 
##### REGULAR EXPRESSIONS
##### 

"""
    Regular expressions are something that every programmer needs to be aware of and likely use to help transform data
    Here is the Python library reference for regular expressions and usage:     https://docs.python.org/3/library/re.html
    They can be used to replace data, remove data, change the state of data (like lower to upper case), and are good for pattern matching
"""

# to use regular expressions, we will need to import the re module
import re

# next, let's look at a basic example:
stringExampleBefore = "$66,000"

# we cannot convert that to an integer
int(stringExampleBefore)

# let's take stringExample and using the re.sug function we will remove any data that is NOT a number: ^0-9
stringExampleAfter = re.sub("[^0-9]", "", stringExampleBefore)
print("value before re: " + stringExampleBefore + " and the value after re: " + stringExampleAfter)

# notice the data has been cleaned and can now be converted to an integer
int(stringExampleAfter)

# pandas makes it easy to send your data through functions that you define
# for example, let's create a function that will accept some data, pass it through our regular express, and return that cleaned data
def returnAnInteger(data):
    
    data = str(data)
    dataThatHasBeenCleaned = re.sub("[^0-9]", "", data)
    return dataThatHasBeenCleaned

# see if we can apply the returnAnInteger function to the income data
dataFrameWithSalesData["income"].apply(returnAnInteger).astype("int")

# we get an error - why? it is due to the NaN value in our data
# the regular expression is expecting some data for it to work - in this case, NaN represents no data, which makes the re fail
# let's go back to a previous example where we looked for missing values - we decided not to drop the missing values so we still have them in the dataframe
dataFrameWithSalesData.isna().sum()


#####
##### DEALING WITH MISSING VALUES
#####

"""
    Missing values are not always bad, but you need to think about what they mean and how they may affect your analysis.
    From a process perspective, you should investigate how the missing values occurred, or why they were allowed in the first place.
    In this section, we will look at 2 basic techniques for detail with the missing data (since we previously decided not to drop the rows with missing values)
"""

# we can fill the missing values as a temporary transformation to the data
dataFrameWithSalesData["income"].fillna("missing")

# but if our goal is to have the column data converted to an integer, the "missing" data should be numeric
# it is a common practice to use a 0 for missing values, but this is a case-by-case basis - from an analysis perspective, you will need to think about what that means
dataFrameWithSalesData["income"].fillna(0)

# let's go ahead and make the change for the missing values to be stored as a 0, so we must re-assign that series (column) in the data set
dataFrameWithSalesData["income"] = dataFrameWithSalesData["income"].fillna(0)

# now let's see if our function works
dataFrameWithSalesData["income"].apply(returnAnInteger).astype("int")

# now re-assign the coverted integer data in the income series
dataFrameWithSalesData["income"] = dataFrameWithSalesData["income"].apply(returnAnInteger).astype("int")

# statistical functions will now work on the income data
dataFrameWithSalesData["income"].mean()

# Filling in missing values is easy with pandas. We can also introduce other techniques for replacing the 0 values.
# For example, let's take the mean of the income (which is now possible since it has a numeric data type) and use that value to replace any instance of 0
# To do this, it will require another module (actually pandas already uses it, but we will import it directly)
import numpy

# look at the existing data - notice the 0
dataFrameWithSalesData["income"]

# this is the value we want to use to replace 0
dataFrameWithSalesData["income"].mean()

# that value would be stored as a float rather than an integer
# this is not a problem, but if you want to keep the data as an integer, we can do that with a couple of extra steps
# round the data to 0 decimal places
incomeMean = round(dataFrameWithSalesData["income"].mean(), 0)
# now make it an integer
incomeMean = int(incomeMean)
# check the type and confirm that it is an integer
type(incomeMean)

# this is how we will perform that transformation - this won't re-assign the data yet, just show us what it will look like
numpy.where(
        dataFrameWithSalesData["income"] == 0,
        incomeMean,
        dataFrameWithSalesData["income"])

# now apply the transformation and re-assign the income series with the updated data
dataFrameWithSalesData["income"] = numpy.where(
        dataFrameWithSalesData["income"] == 0,
        incomeMean,
        dataFrameWithSalesData["income"])

# check out the tranformation
dataFrameWithSalesData["income"]

# now another quick transformation - notice the missing values for our preferredCustomerStatus column
# the x implies the customer has preferred status, and the missing value implies that status is not yet preferred
dataFrameWithSalesData["preferredCustomerStatus"]

# when you have a binary situation, treat the data as boolean - if that is the case, let's make the data true/false
# numpy where function to the rescue - check out the output only
numpy.where(
        dataFrameWithSalesData["preferredCustomerStatus"] == "x",
        True,
        False)

# store the transformed data - notice, you can write out the where function on one line - for short examples, this is my preference, for more complex examples, I would recommend multiple lines like previously demonstrated
dataFrameWithSalesData["preferredCustomerStatus"] = numpy.where(dataFrameWithSalesData["preferredCustomerStatus"] == "x", True, False)

# check out the transformation - notice how the datatype is now boolean - this was done for us given that the data used Python keywords True and False:
dataFrameWithSalesData["preferredCustomerStatus"]
dataFrameWithSalesData.dtypes

#####
##### TRANSFORMING DATA USING EXTERNAL DATASETS
#####

"""
    Many times you might have a known good dataset which you would like to replace some values within your current working dataset.
    For example, states may have been inconsistently entered with either a 2 letter abbreviation or as a full state name.
    If we have another dataset that we could join to our existing dataset given that we have some value that we can relate the datasets on, it is easy to do
"""

# notice inconsistent state names
dataFrameWithSalesData

# load in a good dataset containing city, state, zip data that has been cleaned or is at least considered to be good
dataFrameWithZipCodes = pandas.read_csv("zipCodes.csv")
dataFrameWithZipCodes.info()

# check out an instance of the data
dataFrameWithZipCodes.loc[0]
dataFrameWithZipCodes.loc[0]["city"]
dataFrameWithZipCodes.loc[0]["state"]

# notice how some of the zip codes are duplicated?
dataFrameWithZipCodes

# this will be a problem if we want to combine the datasets based on a related value
# in this case, we want to use the city and state out of the new dataset and we will relate the new to the existing dataset based on the "zip" column
# if the zipCodes.csv is considered to be good data, we can use it, but we need to make sure there are no duplicates in the data
# we can remove the duplicate row by calling drop_duplicates on the dataframe
dataFrameWithZipCodes.drop_duplicates()

# we need to re-assign the dataframe with the duplicates removed
dataFrameWithZipCodes = dataFrameWithZipCodes.drop_duplicates()

# next, we can merge the dataframes with an understanding of our goal
# our goal is to use the data from dataFrameWithZipCodes and where we can match the zip code in our dataFrameWithSalesData, 
# take the data from dataFrameWithZipCodes and list it in the match row dataFrameWithSalesData
# this can be a very complicated process depending on what you are trying to do - reading the documentation is a good place to start: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
pandas.merge(dataFrameWithSalesData, dataFrameWithZipCodes, on='zip', how='inner')

# because this process is complicated, I would recommend creating a new dataframe to store the new dataset, just so you don't have to rebuild dataFrameWithSalesData from scratch if you mess something up
dataFrameWithSalesDataWithNewData = pandas.merge(dataFrameWithSalesData, dataFrameWithZipCodes, on='zip', how='inner')

# check it out and notice the new and re-named column names
dataFrameWithSalesDataWithNewData

# we can change column names easily
dataFrameWithSalesDataWithNewData.rename(columns = {"city_y":"city", "state_y":"state"}, inplace=True)
dataFrameWithSalesDataWithNewData.columns

# we can remove columns with a del funciton
del(dataFrameWithSalesDataWithNewData["city_x"])
del(dataFrameWithSalesDataWithNewData["state_x"])

# check out the dataset
dataFrameWithSalesDataWithNewData


#####
#####   STORING TRANSFORMED DATA
#####

"""
    Now that you have done all of the work that you want to with the data, the transformed dataset can be stored in many formats very easily with the functions provided by pandas
    You can explore the various output writers provided by the pandas module here: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
"""

# saving datasets to external files
dataFrameWithSalesDataWithNewData.to_csv('cleanedData.csv')

# notice the index column - we can easily remove it - make sure you close the file that you just created before trying to re-save or you will get a permission denied error message
# extra details here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
dataFrameWithSalesDataWithNewData.to_csv('cleanedData.csv', index=False)

# other common formats
dataFrameWithSalesDataWithNewData.to_excel("cleanedData.xlsx")
dataFrameWithSalesDataWithNewData.to_json("cleanedData.json")
