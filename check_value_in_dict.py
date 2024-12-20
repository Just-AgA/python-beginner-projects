#Check if a given value is present in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}

#Iterate through the values of the dictioanry by using the values() method
for value in sample_dict.values():
    if value == 200:
        print("200 is present")