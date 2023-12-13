# -*- coding: utf-8 -*-
"""
Created on 10/01/23 11:24 am

@author: Garrett Daily
"""

#####
##### COMPARISON OPERATORS
#####

"""
    https://docs.python.org/3/reference/expressions.html#comparisons
    Comparison operators are used to compare two objects on either side of the comparison operator and return either True or False to the relationship
    <   (is the value on the left side LESS THAN the value on the right side of the operator)
    >   (is the value on the left side GREATER THAN the value on the right side of the operator)
    ==  (is the value on the left side EQUAL TO the value on the right side of the operator)
    >=  (is the value on the left side GREATER THAN OR EQUAL TO the value on the right side of the operator)
    <=  (is the value on the left side LESS THAN OR EQUAL TO the value on the right side of the operator)
    !=  (is the value on the left side NOT EQUAL TO the value on the right side of the operator)
"""

# technically, these can be used stand alone, but they are not very useful that way...
x = 5
y = 3
print(x > y)
print(x < y)

#####
##### CONDITIONAL LOGIC
#####

"""
    Conditional logic in programming is really what starts to make our programs more useful
    Decision making is part of everyday programming (and life) and can range from very straightforward and simple, to very complex (this is usually a source of "logic errors")
    In Python (and most programming languages), if / if else / if else-if / if else-if else (can many other combinations) statements implement the conditional logic for purposes of decision making 
    - if        (a condition is true, run some code; otherwise, do nothing)
    - if else   (a condition is true, run some code; else, run some other code)
    - if else   (a condition is true, run some code; else, run some other code)
"""

# the structure of an IF statement needs attention to detail 
# in English, the next line reads "if the condition x > y evaluates to True, then run the indented code following the colon (until there is no more indented code)
if (x > y):
    print("yes, x is greater than y")
    
# ERROR - an if statement must have at least one statement that will occur in the case the condition evaluates to True
if (x > y):
print("yes, x is greater than y")

# another example - notice no () around the condition - this works, but in more complex conditional tests, this is a bad practice - don't do it - use () around the condition
if x > y:
    print("yes, x is greater than y")

# if you have multiple statements that you would like to conditionally execute:
if (x > y):
    print("x: " + str(x))
    print("y: " + str(y))
    print("yes, x is greater than y")

# pay CLOSE attention to your indentation:
# notice errors if the indentation does not match - the statement must be hard left if you want it out of the if block of code; otherwise, the indentation must match
x = 1 
y = 2 
if (x > y):
    print("x: " + str(x))
    print("y: " + str(y))
    print("yes, x is greater than y")

# else - meaning "otherwise"

# if the condition is true, run the first part of the code; otherwise, run everything after the else (that is correctly indented)
if (x > y):
    print("x: " + str(x))
    print("y: " + str(y))
    print("yes, x is greater than y")
else:
    print("x: " + str(x))
    print("y: " + str(y))
    print("no, x is NOT greater than y")

# now, evolve your code - this is something too often not thought about - eliminate redundant code since it is unnecessary
# what is repeated in the previous example?
print("x: " + str(x))
print("y: " + str(y))

# if the condition is true, let it be known; otherwise, state that it is not true; the other commands occurred in either situation so they were not conditional
# non-conditional statement should not exist in the if statement structure 
# either way, we wanted to show what values were assigned to x and y so we moved those statements outside of the if structure
if (x > y):
    print("yes, x is greater than y")
else:
    print("no, x is NOT greater than y")

# an if statement allows for one path of code to be taken - "if true, do this"
# an if else combination allows for two paths of code to be taken - "if true, do this; OTHERWISE, do this other thing"

# what is we want three paths?
# elif "else if" allows for additional path(s) to be taken by evaluating additional conditions and executing the extra code path if True
# PAY CLOSE ATTENTION TO THE ELSIF HERE: I can't stress the importance enough here == means are they equal which is VERY DIFFERENT than the assignment operator =
x = 2 
y = 2 

if (x > y):
    print("yes, x is greater than y")
elif (x == y):
    print("x is equal to y")
else:
    print("no, x is NOT greater than y")

# what if we want additional paths? you can always introduce more "elif" statements - let's change the example to make this more obvious
grade = 90  
if (grade >= 90):   
    print("A-")
elif (grade >= 80):
    print("B-")
elif (grade >= 70):
    print("C-")
else: 
    print("major issue")

# use caution when implementing your conditional logic - here if somebody gets a 90, the first condition is true and they are assigned a "C-" even though it should have been an "A-"
# the two "elif" statements will never occur since any time the grade is >= 80 or >=90, the first condition is always true
# you must think about the flow of the conditional tests that you want to perform
if (grade >= 70):
    print("C-")
