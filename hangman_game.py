import random

words = ("apple", "banana", "lemon", "pear", "cherry", "watermelon")

#Dictionary of key:(<value is a tuple>)
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" O ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0

    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        
        guess = input("Enter your guess: ").lower()
        #display_answer(answer)

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one character!")
            continue

        if guess in guessed_letters:
            print(f"{guess} has already been guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for idx in range(len(answer)):
                if answer[idx] == guess:
                    hint[idx] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You win. You have found the word!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print(f"You lose. The right answer was {answer}")
            is_running = False

if __name__ == "__main__":
    main()