Principal=eval(input("Enter The total amount of the loan: "))
annual_interest_rate=eval(input("Enter the interest rate of the loan: "))
duration=eval(input("Enter the duration of the loan in years: "))

r = (annual_interest_rate/100) / 12
n = duration * 12
y = (1+r)**n
z = r*y
x = Principal * z
MonthlyPayment = x / (y-1)

Rounded_MonthlyPayment=round(MonthlyPayment,6)

print("You are going to pay",Rounded_MonthlyPayment,"Monthly")