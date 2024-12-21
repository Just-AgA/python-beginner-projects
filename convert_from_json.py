#Convert a JSON object into a dictionary and access the key
import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

#Use the loads() method of json to convert from JSON
converted_data = json.loads(sampleJson)

print(converted_data["key2"])