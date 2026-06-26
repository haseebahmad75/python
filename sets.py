mySet={"first","second","third","fourth","fifth"}
print(mySet)

thisset = {"apple", "banana", "cherry", False, True, 1} # 1 and True are same values, so 1 is ignored
print(thisset)

# set constructor
list1=["A","B","C","D","E"]
newSet=set(list1)
print(newSet)

# update() method is used to add items from another iterable(list,set,tuple) into the current set
set1={1,2,3}
tuple=(4,5,6)
set1.update(tuple)
print(set1)

# If the item to remove does not exist, discard() will not raise an error
mySet.discard("tenth")
print(mySet)

# Loop through set
for x in mySet:
    print(x)

newSet = frozenset(list1)
print(type(newSet))

# Join sets
# union() method returns a new set with all items from both sets
set1={1,2,3}
set2={4,5,6,3}
set3={7,8,9}
set4=set1.union(set2,set3)
print(set4)

set={1,2,3}
tuple1=(4,5,6)
newSet = set.union(tuple1)
print(newSet)

# update() method changes the original set, and does not return a new set
set1.update(set2)
print(set1)

# Intersection in sets
commonSet=set1.intersection(set2)
print(commonSet)

set1.intersection_update(set2) # intersection_update() method changes the original set, instead of returning a new set
print(set1)

print("Intersection of set1 and set2: ",set1 & set2)

diff=set1.difference(set2)
print("Difference b/w set 1 and set2: ",diff)

set1.difference_update(set2)
print(set1)

# symmetric_difference() returns the elements that are not present in both sets (uncommon elements)
uncommonSet=set1.symmetric_difference(set2)
print(uncommonSet)

