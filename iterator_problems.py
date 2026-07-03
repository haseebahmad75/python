# Create an iterator that returns numbers from 1 to 10.
class NumberIterator:
    def __init__(self):
        self.current=1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > 10:
            raise StopIteration
        value=self.current
        self.current+=1
        return value
    
numbers = NumberIterator()

for num in numbers:
    print(num)

# Create an iterator that returns even numbers from 2 to 20
class EvenNumberIterator:
    def __init__(self):
        self.current=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > 20:
            raise StopIteration
        value=self.current
        self.current+=2
        return value
    
evenNumbers = EvenNumberIterator()
for num in evenNumbers:
    print(num)
    
# Create an iterator that counts down from 10 to 1.
class CountDownIterator:
    def __init__(self):
        self.current=10

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value=self.current
        self.current-=1
        return value
    
countDown = CountDownIterator()
for n in countDown:
    print(n)

# Create an iterator that returns A to Z
class AlphabetIterator:
    def __init__(self):
        self.current=ord('A')
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > ord('Z'):
            raise StopIteration
        letter = chr(self.current)
        self.current+=1
        return letter
    
letters = AlphabetIterator()
for char in letters:
    print(char)

# Create an iterator that behaves like range(start,stop)
class RangeIterator:
    def __init__(self,start,stop):
        self.current=start
        self.stop=stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value=self.current
        self.current+=1
        return value
    
range = RangeIterator(2,5)
for item in range:
    print(item)

