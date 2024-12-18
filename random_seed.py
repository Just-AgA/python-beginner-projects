#Roll dice in such a way that every time you get the same number
#Dice has 6 numbers (from 1 to 6). Roll dice in such a way that every time you must get the same output number. do this 5 times.
import random

#Use the seed() method of the random module
dice = [1, 2, 3, 4, 5, 6]

#Randomly selecting a number from the dice
for _ in range(5):
    random.seed(35)
    print(random.choice(dice))