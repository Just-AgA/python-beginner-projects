#Make a new list with items from both lists,but the items in the second list are reversed
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()

#Use the zip function to make tuples out of the elements of the two lists
new_list = zip(list1, list2)

#Iterate through the tuples and print them
for el in new_list:
    print(el)