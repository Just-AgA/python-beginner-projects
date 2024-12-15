#Pretty print a JSON object by using indent and separators
import json

sampleJson = {"key1": "value1", "key2": "value2"}

#Use the dumps() method with the indent and separators parameters
pprinted_json = json.dumps(sampleJson, indent=2, separators=(",", " = "))

print(pprinted_json)