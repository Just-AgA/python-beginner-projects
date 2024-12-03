#Find number of characters,digits and symbols in a string
str1 = "P@#yn26at^&i5ve"

chars = 0
digits = 0
symbols = 0

for char in str1:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        chars += 1
    else:
        symbols += 1

print(f"Characters: {chars}")
print(f"Digits: {digits}")
print(f"Symbols: {symbols}")