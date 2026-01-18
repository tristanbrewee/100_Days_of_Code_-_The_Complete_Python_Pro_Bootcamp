#Square program
squares = int (input("Howmany squares should be at the side of the field?"))
squareSize = int (input("How big do you want the squares?"))
squares *= squareSize
for index in range(0, squares + 1):
    for index2 in range(0, squares + 1):
        if index % squareSize == 0:
            print("*", end=" ")
        elif index2 % squareSize == 0:
            print("*", end=" ")
        elif index % squareSize != 0:
            print(" ", end=" ")
        if index2 == squares:
            print("")