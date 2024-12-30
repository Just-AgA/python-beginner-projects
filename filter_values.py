#Use a filter function to filter None values from a list
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

#Applying the filter function to the list and printing it
filtered_list = list(filter(None, list1))
print(filtered_list)