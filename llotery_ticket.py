#Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
import random

#Create an empty list where we will store the ticket numbers
tickets = []

#All ticket numbers need to be unique and with 10 digits
for num in range(100):
    tickets.append(random.randrange(1000000000, 9999999999))

#Use the sample() method of the random module to choose two numbers from the tickets list
winners = random.sample(tickets, k = 2)

print(f"The winning tickets are: {winners}")