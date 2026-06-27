# python problems
# smallest and largest element in list
list1=[10,5,11,9,23,3,19]
smallest=list1[0]
largest=list1[1]
for x in list1:
    if(x<smallest):
     smallest=x
    if(x>largest):
     largest=x

print("Smallest:",smallest)
print("Largest: ",largest)

# Find the second largest element in a list.
secLargest=list1[0]
for x in list1:
  if(x>secLargest and x != largest):
    secLargest=x
print("Second largest element: ",secLargest)

# count of a number
list2=[1,2,3,4,5,5,6,5]
count=0
for x in list2:
  if(x==5):
    count+=1
print("Count of 5 in list2:", count)

# reverse a list without using reverse()
reversed=[]
for x in list2:
  reversed=[x]+reversed
print(reversed)

# Remove all duplicates from a list
newList=[x for x in list2 if x != 5]
print(newList)

# Remove all duplicates from a list while keeping the first occurrence
result=[]
for item in list2:
  if item not in result:
    result.append(item)
print(result)

# create a tuple of 5 numbers and calculate their sum
tuple1=(1,2,3,4,5)
sum=0
for item in tuple1:
    sum+=item
print("Sum of tuple: ", sum)

# Convert a tuple into a list, add an element, then convert it back to a tuple.
num=list(tuple1)
num.append(6)
tuple2=tuple(num)
print(tuple2)

# check whether an element exists in a tuple
if 10 in tuple1:
    print("Yes, number exists")
else:
    print("Number don't exist")

# Find the length of a tuple without using len().
count=0
for x in tuple1:
    count+=1
print("Length of tuple1: ",count)

# Swap the first and last elements of a list.
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print(list1)
