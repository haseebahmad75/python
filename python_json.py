import json

str = '''
{
  "name": "Haseeb",
  "age": 22,
  "isStudent": true,
  "skills": ["Python", "SQL", "Git"],
  "address": {
    "city": "Lahore",
    "country": "Pakistan"
  }
}
'''
print(json.loads(str))

# Convert a python dictionary into JSON string
dict1={"name":"Haseeb",
       "age":30,
       "marks":80}


json_string = json.dumps(dict1)
print(json_string)

 # Convert a JSON string into a Pthon dictioanry

str = '''
{
"name":"Faraz",
"age":21,
"isMarried":true,
"hasChildren":false,
"skills":["AI","DSA","OOP"]
}
'''

print(json.loads(str))
print(json.loads(str))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# To make the json string more readable, we use indentation
print(json.dumps(x, indent = 4, sort_keys=True)) # sort_keys parameter sort the keys alphabetically

