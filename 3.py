line="It is raining"
txt='He got "95%" marks in college'
print(txt)

var=""" This is the method to assign
multi-line strings to a variable in python.
We have to use three double quotes or threee single quotes
at the start and at the end.
"""
print(var)

# string as array
str="Hello,World"
print(str[0])
print(len(str)) # prints the length of string

# looping through a string
for x in str:
    print(x)

line="The best things in life are free"
if "life" in line:
    print("Yes, 'life' is present")

# slicing string
txt="My name is Haseeb Ahmad"
print(txt[0:9])

# Modify strings
x="Hello,Mars"
print(x.replace("H","J"))
print(x.split("M"))

# string concatenation
a="We are going"
b="to Kashmir"
c=a+ " " +b
print(c)

# format strings
age=20
txt = f"My name is Andrew and I am {age}"
print(txt)

v=5
txt=f"The length of this side is {v:.2f}"
print(txt)

# booleans
x=15
y="hello"
print(bool(x))
print(bool(y))

def function():
    return True
if function():
    print("Yes")
else:
    print("No")

# Escape characters
print("He read \\American\\ history\t in high school")

# String methods
text="Hello"
print(text.count("l"))
print(text.isalpha())
print(text.isdigit())
print(text.isspace())
print(text.isupper())
print(text.islower())
print(text.upper())
print(text.lower())
print(text.replace("e","m"))