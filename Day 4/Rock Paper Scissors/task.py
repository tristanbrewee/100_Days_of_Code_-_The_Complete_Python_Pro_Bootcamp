import random
import hand_strings

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 3 for Scissors "))

output_string = ["You win!", "Draw!", "You loose"]
pc_choice = random.randint(0,2)

hands = [hand_strings.rock, hand_strings.paper, hand_strings.scissors]

print("Your choice:")
print(hands[player_choice])
print("Computer's choice:")
print(hands[pc_choice])

match player_choice:
    case 0:
        match pc_choice:
            case 0:
                print(output_string[1])
            case 1:
                print(output_string[2])
            case 2:
                print(output_string[0])
    case 1:
        match pc_choice:
            case 0:
                print(output_string[0])
            case 1:
                print(output_string[1])
            case 2:
                print(output_string[2])
    case 3:
        match pc_choice:
            case 0:
                print(output_string[2])
            case 1:
                print(output_string[0])
            case 2:
                print(output_string[1])
    case _:
        print("Invalid choice")