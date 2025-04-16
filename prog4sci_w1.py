print("Hello amazing student!")
language = input("What is your favourite programming language? ")
name = input("What is your name? ")
print(name, 'loves', language + '!')

pi = 3.14159
radius = 2
area = pi * (radius**2)
print(area)


pi = 3.14159
radius = 3
area = pi * (radius**2)
print(area)


pi = 3.14159
radius = 2
area = pi * (radius**2)
print(area)
radius = radius + 1
print(area)
area = pi*(radius**2)
print(area)

import math
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))nt statement.
print("The following number represents your first number to the power of your second number:", str(x**y))
print("The following number represents the log of your first number with wit base 3:", str(math.log(x, 3)))


name = input("What is your name? ")
year_born_in = int(input("What year was you born in? "))
age = 2025 - year_born_in
print("Hello,", name + ",","I see that you are", + age, "this year.")
study = input("What are you studying? ")
travel_spend = float(input("How much did you spend to and from travel to London Metropolitan University on 07/02/25? "))
could_save = float(travel_spend) - 3.5
print("Hello,", name + ".","I see that you are", age,"this year. You are studying", study + ".", "On the 07/02/25 you spent £" + str((travel_spend)) + " for a tube and bus fare.", "The cheapest price for you to pay to travel to and from Univerisity is £3.50 via two buses there and back. As you took the tube that day, you spent: £" + str((travel_spend)) + ", but you could have saved: £" + str((could_save)) + " had you taken just two buses instead.")
