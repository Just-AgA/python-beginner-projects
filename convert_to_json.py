#Convert a dictionary to JSON by using the dumps() method
import json

data = {"key1" : "value1", "key2" : "value2"}

json_data = json.dumps(data)
print(json_data)