L=[]
num=input("Enter a Number: ")
for i in num:
    L.append(i)
LL=list(map(int,L))
if 1 <= sum(LL) <= 50 and sum(LL) % 5 == 0:
    print("Bad Forme ghabele Tabdil be Khosh Form")
elif 1 <= sum(LL) <= 50 and sum(LL) % 5 != 0:
    print("Bad Forme Gheyre Ghabele Tabdil")
elif 1 <= num <= 50 and int(num) % 2 == 0:
    print("Khosh Forme Zoj ")
elif 1 <= num <= 50 and int(num) % 2 != 0:
  print("Khosh Forme Fard")
elif 1 <= num <= 50 and int(num) % 5 == 0:
  print("Khosh Forme Matloob")
else:
    print("Nazari Nadarim")