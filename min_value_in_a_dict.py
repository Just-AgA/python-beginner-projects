#Find the minimum value in a dictionary and return the key that has it
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

#Use the built in min() function with a key=dict.get
print(f"The key with minimum vlue is: {min(sample_dict, key=sample_dict.get)}")