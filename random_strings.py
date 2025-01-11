#Generate random String of length 5
import random
import string

#Use a tuple comprehension in conjunction with the join() + choice(string.ascii_letters) methods to create a string of random characters
random_letters = "".join(random.choice(string.ascii_letters) for i in range(5))

print(f"The random letters of length 5 are: {random_letters}")

#Alteratively we can make it a function so we can change the length of the string
def random_string(length):
    letters = string.ascii_letters

    new_string = "".join(random.choice(letters) for i in range(length))

    print(f"The random string with a length of {length} is: {new_string}")

random_string(16)