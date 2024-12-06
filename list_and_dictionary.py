#Iterate through a list and check if an element is a key's value in the dictionary,if it is delete it

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
new_list = roll_number.copy()

#Create a list comprehension to save the new values
roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print("After removing unwanted elements from list:", roll_number)
