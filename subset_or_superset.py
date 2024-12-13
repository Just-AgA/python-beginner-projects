#Check if a set is a subset or superset of another set
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

if first_set.issubset(second_set):
    print("First set is a subset of the second set")
    first_set.clear()

if second_set.issubset(first_set):
    print("Second set is a subset of the first set")
    second_set.clear()
else:
    print("Second set is a superset of the first set")
