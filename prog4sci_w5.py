'''Task 1: Write some code using a function and tuples so that when someone enters two numbers, 
the quotient, and remainder is calculated and printed back to them.'''

def quotient_remainder(x,y):
    q = x / y
    r = x % y
    return(q,r)
    
x = float(input("Enter a number: "))
y = float(input("Enter a number: "))

(quot,rem) = quotient_remainder(x,y)
print("The value of", x, "divided by", y, "=", quot)
print("The remainder when", x, " is divided by", y, "=", rem)

'''The following tuple refers to Adele – when she sang a song and who she sang her
particular song about:

aTuple=((2003,"boyfriend"),(2004,"friend"),(2005,"ex-boyfriend"),(2007,"ex-boyfriend"))

Write a piece of code using a function and iterating over the above tuple given so that
you can find out what year Adele sang from-until and how many unique PEOPLE she
sang about.'''

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        if t[0] not in nums:
            nums = nums + (t[0],)
            if t[1] not in words:
                words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return(min_n, max_n, unique_words)
adele_songs = ((2003, 'boyfriend'), (2004, 'friend'), (2005, 'ex-boyfriend'), (2007, 'ex-boyfriend'))
# aTuple is not working for some reason...
# (min_n, max_n, unique_words) = get_data(aTuple) 
# print("Adele sang from the year", min_n, "to", max_n, )

# Task 3
'''Make a simple modification to the code you have written in task 2 so it could apply
to a chemical inventory of different chemicals and the year they were purchased. Show
how you could obtain the number of chemicals you have and year the oldest chemical was purchased.'''


'''You are provided with the following list:
L = [1,2,3,4,5,1,2,3,4,5]
The operations below are then performed one by one:
L.remove(2)
L.remove(3)
del(L[1])
L.pop()
What is the final list I have at the end of all the operations? Check your answer!
What I think will happen:
L.remove(2) will remove '2' from list: [1,3,4,5,1,3,4,5]
L.remove(3) will remove '3' from list: [1,4,5,1,4,5]
del(L[1]) will delete index 1: [1,5,1,4,5]
L.pop() will remove last item on list: [1,5,1,4]

Here is what actually happens:'''
L = [1,2,3,4,5,1,2,3,4,5]
L.remove(2)
L.remove(3)
del(L[1])
L.pop()
print(L)
'''Terminal: [1, 5, 1, 2, 3, 4]
Python removed only the first '2' and the first '3' rather than all like I assumed:
L = [1,2,3,4,5,1,2,3,4,5]
L.remove(2): [1,3,4,5,1,2,3,4,5]
L.remove(3): [1,4,5,1,2,3,4,5]
del(L[1]): [1,5,1,2,3,4,5]
L.pop(): [1,4,1,2,3,4]'''

