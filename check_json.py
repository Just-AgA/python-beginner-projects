#Check if an object is a valid JSON
import json

#Create a function where you can use a try expcept block and test the loads() method of JSON
def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

#Create a sample JSON object
sample_json= '''{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000
            "bonus":800
         }
      }
   }
}'''

#Call the function on the sample JSON object and save it in a variable
is_valid_json = is_json(sample_json)

#Print the result
print(f"Is the following object valid JSON: {is_valid_json}")