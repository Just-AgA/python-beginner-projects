#Sort the JSON keys and then convert the object into a Python dictionary
import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

#Use the sort_keys parameter of the json object to sort the keys alphabetically
sorted_json = json.dumps(sampleJson, indent = 2, sort_keys=True)
print(sorted_json)