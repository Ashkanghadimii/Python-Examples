file = open("data.csv","a")

while True:

    a = input("Write or Break?")

    if a.lower() == "write":
        name = input("Enter your name:")
        lname = input("Enter your last name:")
        age = input("Enter your age:")
        file.write(name + "," + lname + "," + age + "\n")
    
    else:
        break

file.close()