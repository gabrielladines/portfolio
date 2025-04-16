# Task 1:

# This is incorrect as you need to use " " at the beginning and end of your string.
# print(Hello amazing student!) 
print("Hello amazing student!")

# prompting user to give an input to Python.
language = input("What is your favourite programming language? ")
name = input("What is your name? ")
print(name, 'loves', language + '!')
# Gabriella loves Python!
# we have used ' around the word loves because it prints a string to python, and allows
#  python to interpret the string and print the string. without ' an error would come up as
# the word loves has not been defined, it is not inside any variable.
# , is used to seperate the values, the + will directly 'add' the string to the value.

# Task 2:

# a float (decimal number) as a variables value
pi = 3.14159
radius = 2
# the value of variable pi times by 2 to the power of 2 (value of radius (2)^2 = 4). This value has been stored into the variable area.
area = pi * (radius**2)
print(area)

# try changing the radius and running the code again. is your printed answer different?

pi = 3.14159
radius = 3
# area of circle equation <- this is a comment
area = pi * (radius**2)
print(area)
# area value has changed as it has used a different mathematical int value in radius.

# now type the following underneath your original code:

pi = 3.14159
radius = 2
area = pi * (radius**2)
print(area)
# the value of radius has been incremented by 1. It has rebounded the value by adding 1 to it therefore it now possesses the value 3 and therefore the maths changes after the second print.
radius = radius + 1
print(area)
area = pi*(radius**2)
print(area)
# What do you notice about the different printed values. Why is this?
# the first print statement is printing the value of area (pi * radius **2 = 2**2 = 4 = pi*4)
# the second print statement is the same value as the first print statement, even though
# radius has been rebounded to 3. that is because python executes code in order from
# top to bottom. therefore, as you are asking python to print the area, not the radius,
# the area will only refer to the radius value that is given by that line of code, not
# after. In the final print statement, however, because area variable has been reboundes
# after the rebounded radius variable, it can then update and use the new radius accordingly
# hence having a new value in the final print statement in the terminal.

# Task 3:

# Write a program that does the following in order:
# 1. Asks the user to enter a number "x"
# 2. Asks the user to enter a number "y"
# 3. Prints out number "x", raised to the power "y"
# 4. Prints out the log (base 3) of "x"

# imported a sophisticated library called 'math' from Python which has a lot of pre-made code that aids in your mathematical Python requestions.
import math
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
# here in print, the int is converted into a string so that it is easy for Python to understand that you want it to print the whole sentence including the values and to not get conflicted with the mix of variable types i.e. strings and ints in the same print statement.
print("The following number represents your first number to the power of your second number:", str(x**y))
print("The following number represents the log of your first number with wit base 3:", str(math.log(x, 3)))

# What do you need to think about in terms of values the user inputs?

# In the print statement, as you are inserting two different object types (string and int), 
# python shows an error, as a print statement can not have mixed objects, it needs to be 
# converted a string, as python needs consistent objects type in blocks of code that are 
# getting executed. This is done via adding a , after your string, then converting the int
# into a str().

# Extension: Write your own program and complete your own reflective lof for week 1.

# prompting the user to give python some input. In this case it is a string of your name.
name = input("What is your name? ")
# here an int is required from the user input. In this case Python is asking the user for the int of their birth year.
year_born_in = int(input("What year was you born in? "))
# using maths to calculat the age of the user in this current year that they are/will/would have been.
age = 2025 - year_born_in
print("Hello,", name + ",","I see that you are", + age, "this year.")
study = input("What are you studying? ")
# a float number is required as the user is to express the money they spent with a decimal. This is also for more accuracy to calculate (in next lines of code) how much money the user could have saved, for example.
travel_spend = float(input("How much did you spend to and from travel to London Metropolitan University on 07/02/25? "))
could_save = float(travel_spend) - 3.5
print("Hello,", name + ".","I see that you are", age,"this year. You are studying", study + ".", "On the 07/02/25 you spent £" + str((travel_spend)) + " for a tube and bus fare.", "The cheapest price for you to pay to travel to and from Univerisity is £3.50 via two buses there and back. As you took the tube that day, you spent: £" + str((travel_spend)) + ", but you could have saved: £" + str((could_save)) + " had you taken just two buses instead.")
# space automatically with , and no space automatically with +.