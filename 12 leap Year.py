date=input("Enter the date:")
L=date.split("/")
for i in L:
    if int(L[2])%4==0 and int(L[2])%100 !=0:
        print("Leap Year")
        break
else:
    print(L)
