# list comprehension
list1=[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if(x!=y):
            list1.append((x,y))
print(list1)

list2=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(list2)

from math import pi
pilist = [float(round(pi,i)) for i in range(1,6)]
print(pilist)

vec = [-4,-2,0,2,4]

list3=[x**2 for x in vec]
print(list3)

list4=[abs(x) for x in vec]
print(list4)

pair_list=[(x,x*2) for x in vec]
print(pair_list)

# call a method on each element
fruits={" pine apple  ", "  watermelon", "  dragon fruit"}
new_list=[item.strip() for item in fruits]
print(new_list)
