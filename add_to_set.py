#Add elements from a list to a set
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

#Iterate through the list and add each element using the add() method of the set
for el in sample_list:
    sample_set.add(el)

#Alternative way is by using the update() method of the set
#sample_set.update(sample_list)

print(sample_set)