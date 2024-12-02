sum_odd_digits = 0
sum_even_digits = 0
total = 0

#Remove dashes or whitespaces from the input
card_number = input("Enter a card number: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

#Sum all odd digits in the card
for x in card_number[::2]:
    sum_odd_digits += int(x)


#Sum all even double digits in the card
for x in card_number[1::2]:
    x = int(x) * 2

    if x >= 10:
        sum_even_digits +=- (1 + (x % 10))
    else:
        sum_even_digits += x

#Add the sum of even digits and odd digits
total = sum_even_digits + sum_odd_digits

#Check if total is divisible by 10
if total % 10:
    print("Valid card number")
else:
    print("Invalid card number")