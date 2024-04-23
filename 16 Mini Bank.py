class BankAccount:
    def __init__(self,account_number,balance):
        self.accountnumber = account_number
        self.balance = balance

    def deposit(self):
        amount = eval(input("Enter the amount which you want to add in to your account:"))
        return f"Your actual balance after the deposit is: {self.balance + amount}"

    def withdraw(self):
        amount = eval(input("Enter the amount which you want to get from your account:"))
        if self.balance - amount > 0:
            return f" Your actual balance after the withdraw is: {self.balance - amount}"
        else:
            return "Insufficient Balance "


    def get_balance(self):
        return f"Your Current balance is: {self.balance}"

account_number = eval(input("Enter your account number please: "))
balance = eval(input("Enter your Current balance please: "))
user = BankAccount(account_number,balance)
print("*** Welcome to our Bank ***")
print("What do you want to do dear costumer? ")
print("1)Deposit 2)Withdraw 3)Balance")
order = input("Enter your order please: ")
if order == "1":
    print(user.deposit())
elif order == "2":
    print(user.withdraw())
elif order == "3":
    print(user.get_balance())
else:
    print("Not Available")

