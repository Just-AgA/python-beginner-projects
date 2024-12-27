#Calculate the factorial of a number using recursion

def calculate_factorial(number):
    if number == 1:
        return 1
    return calculate_factorial(number - 1) * number

print(calculate_factorial(3))