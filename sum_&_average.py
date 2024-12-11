#Find the sum and average of all the digits in a string,ignoring the rest of the characters
import statistics

str1 = "PYnative29@#8496"
total = 0
average = []

#Iterate thorugh each char in the string and check if  it's a digit with the .isdigit() function
for char in str1:
    if char.isdigit():
        total += int(char)
        average.append(int(char))

print(f"Sum of all numbers is: {total}")
print(f"Average of all numbers is: {statistics.fmean(average)}")