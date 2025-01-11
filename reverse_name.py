#Get user input of name and last name and reverse them

def reverse_name():
    name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")

    return f"{name[::-1]} {last_name[::-1]}"

print(reverse_name())