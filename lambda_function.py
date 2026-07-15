# Create a lambda that returns the square of a number.
# Create a lambda that returns the cube of a number.
# Create a lambda that returns the larger of two numbers.
# Create a lambda that checks if a number is even.
# Create a lambda that checks if a string is empty.
# Create a lambda that returns the length of a string.
# Create a lambda that returns the last character of a string.
# Create a lambda that converts a string to uppercase.
# Create a lambda that adds three numbers.
# Create a lambda that returns "Positive", "Negative", or "Zero" depending on the input.

square = lambda a: a*a
print(square(5))

cube = lambda a: a*a*a
print(cube(5))

larger = lambda a,b: a if a>b else b
print(larger(5,6))

even = lambda x : x%2==0
if even(10):
    print("Even")
else:
    print("Odd")

empty = lambda words: True if len(words)==0 else False
if empty("h"):
    print("Empty")
else:
    print("Not empty")

length = lambda word: len(word)
print(length("how"))

last = lambda word: word[-1]
print(last("venus"))

upper = lambda word: word.upper()
print(upper("string"))

add = lambda a,b,c: a+b+c
print(add(1,2,3))

num = lambda x : "Positive" if x>0 else "Negative" if x<0 else "Zero"
print(num(-2))

# Use map() with a lambda to square every number in a list.
# Use map() to convert a list of strings to uppercase.
# Use filter() with a lambda to keep only even numbers.
# Use filter() to keep strings longer than 5 characters.

num=[1,2,3,4]
square = map(lambda x : x*x, num)
print(list(square))

cities=["lahore","karachi","multan","skardu"]
temp_obj = map(lambda word: word.upper(), cities)
print(list(temp_obj))

num=[2,3,4,5,7,8,10,13,15,16]
even = filter(lambda x : x%2==0, num)
print(list(even))

animals=["elephant","cat","ostrich","dog","panda","polar beer","hen"]
filter_obj=filter(lambda item: len(item)>5, animals)
print(list(filter_obj))

# Use max() with a lambda to find the longest string in a list.
animals=["elephant","cat","ostrich","dog","panda","polar beer","hen"]
longest=max(animals, key = lambda x: len(x))
print(longest)