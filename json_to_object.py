#Convert the following JSON into Vehicle Object
import json
from types import SimpleNamespace

json_data = '{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(json_data, object_hook=lambda d: SimpleNamespace(**d))

print("Vehicle Details")
print(f"Name: {x.name}, Engine: {x.engine}, Price: {x.price}")