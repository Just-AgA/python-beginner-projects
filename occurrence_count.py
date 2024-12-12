#Count the occurence of each element from a list and save it in a dictionary

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

#Create an empty dictionary where we will store the occurrence counts
occurences  = {}

#Loop through each element in the list,count them and add them to the dictionary
for el in sample_list:
    occurences[el] = sample_list.count(el)

print(occurences)
