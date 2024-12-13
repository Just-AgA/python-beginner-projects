#Find and replace the first found element in a list
list1 = [5, 10, 15, 20, 25, 50, 20]

#Iterate through the list and check if an index has the specified value
for el in range(len(list1)):
    if list1[el] == 20:
        list1[el] = 200
        break

print(list1)
