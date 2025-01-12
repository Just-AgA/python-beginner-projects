#Print the Sum of a Current Number and a Previous number
#Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

for num in range(10):
    if num == 0:
        print(f"Current number: {num} Previous number: {num} Sum: {num}")
        continue
    print(f"Current number: {num} Previous number: {num - 1} Sum: {num + (num - 1)}")