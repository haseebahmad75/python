class Student:
    def __init__(self): # init() is a special function that runs automatically when an object is created. We use it to give initial values to object
                        # self means the current object
        self.name="Haseeb"
        self.age=20
s1 = Student()
print(s1.name)
print(s1.age)

# Manual implementation of Iterator
class Iterator:
    def __init__(self):
        self.current=1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > 3:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
    
my_it = Iterator()

print(next(my_it))
print(next(my_it))
print(next(my_it))


mytuple=("apple","banana","orange")
myit=iter(mytuple) # create an iterator

for item in myit:
    print(item)

# Iterate the characters of string
it=iter("jim")
print(next(it))
print(next(it))
print(next(it))
