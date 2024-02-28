import random
file = open("data.csv","a")
L=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
captcha=""
for i in range(5):
    n=random.choice(L)
    captcha=captcha+n
while True:
    a=input("sign up or else?")
    if a.lower()=="sign up":
        user=input("Enter your username:")
        password=input("Enter your pass:")

        print(captcha)
        b=input("Enter the captcha:")
        if b==captcha:
            file.write(user+","+password+"\n")
        else:
            print("Captcha is wrong")
    else:
        print("Goodbye")
        break

