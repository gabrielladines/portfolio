# Week 3 Tutorial

# Task 1: 

# assigning a string value to a variable:
s1 = "cat u rock" 
# assigning a string value to another variable:
s2 = "i help cat"
# is statement that checks the length of the string from variable s1, if it is equal to the length of the string in s2
if len(s1) == len(s2):
        # if the if statement is true, it enters a for loop and walks through each character (in this case, not the white space)...
        for char1 in s1:
            # an extension of the condition is to loop through the charcaters of the string stored in s2...
            for char2 in s2:
                # as Python loops through the characters of both strings stored in s1 and s2, it checks another condition set by the if statement, to check if there are characters that are in common with each string...
                if char1 == char2:
                    # as s1 and s2 have 3 of the same type of character in each string that appears twice, the print function has been instructed to print a statement according to the conditons of the if statement.
                    print("common letter")
                    # breaking the loop once all conditions and instructions have been met. without break, Python will loop through again to check if condition is false, so will print statement twice to account for both variables taken into considerationin the nested for.
                    break

# Task 2:

# Type the following and save as a .py file with a sensible name:
an_letters = "aefhilmnorsxAEFHILMNORSX"
# taking user input to cheer a word.
word = input("I will cheer for you! Enter a word: ")
# the int the user inputs will correlate with how many cheers they will recieve.
times = int(input("Enthusiasm level (1-10): "))
# counter
i = 0
# entering a while loop where python checks if the length of the word the user inputed is less than the counter. As the counter (i) starts at 0, it is expected that the condition is met.
while i < len(word):
    # this variable rebounds the varibale word with i, so you are inserting the data from word into char.
    char = word[i]
    # because of this you are able to check if any of the characaters from user input are in an_letters.
    if char in an_letters:
        # if the user input possesses the characters in an_letters, it will print "Give me an (first character of user input)! (first character of user input)"
        print("Give me an " + char + "! " + char)
        # if the user gives other characters that is not possessed in an_letters, still executes same action as above.
    else:
        print("Give me a " + char + "! " + char)
        # i gets incremented by 1 as to tell the loop to go to the next letter.
    i += 1
print("What does that spell?")
# i is entered into a for loop with a range that refers to the range of times varible from user input. 
for i in range(times):
    # it will print the word the user inputs in the range of how much enthusiasm the user inputed.
    print(word, "!!!")

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
# this code executes the same kind of functionality but with a for loop, making it more pythonic as it does not need the extra adjustments a while loop usually needs.
for char in word:
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
print("What does that spell?")
for i in range(times):
    print(word, "!!!")


# Task 3:

# Question 1
cubed2 = int(input("Input a int: "))
# abs keeps the number positive
cubed = abs(cubed2)
# for loop is taking a range of cubed (cubed2 user input) and adding 1.
for i in range(cubed + 1):
    # inserting an if statement as a condition where if i cubed (range(cubed + 1)) is more than or equal to the cubed then to end the loop via break function.
    if i**3 >= cubed:
        break
    #another condition if i cubed does not equal to cubed, then it will print the statement that it is not a perfect cube.
if i**3 != cubed:
    print("This is not a perfect cube.")
    # To let the user know what the cubed of their user input is.
    print("Square root of", cubed, "is", i)
# if conditions are not met in if statements above, Python will go to the condition following the else statment.
else:
    if cubed2 < 0:
        # it remounds user input to a positive number using mathematical logic (two negatives equal a positive).
        i = - i
        print("Cubed root of", cubed2, "is", i)
    else:
        print("Cubed root of", cubed2, "is", i)

# Question 2:
# taking user input as a float. IT will convert the number they give into a float.
cubed2 = float(input("Enter a number you wish to find the square root of: "))
# abs keeps number a positive.
cubed = abs(cubed2)
# epsilon to
epsilon = 0.01
# guess count starts at 0.0
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cubed) >= epsilon:
    # guesses get incremented by 0.0001 
    guess += increment
    # increments number of guesses by 1 to track  how many guesses it takes for Python to guess.
    num_guesses += 1
print("Number of guesses =", num_guesses)
if abs(guess**3 - cubed) >= epsilon:
    print("Failed on square root of", cubed)
else:
    if cubed2 < 0:
        # converts the guess to a positive float
        guess = -guess
        print(guess, "is close to the square root of", cubed2)
    else:
        print(guess, "is close to the square root of", cubed2)

# Question 3
# setting a variable that requires a number from the user. The number gets converted into a float.
cubed = float(input("Enter a positive number greater than 1 to find the cubed root of: "))
# epsilon to 'cap' or 'round' needed for while loop, as to allow answer to keep on going until it reaches high enough accuracy.
epsilon = 0.01
# counter starts at 0
num_guesses = 0
low = 0
high = cubed
# Guess halfway between known as bisection search method
guess = (high + low)/2.0
# abs to keep conditon set to positive number. 
while abs(guess**3 - cubed) >= epsilon:
    
    if guess**3 < cubed:
        low = guess
    else:
        high = guess
        # 
    guess = (high + low)/2.0
    # updats number of guesses
    num_guesses += 1
print("Number of guesses =", num_guesses)
print(guess, "is close to the cubed root of", cubed)
print(guess**3)