s1 = "cat u rock" 
s2 = "i help cat"
if len(s1) == len(s2):
        for char1 in s1:
            for char2 in s2:
                if char1 == char2:
                    print("common letter")
                    break

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
i = 0ter (i) starts at 0, it is expected that the condition is met.
while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    i += 1
print("What does that spell?")
for i in range(times):
    print(word, "!!!")

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
for char in word:
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
print("What does that spell?")
for i in range(times):
    print(word, "!!!")


cubed2 = int(input("Input a int: "))
cubed = abs(cubed2)
for i in range(cubed + 1):
    if i**3 >= cubed:
        break
if i**3 != cubed:
    print("This is not a perfect cube.")
    print("Square root of", cubed, "is", i)
else:
    if cubed2 < 0:
        i = - i
        print("Cubed root of", cubed2, "is", i)
    else:
        print("Cubed root of", cubed2, "is", i)


cubed2 = float(input("Enter a number you wish to find the square root of: "))
cubed = abs(cubed2)
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cubed) >= epsilon:
    guess += increment
    num_guesses += 1
print("Number of guesses =", num_guesses)
if abs(guess**3 - cubed) >= epsilon:
    print("Failed on square root of", cubed)
else:
    if cubed2 < 0:
        guess = -guess
        print(guess, "is close to the square root of", cubed2)
    else:
        print(guess, "is close to the square root of", cubed2)


cubed = float(input("Enter a positive number greater than 1 to find the cubed root of: "))
epsilon = 0.01
num_guesses = 0
low = 0
high = cubed
guess = (high + low)/2.0
while abs(guess**3 - cubed) >= epsilon:
    
    if guess**3 < cubed:
        low = guess
    else:
        high = guess
        # 
    guess = (high + low)/2.0
    num_guesses += 1
print("Number of guesses =", num_guesses)
print(guess, "is close to the cubed root of", cubed)
print(guess**3)