elif (grade >= 80):
    print("B-")
elif (grade >= 90):
    print("A-")
else:
    print("major issue")

# what if we want more granularity? e.g. 93-100 = A, 87-90 = B+, 83-87 = B, etc.
# we could just keep adding (in correct order) "elif" statements, but let's check out other options


#####
##### NESTED IF
#####

"""
    Sometimes you need more control over your decision making with conditional logic - this is where nesting comes in
    Nesting conditional tests within conditional test is a way to do this
"""
grade = 92.9999
if (grade >= 90):
    if (grade >= 93):   
        print("A-")
    else:   
        print("A-")
elif (grade >= 80):
    if (grade >= 83):
        print("B")
    else:   
        print("B-")
elif (grade >= 70):
    if (grade >= 73):
        print("C")
    else:   
        print("C-")
else:   
    print("major issue")

# why would you do it this way? couldn't we just do a series of elif (see the following code) 
# what if we had awards that we gave out for the initial tiers (e.g. >90 free ice cream (or apples ;) for a month, >80 free for a week, >70 1 cone (or apple))
# think back to the duplication issue - we have some duplicate code that I have provided below - this is typically where issues come in due to inconsistencies in intended duplicate code


grade = 90
if (grade >= 93):
    print("A")
    print("free for a month")
elif (grade >= 90):
    print("A-")
    print("free for a month")
elif (grade >= 83):
    print("B")
    print("free for a week")
elif (grade >= 80):
    print("B-")
    print("free for a week")
elif (grade >= 73):
    print("C")
    print("free item")
elif (grade >= 70):
    print("C-")
    print("free item")
else:
    print("no award")


# let's copy your previous nested if example and add the ice cream or apple example - less room for error due to eliminating duplicated code since the messages are written only once
grade = 60
if (grade >= 90):
    print("free for a month")
    if (grade >= 93):
        print("A")
    else:
        print("A-")
elif (grade >= 80):
    print("free for a week")
    if (grade >= 83):
        print("B")
    else:
        print("B-")
elif (grade >= 70):
    print("free item")
    if (grade >= 73):
        print("C")
    else:
        print("C-")
else:
    print("no award")


#####
##### LOGICAL OPERATORS
#####

"""
    We can expand on our conditional logic by introducing logical operators - somewhat similar to comparison operators, they will let us compare two (or more) conditional statements
    and (returns True if BOTH statements are true     5>3 and 3<4 is True;   5<3 and 3>4 is False)
        basically: True and True is True; anything other than that is False
    or  (returns True if EITHER statements are true   5<3  or 3<4 is True;   5<3  or 3>4 is False)
        basically: True or True is True; True or False is True; False or True is True; False or False is False
    not (returns the opposite of whatever the logical operator test returned - so in the previous example: not(5>3 and 3<4) is False
         this is tricky based on the not(5>3 and 3<4) - I would suggest avoiding this type of use typically
         however, it is really useful if you want to test the state of a boolean variable
         for example, you create a boolean variable call "todayIsSunny" and set it equal to True
         if you say not(todayIsSunny) - this is same as saying today is not sunny (or the same as saying todayIsSunny is False)
"""

# conditional logic can be expanded by using logical operators in the conditional test
# let's copy the previous example:
# what if we kept track of if it is a first-time award in a boolean variable
firstTimeAward = False

# how do we use that? it seems like the logic is already pretty complex - this is where logical operators come in (in this case "and")
grade = 90
if (firstTimeAward and grade >= 90):
    print("free for a month")
    if (grade >= 93):
        print("A")
    else:   
        print("A-")
elif (firstTimeAward and grade >= 80):
    print("free for a week")
    if (grade >= 83):
        print("B")
    else:   
        print("B-")
elif (firstTimeAward and grade >= 70):
    print("free item")
    if (grade >= 73):
        print("C")
    else:   
        print("C-")
else: 
    print("no award")

# let's copy the previous example and change the boolean variable to demonstrate the NOT logical operator
# instead, what if we kept track of if the award was previously received in a boolean variable
# how do we use that? it has the opposite context of what was implied with firstTimeAward
# e.g. firstTimeAward = True would imply hasStudentReceivedAwardBefore = False (this will force us to use the not operator)
    
hasStudentReceivedAwardBefore = False
grade = 90
if (not(hasStudentReceivedAwardBefore) and grade >= 90):
    print("free for a month")
    if (grade >= 93):
        print("A")
    else:   
        print("A-")
elif (not(hasStudentReceivedAwardBefore) and grade >= 80):
    print("free for a week")
    if (grade >= 83):
        print("B")
    else:   
        print("B-")
