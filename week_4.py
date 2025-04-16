# Week 4

# Task 1
# With this block of code I assume there would be 3 outputs returned but there were 4.
# def for functiontion being defined called 'add' with 2 values it can take.
def add(x, y):
        return x+y
def mult(x, y):
    print(x*y)
    # add function refers to the defined function as works as a temporary varible.
add(1,2)
# print statment refers the condition set where add is x + y, in this case 2+3.
print(add(2,3))
# Functions naturally work as a loop so prints the values of the conditions set by funtion 'mult' where x*y, in this case, 3 * 4 = 12
mult(3,4)
# prints value of 4*5
print(mult(4,5))

# Task 2
def sq(func, x):
    y = x**2
    return func(y)
def f(x):
    return x**2
calc = sq(f, 2)
print(calc)

# Task 3
"""Without looking at the lecture notes. Write a function for deducing even numbers and
then write a program using this function to print all the even numbers between 0 and
50."""
