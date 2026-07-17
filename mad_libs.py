import random
import textwrap
import re
with open("stories.txt") as f:
    lines=f.readlines() # lines contain list of all stories

story=random.choice(lines)

words={}

# we can make a function for input instead of writing it each time
def get_input(word_type):
    return input(f"Enter a/an {word_type}: ")

# we made this function to replace every placeholder in the given string, so we don't need to print the string again
def get_story(story,words):
    for key,value in words.items():
        story=story.replace(f"[{key}]",value)
    return story

# this function finds all the placeholders in a given string and return their list
def extract_placholders(story):
    return re.findall(r"\[(.*?)\]" , story)

print("=======================")
print("Welcome to the Mad Libs")
print("=======================")

placeholders = extract_placholders(story)

for item in placeholders:
    words[item] = get_input(item)

print(textwrap.fill(get_story(story,words), width=100))
