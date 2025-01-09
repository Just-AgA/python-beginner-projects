#Get user input separated by commas,and convert them into a list and a tuple
def generate_list_and_tuple():
    user_input = input("Please enter a list of numbers separated by commas: ")

    formatted_input = user_input.split(",")

    new_list = list(formatted_input)
    new_tuple = tuple(formatted_input)

    print(f"List is: {new_list}")
    print(f"Tuple is: {new_tuple}")

generate_list_and_tuple()