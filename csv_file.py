import csv
with open("D:\\data.txt", mode="r")as file:
    lines = csv.reader(file) # csv.reader prints a list of strings
    for line in lines:
        print(line)

data=[
    ["City","Country"],
    ["Lahore","Pakistan"],
    ["Mumbai","India"],
    ["Kabul","Afghanistan"],
    ["Tehran","Iran"]
]

try:
    with open("D:\\cities.csv", mode="w") as f:
     input = csv.writer(f)
     input.writerows(data)
except:
   print("Could not write to file")
else:
   print("Successfully written to cities.csv")

with open("D:\\dictionary.txt", mode="r") as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        print(row)