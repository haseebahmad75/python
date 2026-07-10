class Person:
    def __init__(self,name,age):
        self.name=name
        self._age=age # private property
        # In python, you can make a property private by using a double underscore prefix
    
    # To access a private property, create a getter method
    def get_age(self):
        return self.__age
    
    # To modify a private property, create a setter method
    def set_age(self,age):
        self.__age=age
    
p1=Person("Anas",20)
print(p1.name)
# private property can still be accessed like this 
p1._Person__age=30
print(p1.get_age())

class Student:
    def __init__(self,name):
        self.name=name
        self.__marks=0
    
    def set_marks(self,marks):
        if marks>=0 and marks<=100:
            self.__marks=marks
        else:
            print("Grade must be between 0 and 100")
    
    def get_marks(self):
        print(f"{self.__marks}")

    def get_status(self):
        if self.__marks >= 50:
            print("Pass")
        else:
            print("Fail")

s1=Student("Faraz")
s1.set_marks(75)
print(s1.name)
s1.get_marks()
s1.get_status()
    
class Car:
    def __init__(self):
        print("This is a class")
    def __oldCar(self):
        print("This is an old car")
    def newCar(self):
        self.__oldCar()
c1=Car()
c1._Car__oldCar() # name mangling in python to access private attributes or methods, not recommended
