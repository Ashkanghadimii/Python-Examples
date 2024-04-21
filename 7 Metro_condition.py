counter = 0


FR = input("Enter the First Row of the Subway seats condition: ")
SR = input("Enter the Second Row of the Subway seats condition:")

S = FR.split()
S2 = SR.split()

for i in range(8):
    if S[i] == "1" and S2[i] == "1":
        counter = counter+1
print(counter)
