for i in range(5):
    print("Hello")


mysum = 0
for i in range (5, 11, 2):
    mysum += i
    print(mysum)

n = input("You are lost in the forest. \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n :) \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n Go left or right? ")
while n == "right":
    n = input("You are lost in the forest. \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n :( \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n Go left or right? ")
print("Congratulations! You got out the woods and made it to the sea. \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n :) \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n")


n = input("You are lost in the forest. \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n :) \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n Go left or right? ")
while n == "right" or "straight" or "left":
    n = input("You are lost in the forest. \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n :( \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n Go left or right? ")
    if n == "left":
        n = input("You are lost in the forest. \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n :( \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n Go left or right? ")
        print("You are lost :(")
    elif n == "right":
        n = input("You are lost in the forest. \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n >:( \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n XXXXXXXXXXXXX \n Go left or right? ")
    elif n == "straight":
        print("Congratulations! You got out the woods and made it to the sea. \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n :) \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n ~~~~~~~~~~~~ \n")
        break
    else:
        n = input(("Please play again. Use 'straight, right or left'."))
        print("Please play again. Use 'straight, right or left'.")
        break

