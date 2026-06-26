num=[1,2,3,4,5]
print(num)

married=[True,False,True,True,False]
print(married)

mixed=["hello",1,True,"Venus",False]
print(mixed)
print(type(mixed))

a = list()
print(a)

list1=["lahore","karachi","multan","peshawar","skardu","islamabad"]
print(list1)
print("Length of list: ", len(list1))

# print the last element of a list
length=len(list1)
print(list1[length-1])

# Access list items
print(list1[2])
print(list1[-1]) # -1 refers to the last item, -2 refers to the 2nd last item, so on
print(list1[1:3])

if "karachi" in list1:
    print("Yes, \"karachi\" is in the list'")
else:
    print("No, \"karachi\" is not in the list")

# Change list items
list1[0]="delhi"
print(list1)
list1[1:3]=["berlin","stuttgart","hamburg","munich"]
print(list1)
list1[1:3]=["london"]
print(list1)

# Add list items
list1.insert(0,"texas") # insert method adds at a specific position
print(list1)

list1.append("florida") # append() method adds at the end
print(list1)

list2=["dubai","abu dhabi","sharjah","amman"]
list1.extend(list2) # extend() method appends elements from another list to the current list
print(list1)

# Remove list items
list1.remove("skardu")
print(list1)

list1.pop()
print(list1)

list1.pop(0)
print(list1)

# Loop through list
for x in list1:
    print(x)

# loop through index numbers
for x in range(len(list1)):
    print(list1[x])

# using while loop
x=0
while x<len(list1):
    print(list1[x])
    x+=1

# list comprehension
fruits=["apple","mango","orange","strawberry","kiwi"]
newList=[fruit.upper() for fruit in fruits if "w" in fruit]
print(newList)

# Sort lists
fruits=["kiwi","strawberry","mango","apple","guava","watermelon"]
fruits.sort()
print(fruits)

num=[35,5,11,9,23,19,27,15]
num.sort()
print(num)

# sort descending
num.sort(reverse=True)
print(num)

# By default, sort() function is case-sensitive. If we want to make it case-insensitive then we need to use a key function, str.lower
newList=["Kiwi","strawberry","Guava","apple","orange"]
newList.sort(key=str.lower)
print(newList)

# Copy lists
list1=[1,2,3,4,5,6,7]
list2=list1.copy()
print(list2)

# Join lists
list1=["a","b","c"]
list2=[1,2,3]
list3=list1+list2
print(list3)

for item in list2:
    list1.append(item)
print(list1)




