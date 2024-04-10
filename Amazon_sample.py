def splitter(filename):
    file = open(filename,"r")
    text = file.read()
    L = text.split()
    users = []
    passwords = []
    for i in L:
        temp = i.split(",")
        users.append(temp[0])
        passwords.append(temp[1])
    return users,passwords


file = open("user.csv", "r")
text = file.read()
L_admin = []
Add = {}

while True:
    order = input("***** What Do you Want To Do?*****\n")
    L_admin.append(order)
    L_admin = order.split()
    if L_admin[0] == "register":
        if L_admin[1] == "<username>":
            print("Enter following information to register in our Website: ")
            username1 = input("Enter your Username please: ")
            Password1 = input("Enter your Password please: ")
            file = open("user.csv", "r")
            text = file.read()
            if username1 in text:
                print("Invalid Username")
            else:
                file = open("user.csv", "a")
                file.write(username1+","+Password1+"\n")
                print("** Registered Successfully - Welcome to our Website **")
                file.close()
                break

    if L_admin[0] == "Login" and L_admin[1] == "User":
        username1 = input("Enter your Username: ")
        password1 = input("Enter your Password: ")
        users,passwords = splitter("user.csv")
        for i in range(len(users)):
            if username1 == users[i]:
                if password1 == passwords[i]:
                    print("****Welcome****")
                    print("What do you want to do now",username1,"?")
                    print("1)adding advertisements 2)preview advertisement 3)delete advertisements")
                    Userorder = input()
                    if Userorder.lower() == "1" or "add" or "Adding Advertisements" or "Adding":
                        add_title = input("Enter your add title: ")
                        Add[username1] = add_title
                    elif Userorder.lower() == "2" or "Preview Advertisement" or "Preview":
                        print("***** Your Adds:*****\n",Add)
                    elif Userorder.lower() == "2" or "delete advertisements" or "Delete":
                        d=input("Select which ad you want to remove:")
                        if d in Add:
                            del Add[d]
                            print(Add)
                else:
                    print("Wrong Input")


    if L_admin[0] == "Superlogin" and L_admin[1] == "admin" and L_admin[2] == "1394":
        print("**Login Successful**\n**Welcome Admin**")
        turnoff = input("What do you want to do now admin?\n")
        if turnoff.lower() != "turn off":
            print("Wrong Input! - Try Again")
        else:
            print("END")
            break




