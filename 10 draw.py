import random
L=[]
def Lisst(s):
    random.shuffle(s)
    return random.choice(s)
for i in range(5):
    a=input("Enter your name:")
    L.append(a)
print(Lisst(L))