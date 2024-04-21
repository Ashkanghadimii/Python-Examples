
PriceBuy = eval(input("Enter your PriceBuy: "))
if PriceBuy < 1000 or PriceBuy > 100000:
    print("Invalid Input")
elif PriceBuy % 10 !=0:
    print("Invalid Input")

PriceCurrent = eval(input("Enter your PriceCurrent: "))
if PriceCurrent < 1000 or PriceCurrent > 100000 and PriceCurrent % 10 != 0:
    print("Invalid Input")
elif PriceCurrent % 10 !=0:
    print("Invalid Input")

Count = eval(input("Enter your Count:"))
if Count < 50 or Count > 5000:
    print("Invalid Input")

if PriceCurrent>PriceBuy:
    print("\nProfit")
else:
    print("\nLoss")

InterestRates=((PriceCurrent-PriceBuy)/PriceBuy)*100
ProfitLoss = PriceCurrent - PriceBuy

print(InterestRates)
if (PriceBuy*Count)+ProfitLoss > 5000000 and InterestRates > 20:
    print("LUCKY")
elif  (PriceBuy*Count)+ProfitLoss <= 5000000 and 0< InterestRates <= 20:
    print("NORMAL")
elif (PriceBuy*Count)+ProfitLoss >= 10000000 or InterestRates <= -20:
    print("Under The Coverage")
elif (PriceBuy*Count)+ProfitLoss < 10000000 and InterestRates > -20:
    print("Chance")


