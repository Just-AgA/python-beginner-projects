#Find the total of occurences for every char in a string
str1 = "Apple"

#Create an empty dictionary to hold the result
occurences = {}

for char in str1:
    occurences[char] = str1.count(char)

print(occurences)