print("I am Haseeb")
print("I am studying Computer Science")
print("I am learning python")

# to print statements on the same line
print("This is a laptop", end=" ")
print("This is mine")

age=30
print(5)
print(3+5*2-10/2)
print("I am",20,"years old")
print("I am",age,"years old")

print("\"I am\" and the number 20")
print('His hometown is "Lahore"')
print("His maternal hometown is \"New York\"")

# This is a single line comment
"""
This is a multi-line comment
This is line 1
This is line 2
"""

# type() function gives the data type of a variable
marks=80
grade="B+"
name="Haseeb"

print(type(marks))
print(type(grade))
print(type(name))

# casting: To specify the data type of a variable, we do casting
age=int(30)
grade=str("A")

print(type(age))

# variables
x=5
CreditCardScore=710
permanent_address="Lahore"
x,y,z=10,20,30
a=b=c=50
print(a)
print(b)
print(c)

# unpacking a collection
fruits=["apple","orange","banana"]
x,y,z=fruits
print(x)
print(y)
print(z)

x="python"
y="is"
z="awesome"
print(x,y,z)

# global variable
word="awesome"
def func():
    word="great"
    print("Python is",word)
func()
print("Python is",word)

