# while loop
i=0
while i<5:
    print(i)
    i+=1
else:
    print("i is no longer less then 5")

# for loop
str="hello,venus"
for i in str:
    if (i==","):
     break
    print(i)

# range() in for loop
# range() function starts from 0 by default, and increments by 1 by default
for x in range(6): # excluding 6
   print(x)

# specifying the starting value
for x in range(2,6):
   print(x)

for x in range(2,30,5): # increments by 5
   print(x)

for x in range(3):
   if(x==2): break
   print(x)
else:
   print("Loop finished")

# Nested loop
tuple1=("a","b","c")
tuple2=(1,2,3)

for x in tuple1:
   for y in tuple2:
      print(x,y)