elif (not(hasStudentReceivedAwardBefore) and grade >= 70):
    print("free item")
    if (grade >= 73):
        print("C")
    else:   
        print("C-")
else: 
    print("no award")
  
# let's copy the previous example and test the OR logical operator
# if somebody gets a grade of 100, let's ignore the fact that they may have received the award before
# or can be used in a combination with an existing complete conditional test - look at the initial if statement
    
# if (not(hasStudentReceivedAwardBefore) and grade >= 90):
# translate it to English (this is something you should always do from a validation standpoint - actually it is better to start with English and THEN try to translate to code)
# "if the student has not received the award before and their grade is 90 or above, give them the award"

# what if we wanted to have a second clause that said:
# "if they get a grade of 100, they will get the award no matter what"

# we can use OR logical operator to help us here:
# condition1 is true OR condition2 is true ----- then give them the award

# this is where using () is a must

# condition1 = (not(hasStudentReceivedAwardBefore) and grade >= 90)
# condition2 = (grade == 100)           # which says "is the grade equal to 100"

# if (condition1 OR condition2)

# remember to change the grade to 100

hasStudentReceivedAwardBefore = True
grade = 100
if ((not(hasStudentReceivedAwardBefore) and grade >= 90) or (grade == 100)):
    print("free for a month")
    if (grade >= 93):
        print("A")
    else:   
        print("A-")
elif (not(hasStudentReceivedAwardBefore) and grade >= 80):
    print("free for a week")
    if (grade >= 83):
        print("B")
    else:   
        print("B-")
elif (not(hasStudentReceivedAwardBefore) and grade >= 70):
    print("free item")
    if (grade >= 73):
        print("C")
    else:   
        print("C-")
else: 
    print("no award")



#####
##### WRITING YOUR OWN FUNCTIONS
#####

"""
    Any time that you want to re-use code, encapsulating it in your own function is likely a good solution and pretty easy to do
"""

# the structure of a function is like this:
"""
def FunctionName():
    "describe what the function does here"
    # any code you want to run goes here
    # then we "return"
    return
"""

# copy the previous example and create the following function called DetermineAwardVersion1 (paste your code like mine - NOTICE how you have to deal with indentation)
def DetermineAwardVersion1():
    "This function determines the award"

    hasStudentReceivedAwardBefore = True
    grade = 100
    if ((not(hasStudentReceivedAwardBefore) and grade >= 90) or (grade == 100)):
        print("free for a month")
        if (grade >= 93):
            print("A")
        else:   
            print("A-")
    elif (not(hasStudentReceivedAwardBefore) and grade >= 80):
        print("free for a week")
        if (grade >= 83):
            print("B")
        else:   
            print("B-")
    elif (not(hasStudentReceivedAwardBefore) and grade >= 70):
        print("free item")
        if (grade >= 73):
            print("C")
        else:   
            print("C-")
    else: 
        print("no award")

    return

# how you can call your function:
DetermineAwardVersion1()
 
# see if the function gives you details on what it does
print(DetermineAwardVersion1.__doc__)

# try other functions - you get the idea now
print(dir.__doc__)

# let's make the function more useful - it would be good if we could pass it the grade and if the student has received the award
# copy DetermineAwardVersion1 and rename it to DetermineAwardVersion2
def DetermineAwardVersion2(hasStudentReceivedAwardBefore, grade):
    "This function determines the award based on the grade and prior award status"

   #hasStudentReceivedAwardBefore = True
   #grade = 100
    if ((not(hasStudentReceivedAwardBefore) and grade >= 90) or (grade == 100)):
        print("free for a month")
        if (grade >= 93):
            print("A")
        else:   
            print("A-")
    elif (not(hasStudentReceivedAwardBefore) and grade >= 80):
        print("free for a week")
        if (grade >= 83):
            print("B")
        else:   
            print("B-")
    elif (not(hasStudentReceivedAwardBefore) and grade >= 70):
        print("free item")
        if (grade >= 73):
            print("C")
        else:   
            print("C-")
    else: 
        print("no award")

    return

# call your new function
DetermineAwardVersion2()

# notice how it tells you missing 2 required positional arguments: 'hasStudentReceivedAwardBefore' and 'grade'
# call you function again, but this time pass it the required data
DetermineAwardVersion2(True, 100)

# test it a few times
DetermineAwardVersion2(True, 90)
DetermineAwardVersion2(True, 70)
DetermineAwardVersion2(True, 50)
DetermineAwardVersion2(False, 90)
DetermineAwardVersion2(False, 85)
DetermineAwardVersion2(False, 65)
