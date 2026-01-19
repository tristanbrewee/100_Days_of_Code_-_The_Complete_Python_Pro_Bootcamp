print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

result = bill
match tip:
    case 10:
        result*=1.10
    case 12:
        result*=1.12
    case 15:
        result*=1.15

result /= people
print(f"Each person should pay ${result:.2f}")