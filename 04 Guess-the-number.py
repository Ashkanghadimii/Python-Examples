#guess the number with Python
import random
n=random.randint(1,10)
for i in range(3):
    a=eval(input("Enter your number :"))
    if a==n:
        print("Hadset dorost bood :",n)
        break
    elif a<n:
        print("drake taresh kon")
    else:
        print("Kochik taresh kon")