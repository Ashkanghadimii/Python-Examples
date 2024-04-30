#guess the number with Python
import random
n=random.randint(1,10)
for i in range(3):
    a=eval(input("Enter your number :"))
    if a==n:
        print("You Won!! :",n)
        break
    elif a<n:
        print("Guess bigger")
    else:
        print("Guess smaller")