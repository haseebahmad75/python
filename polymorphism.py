# Polymorphism
class Car:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def move(self):
        print("Move!")

class Boat:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def move(self):
        print("Sail!")
class Plane:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def move(self):
        print("Fly!")
c1=Car("Ford","Mustang")
b1=Boat("Ibiza","Touring 20")
p1=Plane("Beoing","747")
c1.move()
b1.move()
p1.move()

# Inheritance class Polymorphism
# The child classes inherit the methods of Vehicle, but the child's methods will override them
class Vehicle:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def move(self):
        print("Move!")

class Car(Vehicle): # Inheritance: Car inherits the properties and methods of Vehicle here
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")
    
c1=Car("Toyota","Prius")
b1=Boat("Maersk","JFk=100")
p1=Plane("Boeing","747")
c1.move()
b1.move()
p1.move()