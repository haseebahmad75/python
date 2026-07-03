# Python datetime
import datetime
dt = datetime.datetime.now()
print(dt)

x = datetime.datetime.now()
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.strftime("%Z"))

print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%w")) # Weekday as a number(0-6), 0 is sunday

x = datetime.datetime(2008,2,20)
print(x)

# Python math
# We do not need to import math module bcz min(), max(), pow() etc. these are the built-in python functions and are also available in math module

x=max(5,10,19,35,12,9,3)
y=min(90,78,5,3,34,21,10)
print(x)
print(y)

z=abs(-1.56)
print(z)

exp = pow(3,3)
print(exp)

import math
a = math.ceil(1.6) # prints the nearest upward integer
b = math.floor(1.6) # prints the nearest downward integer
print(a)
print(b)

r = math.sqrt(81)
print(r)



