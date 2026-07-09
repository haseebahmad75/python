class Person:
    def __init__(self, name, age=12):
        self.name=name
        self.age=age

p1=Person("Haseeb", 20)
p2=Person("Faiq", 30)
p3=Person("Faraz")
print(f"{p1.name},{p1.age}")
print(f"{p2.name},{p2.age}")
print(f"{p3.name},{p3.age}")

class Person:
    last_name="Harrold" # This is a class property and is shared by all objects
    def __init__(self,name):
        self.name=name
        
p1=Person("Katherine")
p2=Person("Charles")
print(p1.last_name)
print(p2.last_name)

# Access another method from a method inside a class
class Person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f"Welcome {self.name}")
        print("Wishing you the best!")

    def display(self):
        self.greet()
        print("Many more to go!")

p1=Person("Faiq")
p1.greet()
p1.display()

# You can also call other methods within the class using self
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def func(self):
        print(f"The car's brand is {self.brand}")
        print(f"The car's model is {self.model}")
    
    def this_func(self):
        self.func()
      

c1=Car("Audi","A7")
c1.this_func()