# for n in range(6):
#     print(n)

# ranges are immutable sequence of numbers and it is not directly displayable. Therefore, ranges are converted to lists for display
x=range(5)
print(x)

y=range(3,10)
print(list(y))

z=list(range(3,20,2))
print(z)

# Slicing ranges
r = range(10)
print(r[0])
print(r[:4])
print(list(r[3:7]))

# Membership testing
r=range(0,5,1)
print(10 in r)
print(2 in r)

# Length of range
print(len(r)) # return the number of elements in the range


