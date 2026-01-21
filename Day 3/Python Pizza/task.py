print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

size = str.lower(size)
pepperoni = str.lower(pepperoni)
extra_cheese = str.lower(extra_cheese)

price = 0

if size == "s":
    price += 15
    if pepperoni == "y":
        price += 2
elif size == "m":
    price += 20
elif size == "l":
    price += 25
if pepperoni == "y" and price >= 20:
    price += 3
if extra_cheese == "y":
    price += 1

print(f"Your final bill is: ${price}.")