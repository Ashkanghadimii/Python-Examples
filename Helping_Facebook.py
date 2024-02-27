number = eval(input("Enter number:"))

L = []
for i in str(number):
    L.append(i)

LL=list(map(int,L))
s = sum(LL)
if 1 <= number <= 50:

    if number % 2 == 0:

        if number % 5 == 0:
            print("khosh form zoj matloob")
        else:
            print("khosh form zoj namatloob")
    
    else:

        if number % 5 == 0:
            print("khosh form fard matloob")
        else:
            print("khosh form fard namatloob")
elif 51 <= number <= 99:

    if 1 <= s <= 50 and s % 5 == 0:
        print("bad form ghabele tabdil be khosh form")
    
    else:
        print("bad form gheire ghabele tabdil be khosh form")

else:
    print("no idea")
