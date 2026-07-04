import re
text="The rain in Spain Gpain Dpain Kpain"
word = "[A-Z]pain"
print(re.findall(word,text))

print(re.search("hello",text))

# You can control the number of occurences in split by using maxsplit parameter
print(re.split("in", text, maxsplit=3))

# sub() replaces the matches with the text of your choice
print(re.sub("i", "9", text))

text = "Hello how are you"
a = re.search("how",text) # this returns a match object
print(a.group()) # .group() extracts the actual matched string from the object

text="The rain in Belgium 19"
# a set is a set of characters inside a pair of square brackets[]
# In search() function, if there is more than one match, only the first occurrence of the match will be returned
word="[arn]"
print(re.findall(word,text))

word="[a-i]"
print(re.findall(word,text))

word = "[A-Z]"
print(re.findall(word,text))

word="[012]"
print(re.findall(word,text))

text = "hello234"
# \d returns a match where the string contains digit
print(re.sub(r"\d","#", text))

# extract all numbers
print(re.findall(r"\d+", text))