import random
file = open("data.csv","a")
L=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
captcha=""
for i in range(5):
    n=random.choice(L)
    captcha=captcha+n
a=input("sign up or sign in?")
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
    print("go to the log in system below")

print("-----------------------Login System--------------------------------")
file = open("data.csv","r")
text=file.read()
login=input("do you want to login into your account?")
if login.lower() == "yes":
    login_user = input("Enter your username:")
    login_password = input("Enter your pass:")
    if login_user in text and login_password in text:
        print("Login was successful")
    else:
        print("Username or Password was incorrect")
else:
    print("Goodbye")
file.close()