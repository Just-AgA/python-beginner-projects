#Pick a random character from a given String
import random

sample_string = "abcdefgijklmnop"

#Use the choice() method of the random module
print(f"A random character of the above string is: '{random.choice(sample_string)}'")