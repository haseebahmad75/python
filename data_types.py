# complex data type
# complex numbers are written with j as imaginary part
x=5j
y=3+5j
print(x.imag)
print(y.real)
print(y.imag)

# type conversion
x=8
y=2.5

a=float(x)
b=int(y)
c=complex(y)
print(b)
print(c)

# to generate a random number
import random
print("Random number:", random.randrange(1,9))
