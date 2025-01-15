#Generate a random Password which meets the following conditions:
#Password length must be 10 characters long.
#It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
import random
import string

def password_generator(length):
    #Get all upper chars,lower chars, digits and special chars by using the string module
    upper_char = string.ascii_uppercase
    lower_char = string.ascii_lowercase
    digit_num = string.digits
    special_char = string.punctuation
    
    #Add them all together
    char_source = upper_char + lower_char + special_char

    password = ""

    #Get at least 2 upper case letters by using a range,then add the rest to the password variable
    for _ in range(2):
        password += random.choice(upper_char)

    password += random.choice(lower_char)

    password += random.choice(special_char)

    password += random.choice(digit_num)

    #Add the rest of the password from all the chars + digits above
    for _ in range(length - 5):
        password += random.choice(char_source)

    #Convert the string into a list so we can use the shuffle() method on it
    password_list = list(password)

    random.SystemRandom().shuffle(password_list)

    #Join all the shuffled chars together once more and return the value
    password = "".join(password_list)

    return f"The password for a length of {length} is: {password}"

print(password_generator(35))
