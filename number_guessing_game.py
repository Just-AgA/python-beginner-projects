#Make a number guessing game with user input
import random

#Use the random module to select a random number from 1 to 10
number = random.randint(1, 10)

#Ask the user for a guess,andconvert it to an integer
guess = int(input("Guess the number from 1 to 10: "))

#Initial stopping vonditions for the while loop
is_running = True
num_guesses = 0

while is_running:
    #Setting a maximum number of tries for guessing
    if num_guesses == 5:
        print("You ran out of guesses!")
        break
    
    #Check if the guess is less than or higher than the random number
    if guess < number:
        print("Too low!")
        guess = int(input("Try again: "))
    elif guess > number:
        print("Too high!")
        guess = int(input("Try again: "))
    elif guess == number:
        print(f"Correct, {guess} is the right number!")
        is_running = False    

    #Increase the number of guesses so the stopping condition can be reached
    num_guesses += 1

