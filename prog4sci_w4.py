def add(x, y):
        return x+y
def mult(x, y):
    print(x*y)
add(1,2)
print(add(2,3))
mult(3,4)
print(mult(4,5))


def sq(func, x):
    y = x**2
    return func(y)
def f(x):
    return x**2
calc = sq(f, 2)
print(calc)

"""Without looking at the lecture notes. Write a function for deducing even numbers and
then write a program using this function to print all the even numbers between 0 and
50."""
