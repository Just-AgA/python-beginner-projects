#Generate 3 random integers between 100 and 999 which is divisible by 5
from random import randrange

#Iterate three times through a range and generate three random numbers which are divisible by 5
for num in range(3):
    number = randrange(50, 200, 5)
    print(number)