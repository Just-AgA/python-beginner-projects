#Go through the dictionary and check if the value is in the list
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
new_list = list()

#Iterate through the values of the dictionary and check if that value is in the list,if it isn't then append it to it(only unique values are appended)
for value in speed.values():
    if value in new_list:
        continue
    else:
        new_list.append(value)

print(f"New list is {new_list}")