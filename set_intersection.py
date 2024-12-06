#Finding the intersection between two sets
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

intersection = first_set.intersection(second_set)
print(f"Intersection is: {intersection}")

#Remove the intersection from the first set by looping through the set
for el in list(first_set):
    if el in intersection:
        first_set.remove(el)
    else:
        continue

print(f"The first set after removing the elements in the intersection: {first_set}")