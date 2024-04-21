class Customer:
    def __init__(self,name,phone,address,postal_code,username,password,basket):
        self.name = name
        self.phone = phone
        self.address = address
        self.postal_code = postal_code
        self.username = username
        self.password = password
        self.basket = basket

    def LogIn(self,username,password):
        if username == self.username and password == self.password:
            return True
        else:
            return False

    def buy(self,product):
        self.basket.append(product)

    def ShowOrders(self):
        return self.basket

    def __repr__(self):
        return f"{self.name}:{self.phone}:{self.address}:{self.postal_code}:{self.username}:{self.password}\n"
    
#from customer import Customer
#from filename import class

name = input("Enter your name:")
phone = input("Enter your phone:")
address = input("Enter address:")
postal_code = eval(input("Enter your postal code:"))
username = input("Enter your username:")
password = input("Enter your password:")
basket = []
user = Customer(name,phone,address, postal_code, username, password, basket)

#print(user)
f = open("database.txt","a")
f.write(user.__repr__())
f.close()

while True:
    print("Welcome to our online shop")
    print("1-Buy")
    print("2-show orders")
    item = input("Choose your item:")
    if item == "1":
        product = input("What do you want?")
        user.buy(product)
    else:
        print(user.ShowOrders())