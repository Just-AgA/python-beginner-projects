#Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

#Use the zip() function together with a dict() constructor
new_dict = dict(zip(keys, values))

print(new_dict)