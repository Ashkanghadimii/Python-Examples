L=[]
a=input("Enter your Health Label :")
a.upper()
for i in a:
    L.append(i)
if (L.count("R")) == 5 or (L.count("R")) == 3 or (L.count("R")) == 2 or L.count("Y") == 2 or L.count("Y") == 5 :
    print("Nakhor Lite")
else:
    print("Rahat Bash")


