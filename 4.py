x=13
y=5
print(x/y)
print(x//y) # floor division: always return an integer

a=3
b=4
# exponentiation: raising a number to a power
print(a**b)

num=5
# ternary operator syntax: value_if_true if condition else value_if_false
day="Weekend" if num>5 else "Workday"
print(day)

# comparison operator
marks=60
if (marks>=90 and marks<=100):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
elif(marks>=60 and marks<70):
    print("D")
elif(marks>=50 and marks<60):
    print("E")
elif(marks<50):
    print("F")

# identity operator(is/is not) : checks whether the two objects are actually the same object, with same memory location
# == checks if values of both variables are equal or not
x=["mango","apple"]
y=["mango","apple"]
z=x
print(z is x)
print(x==y)
print(x is y)
print(x is not y)

# Membership operator(in/not in): used to check if a value exists in a sequence or not
fruits=["apple","mango","orange","banana"]
print("apple" in fruits)
print("kiwi" in fruits)

str="Membership"
print("M" in str)
print("l" not in str)