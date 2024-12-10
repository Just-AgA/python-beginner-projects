#Return the list of elements from both sets except the elements that are present in both sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

#Use the symetric_difference() method of sets
set3 = set1.symmetric_difference(set2)
print(set3)