#Calculate the multiplication and sum of two numbers
#Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. 
#Otherwise, return their sum.
number1 = 40
number2 = 30

#Create a function that check the above condition
def add_or_multiply(number1, number2):
    if number1 * number2 <= 1000:
        return number1 * number2
    return number1 + number2

print(add_or_multiply(number1, number2))