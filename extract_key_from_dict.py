#Exctract keys from the dictionary and create another dictionary with them
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

#Create an empty dictionary
new_dict = dict()

for key in keys:
    if key in sample_dict:
        new_dict.update({key : sample_dict[key]})

#Alternative way with a dictionary comprehension
#new_dict = {key: sampleDict[key] for key in keys}

print(new_dict)