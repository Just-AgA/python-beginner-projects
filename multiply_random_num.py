#Calculate multiplication of two random float numbers
#First random float number must be between 0.1 and 1
#Second random float number must be between 9.5 and 99.5
import random

#Get the first number by using the random() method
num1 = random.random()

#Get the second number by using the uniform() method
num2 = random.uniform(9.95, 99.5)

#Multiply them
result = num1 * num2
print(result)