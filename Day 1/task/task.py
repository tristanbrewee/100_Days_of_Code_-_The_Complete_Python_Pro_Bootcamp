# Write your code below this line 👇
print("Hello, my name is Tristan.")

number = int (input("How many columns?"))
squareSize = 3
number *= squareSize
for index in range(0, number + 1):
    for index2 in range(0, number + 1):
        if index % squareSize == 0:
            print("*", end=" ")
        elif index2 % squareSize == 0:
            print("*", end=" ")
        elif index % squareSize != 0:
            print(" ", end=" ")
        if index2 == number:
            print("")