#Remove items from the first set if they are present in the second set
set1 = {10, 20, 30}
set2 = {20, 40, 50}

#Use the difference_update() method of sets
set1.difference_update(set2)
print(set1)