dict1={
    "name":"Haseeb",
    "age":20,
    "marks":80,
}
print(dict1)
print(type(dict1))

# you can access a dictionary item by referring to it's key name
print(dict1["name"])
print(dict1["age"])
print(dict1["marks"])
print(len(dict1))

# dict() constructor
list1=[("name","Hamza"),("age",20)]
dictionary=dict(list1)
print(dictionary)

# Add a new value in dictionary
dict1["city"]="Lahore"
print(dict1)

# Access items
x=dict1.get("marks")
print(x)

keyList=dict1.keys()
print(keyList)

valuesList=dict1.values()
print(valuesList)

# items() method returns both keys and values as (key,value) tuples
x=dict1.items()
print(x)

# check if key exists
if "name" in dict1:
    print('Yes "name" is present in dictionary')

dict1.update({"matric":1040,"inter":1004})
print(dict1)

# Remove items
dict1.pop("city")
print(dict1)

dict1.popitem()
print(dict1)

# Loop dictionaries
for x in dict1:
    print(x)

for x in dict1.values():
    print(x)

for x in dict1.items():
    print(x)

# Copy dictionaries
dict2=dict1.copy()
print(dict2)

# copy using dict() constructor
dict3=dict(dict1)
print(dict3)

# Nested dictionaries
family={
    "child1":{
        "name":"ali",
        "age":10,
        "marks":80
    },
    "child2":{
        "name":"ahmad",
        "age":12,
        "marks":85
    },
    "child3":{
        "name":"hamza",
        "age":15,
        "marks":90
    }
}

# access item in nested dictionary
print(family["child1"]["name"])
print(family["child2"]["age"])

# Loop through nested dictionary
for child,details in family.items():
    print(child)
    for key,value in details.items():
        print(key, ":" ,value)




