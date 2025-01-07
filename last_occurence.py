#Find the last occurence of a substring in a string

s = "Emma is a data scientist who knows Python. Emma works at google."

#Use .rfind() to find the last occurence of a string
last_occurence = s.rfind("Emma")

print(f"The last occurence of the string 'Emma' was on index {last_occurence}")