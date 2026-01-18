# Write your code below this line 👇
print("Hello, my name is Tristan.")

#Square program
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

#Printing Practice
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")