# Even numbers generator — Write a generator even_numbers(n) that yields even numbers from 0 up to n.

def even_numbers(n):
    num = 0
    while num<=n:
        if num%2==0:
           yield num
        num+=2

my_list=even_numbers(10)
for i in my_list:
    print(i)

# Countdown — Write a generator countdown(n) that yields n, n-1, ..., 1, "liftoff!".

def countdown(num):
    while num>0:
          yield num
          num-=1
    yield "liftoff!"

count=countdown(5)
print(next(count))
print(next(count))
print(next(count))

# same as above
# for i in count:
#      print(i)

# Infinite counter — Write a generator counter(start=0, step=1) that yields values forever, incrementing by step each time.
#  (Test it with itertools.islice or by manually calling next() a few times — don't try to list() it!)

import itertools
def counter(start=0,step=1):
    while True:
        yield start
        start += step

infinite=counter()
# itertools.islice(iterable, start, stop, step)
sliced_obj=itertools.islice(infinite,0,20)
for i in sliced_obj:
    print(i)

# File line reader — Write a generator read_large_file(path) that yields one line at a time from a file,
#  stripped of whitespace. (This is the classic "why generators matter for memory" example.)

import sys
path="D:\\text.txt"
def read_large_file(path):
    with open(path) as f:
        while True:
            line = f.readline()
            if line=="":
                break
            yield line.strip()

lines=read_large_file(path)
print(next(lines))
print(next(lines))

