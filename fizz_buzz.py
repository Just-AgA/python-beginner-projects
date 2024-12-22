#Iterate from 1 to 100,and print Fizz for  multiple of 3,Buzz for multiple of 5 and FizzBuzz for multiple of both

for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
        continue
    elif num % 5  == 0:
        print("Buzz")
        continue
    elif num % 3 == 0:
        print("Fizz")
        continue
    print(num)