#Reverse a number using a For loop
def reverse_number(number):
    original_number = number
    reverse = 0

    for _ in str(number):
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10

    print(f"Original number: {original_number}")
    print(f"Reversed number: {reverse}")

reverse_number(476031)