questions = ("What is the Capital of Spain??",
             "How many days does a year have?", 
             "When is the sunniest month in the year?")
options = (("A.Madrid", "B.Oslo", "C.Rome"),
           ("A.365", "B.366", "C.367"),
           ("A.August", "B.May", "C.July"))
answers = ("A", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter your answer: ").upper()

    if guess not in ("A", "B", "C"):
        print("Please enter one of the options!")
    elif guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
    guesses.append(guess)
    question_num += 1

for guess in guess:
    print(f"Your guess were: {guess}")

score = int(score / len(questions) * 100)
print(f"Your score was {score}%")


