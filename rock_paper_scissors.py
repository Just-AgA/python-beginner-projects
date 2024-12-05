import random

choices = ["rock", "papper", "scissors"]
computer_choice = random.choice(choices)

print("Hello and welcome to my test rock-scissors-papper game! Press Q to quit the game.")


while True:
    user_input = input("""Please choose the following options:\n
                   1. Rock\n
                   2. Scissors\n
                   3. Papper\n""").lower()
    
    if user_input == "q":
        print("Thank you for playing!")
        break

    if user_input not in choices:
        print("Please choose one of the options above\n")

    if (user_input == "rock" and computer_choice == "papper") or (user_input == "papper" and computer_choice == "scissors") or (user_input == "scissors" and computer_choice == "rock"):
        print(f"User chose {user_input} and Computer chose {computer_choice}")
        print("Computer wins!")
    elif user_input.lower() == computer_choice:
        print(f"User chose {user_input} and Computer chose {computer_choice}")
        print("It's a tie")
    else:
        print(f"User chose {user_input} and Computer chose {computer_choice}")
        print("User wins!")
