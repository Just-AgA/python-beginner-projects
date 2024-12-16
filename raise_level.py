#Loop through evey element in a list and raise them to their square
numbers = [1, 2, 3, 4, 5, 6, 7]

#Use a list comprehension to loop through all the element in the list and raise them to their root
root = [i * i for i in numbers]
print(root)