price=200
text=f"The value is {price} dollars"
print(text)

line=f"The value of {price:.2f} pounds"
print(line)

tax=0.25
sen=f"The value of this is {price+(price*tax)} dollars"
print(sen)

txt=f"It is very {"Expensive" if price>290 else "Cheap"}"
print(txt)

fruit="apple"
txt=f"I love {fruit.upper()}"
print(txt)

def converter(x):
    return x * 0.3048
txt=f"The plane is flying at a {converter(30000)} meter altitude"
print(txt)

price=56000
txt=f"The price is {price:,} dollars"
print(txt)

# names indexes in format() method
text="My name is {name} and my age is {age}"
print(text.format(name="Haseeb", age=20))

text="I want {} pieces of item no {} for {} dollars"
print(text.format(20, 101, 12.5))

text="His name is {0}. {0} is {1} years old"
print(text.format("Abdullah", 20))


