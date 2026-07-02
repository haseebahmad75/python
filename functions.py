# Function can return any data type
def my_function():
    return ["apple","mango","peach"]

fruits=my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def tuple():
    return (10,20)

x,y=tuple()
print("x:",x)
print("y:",y)

# You can send any data type as an argument to a function
def function(data):
    print("Name", data["name"])
    print("Age",data["age"])

dictionary={"name":"Hamza","age":30}
function(dictionary)

# Positional-only arguments
def my_function(name,section,age,gpa,/):
    print(name)
    print(section)
    print(age)
    print(gpa)
my_function("Haseeb","A",20,3.5)

# Keyword-only arguments
def this_function(*,brand,name,year):
    print(brand)
    print(name)
    print(year)
this_function(name="Corolla",brand="Toyota", year=20)

# Combining Positional-only and Keyword-only arguments
def combined_function(name,marks,age,/,*,sub1,sub2,sub3):
    print(name)
    print(marks)
    print(age)
    print(sub1)
    print(sub2)
    print(sub3)
combined_function("Haseeb",85,20,sub1="English", sub2="Urdu", sub3="Math")

def sum_func(a,b,/,*,c,d,e):
    return a+b+c+d+e
res=sum_func(2,2,c=2,d=2,e=2)
print(res)

# arbitrary arguments
def function(*args):
    print(type(args))
    print(args)
function(1,2,3,4,5)

def unknown_arguments(*args):
    print(type(args))
    print("First item:", args[0])
    print("Second item:", args[1])
    print("Third item:", args[2])
unknown_arguments("apple","mango","orange")

# Combining *args with regular parameters
def my_function(greeting, *names):
    for name in names:
        print(greeting, name)
my_function("Hello","Faraz","Faiq","Ahmad","Bilal")

# *args is useful when you want to create flexible functions
# Calculing total using *args
def cal_total(*numbers):
    total=0
    for num in numbers:
        total+=num
    return total
print(cal_total(1,2,3))
print(cal_total(5,5,5,5,5))

# finding maximum number using *args
def maximum(*numbers):
    max=numbers[0]
    for num in numbers:
        if num>max:
            max=num
    return max
print("Maximum number:", maximum(1,2,3,4))

# arbitrary keyword arguments
# when you do not know how many keyword arguments will be passed into the function, add ** before the parameter name

# when you pass arbitrary keyword arguments, it is stored as a dictionary inside the function
def this_function(**args):
    print("Brand:",args["brand"])
    print("Model:",args["model"])
this_function(brand="Audi", model="A5", year=2022)

def intro(**args):
    print("My first name is:",args["fname"])
    print("My last name is:",args["lname"])
    print("My marks are:",args["marks"])
    print("My gpa is:",args["gpa"])
    print(args)
intro(fname="Faiq",lname="Amir",marks=20,gpa=3.5)

# Combining regular arguments with keyword arguments
def combined(username, **args):
    print(username)
    for key,value in args.items():
        print(key + ":", value)
combined("haseeb123", name="Ahmad", age=22, gpa=3.5)

def new_function(name, **args):
    print(name)
    for key,value in args.items():
        print(key+":",value)
new_function("Haseeb", age=20, gpa=3.5, hobby="coding")

# Unpacking arguments
def cal_sum(a,b,c):
    return a+b+c
numbers=[1,2,3]
result=cal_sum(*numbers)
print(result)

def print_name(fname,lname):
    print(fname)
    print(lname)
person={"fname":"Haseeb","lname":"Ahmad"}
print_name(**person)

# inner functions can access outer variables
def outer():
    message="hello"
    def inner(): # inner function is not directly accessible. inner only exists while the outer is running
        print(message)
    inner()
outer()

# nonlocal keyword
def outer():
    x=10
    print(x)
    def inner():
        nonlocal x
        x=20
        print(x)
    inner()
    return x
outer()

# Keyword Arguments
def student(name,marks,city):
    print(name); print(marks); print(city)

student(city="Lahore", name="Haseeb", marks=80)

# Default Arguments
def greet(name, greeting="Hello"):
    print(greeting + "," + name+ "!")

greet("Ali")
greet("Ali", "Welcome")

def employee(name, salary=30000, *skills, **details):
    print(name)
    print(salary)
    print(skills)
    for key,value in details.items():
        print(key+","+value)

employee("Haseeb",250000,"C++","Git","OOP","DSA", city="Lahore", dept="CS", experience="2 years")





