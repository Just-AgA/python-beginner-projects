#Remove any duplicates from a list,convert it to a tuple and then find the maximum and minimum values
sample_list = [87, 52, 44, 53, 54, 87, 52, 53]

new_list = list(set(sample_list))
print(f"The list with unique values is: {new_list}")

#Convert it to a tuple
new_tuple = tuple(new_list)
print(f"The tuple is: {new_tuple}")

#Find the max and min values
max_value = max(new_list)
min_value = min(new_list)

print(f"Max value is: {max_value}")
print(f"Min value is: {min_value}")