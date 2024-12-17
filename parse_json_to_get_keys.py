#Parse the following JSON to get all the values of a key ‘name’ within an array
import json

#Create a sample JSON object
sample_json = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

#Use a try except block so you can catch any errors,but also append the result of converting JSON to a dictionary into the contents list
contents = []

try:
    contents = json.loads(sample_json)
except Exception as err:
    print(err)

#Use a list comprehension by using the get() method of a dictionary
li = [item.get("name") for item in contents]

print(f"The values for the 'name' keys are: {li}")