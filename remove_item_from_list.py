#Remove all occurences of an item in a list
list1 = [5, 20, 15, 20, 25, 50, 20]

#Iterate through the list and check if the item's value is 20,if yes then remove it from the list
for el in list1:
    if el == 20:
        list1.remove(el)

#Alternative way with a list comprehension
#new_list = [el for el in list1 if el != 20]

print(list1)