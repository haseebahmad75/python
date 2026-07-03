import mymodule
mymodule.greeting("Haseeb")
x = mymodule.person["name"]
print(x)

import mymodule as mm
mm.greeting("Faraz")
y = mm.person["country"]
print(y)

# There are many built-in modules in python which you can import whenever you like
import platform
machine=platform.machine()
pv=platform.python_version()
print(machine)
print(pv)

# dir() function is used to list all the function names in a module
import sets
x=dir(sets)
print(x)

# Import from module
# You can choose to import only parts from a module, by using the from keyword

from mymodule import person
print(person["age"])