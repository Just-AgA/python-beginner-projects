#Create a dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

#Use the fromkeys() method of the dict constructor to create the dictrionary with the specified keys:values
new_dict = dict.fromkeys(employees, defaults)
print(new_dict)