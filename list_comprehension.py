#Join the strings of the lists in a way that elements from every position in the first list get joined to the corresponding one in the other list
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

#Use the join() method together with the zip() method to create a new list with the joint elements
new_list = ["".join(item) for item in zip(list1, list2)]
print(new_list)