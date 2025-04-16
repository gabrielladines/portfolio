# Task 1:

# Using for loop with range function, starting at 0 up to 4 (a range of 5).
for i in range(5):
    print("Hello")

# Task 2:

# I think it will update mysum variable's value to 5, add 2 (updating the value to 7) and print 7. As 7 is < 10, it will add 2 to the value, rebounding it to 9, and then print 9 next. If it adds 2 to 9, it makes 11, exceeding the range, and therefore it will not add 2 to 9 and the program will finish. In summary, the console will print 7 and 9.
# setting variable 'mysum' and value '0'
mysum = 0
# entering a for loop starting at 5, 'skipping ahead' 2 spaces until 10.
for i in range (5, 11, 2):
    # mysum variable gets updated according to 'i' which is referring to the range, so first gets updated to '5'.
    mysum += i
    # printing the ints that mysum gets updated to through the range in for loop.
    print(mysum)
# My prediction was incorrect. What it did print is the first value that is rebounded to mysum which is 5. Python then calculates 5 + 2 which = 7. It then adds this number (mysum += i), rebounding it to 12 and then printing that. Because 7 < 10, it adds 2 again. 7 + 2 = 9, 9 + 12 = 21. Because 9 + 2 = 11, which exceeds the range, it means the program is complete so concludes the loop and does not continue to add 2 and print any more ints. 

# Task 3:

# prompting the user to type in 'left' or 'right'.
n = input("You are lost in the forest. \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n :) \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n Go left or right? ")
# a while condition has been set for if the user types in 'right' as the input. As the program is not finished under the condition the user puts 'right' it loops and promps the user to give another input.
while n == "right":
    n = input("You are lost in the forest. \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n :( \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n Go left or right? ")

# if you do not enter 'right' and enter anything else, it will not pass the condition of the while and therefore go stright to the next command, in this case a print statement.
print("Congratulations! You got out the woods and made it to the sea. \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n :) \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n")


# Extension: 

n = input("You are lost in the forest. \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n :) \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n Go left or right? ")
# here you are setting a condition with alternative responses. Depending on which response the user gives, will correlate with the condition Python will execute.
while n == "right" or "straight" or "left":
    n = input("You are lost in the forest. \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n :( \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n Go left or right? ")
    if n == "left":
        n = input("You are lost in the forest. \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n :( \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n Go left or right? ")
        print("You are lost :(")
    elif n == "right":
        n = input("You are lost in the forest. \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n >:( \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n Go left or right? ")
    elif n == "straight":
        print("Congratulations! You got out the woods and made it to the sea. \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n :) \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n")
        # break is important to stop the while loop from continuously looping and eventually causing a crash.
        break
    # else is for incase user does not give the input 'right', 'left', or 'straight'. It lets the user know that their input will not work with the game and to only use the suggested inputs.
    else:
        n = input(("Please play again. Use 'straight, right or left'."))
        print("Please play again. Use 'straight, right or left'.")
        break

