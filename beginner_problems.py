# Multiplication table of a number
num=int(input("Enter a number to print it's table: "))
for n in range(1,11):
    print(f"{num} * {n} = {num * n} ")

# Count vowels and consonants in a string
word=input("Enter a string: ")
vow=0
cons=0
for i in word:
    if i.isalpha(): # so it does not count digits as a consonant
      if i in "aeiou":
        vow += 1
      else:
        cons += 1
print(f"Vowels:{vow}")
print(f"Consonants:{cons}")

# Reverse a string without using [::-1]
word=input("Enter a string: ")
rev=""
for i in reversed(word):
    rev += i
print(rev)

# Check whether a string is a palindrome
a=input("Enter a string: ")
rev="".join(reversed(a)) # reversed() does not return a string, it returns a reverse iterator. To convert it into string, we use .join
if(rev==a):
    print("Palindrome")
else:
    print("Not a palindrome")

# Remove duplicate elements from a list.
# This method doesn't preserve order
list1=[5,5,5,3,3,3,9,9,9,8,4]
new_set=set(list1)
list2=list(new_set)
print(list2)

# This method preserves order
new_list=list(dict.fromkeys(list1))
print(new_list)

# Merge two dictionaries
dict1={
    "car1":"Honda",
    "car2":"Suzuki",
    "car3":"Toyota"
}
dict2={
    "car4":"Nissan",
    "car5":"Audi"
}
new_dict=dict1 | dict2
print(new_dict)

# Count the frequency of each character in a string
text = input("Enter a string: ")
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print("Character frequencies: ")
for key,value in freq.items():
    print(f"{key}: {value}")


