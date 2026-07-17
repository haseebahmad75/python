import random
print("======================")
print("Guess the number game")
print("======================")
n = random.randint(1,10)
attempts=10
found=False
print("The range is 1-10")
while attempts>0:
    try:
        num=int(input("Enter a number: "))
    except:
        print("Enter a valid integer: ")
        continue
    if num==n:
        print("You nailed it!")
        print("You Won!")
        found=True
        break
    else:
        attempts-=1
        if num>n:
            print("Lower...")
        elif num<n:
            print("Higher...")
if(found!=True):
    print("Out of attempts!")
    print("Number is:",n)
