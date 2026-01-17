# Write your code below this line 👇
print("Hello, my name is Tristan.")

number = int (input("How many columns?"))
number *= 3
for index in range(0, number + 1):
    for index2 in range(0, number + 1):
        if index % 5 == 0:
            print("*", end=" ")
        elif(index2 % 5 == 0):
            print("*", end=" ")

        elif (index % 5 != 0):
            print(" ", end=" ")


        if (index2 == 15):
            print("")