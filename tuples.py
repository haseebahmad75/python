tuple1=("book","pencil","pen")
tuple2=(1,2,3,4)
tuple3=(True,False,False,True)
print(tuple1)
print(tuple2)
print(tuple3)

print("Length of tuple3:", len(tuple3))

# Tuple with a single element: remember to add a comma after the item, otherwise it is not considered as a tuple
tuple4=("mercury",)
print(tuple4)
print(type(tuple4))

# Tuple constructor usage
# Tuple constructor is used when we want to convert another iterable into a tuple
list1=[1,2,3,4]
newTuple=tuple(list1)
print(newTuple)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-5:-1])

# Modify Tuple
# Tuples are unchangeable but you can convert the tuple into a list,modify the list and then convert the list back into a tuple
tempList=list(tuple1)
tempList.append("chair")
tuple1=tuple(tempList)
print(tuple1)

# Unpacking Tuple
colors=("red","green","yellow")
(x,y,z)=colors
print(x); print(y); print(z)

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
colors=("red","green","yellow","blue","black")
(x,y,*z)=colors
print(x); print(y); print(z)

# Loop through tuples
for x in colors:
    print(x)

i=0
while i<len(colors):
    print(colors[i])
    i+=1

# Tuple methods
num=(1,2,3,4,5,6,6,6)
count=num.count(6)
index=num.index(3) # searches the tuple for a specified value and returns the index of where it was found
print("Count of 6:",count)
print("Index of 3:",index)

