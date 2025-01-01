list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

#Use a list comprehension to generate the output
new_list = [[i + j for j in list2] for i in list1]
print(new_list)