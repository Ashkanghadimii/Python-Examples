import random
import secrets

L = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
     "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
     "y", "z"]
captcha = ""

class Human:
    def __init__(self, Name_Lname, ID_Number, Birthday, Email, Address, Phone_Number):
        self.Name_Lname = Name_Lname
        self.ID_Number = ID_Number
        self.Birthday = Birthday
        self.Email = Email
        self.Address = Address
        self.Phone_Number = Phone_Number


class Student(Human):

    def __init__(self, Name_Lname, ID_Number, Birthday, Email, Address, Phone_Number, Major, Enter_Year,
                 StudentNumber, Grade, Degree, Supervisor, Unit, tuition):
        super().__init__(Name_Lname, ID_Number, Birthday, Email, Address, Phone_Number)
        self.Major = Major
        self.Enter_Year = Enter_Year
        self.Student_Number = StudentNumber
        self.Grade = Grade
        self.Degree = Degree
        self.Supervisor = Supervisor
        self.Unit = Unit
        self.tuition = tuition

    @staticmethod
    def Register_Student():
        file_Register = open("Students_Database.csv", "a")
        file_Register.write("Full Name: " + S_Name_Lname + " | ID Number: " + S_ID_Number
                            + " | Year of Birth :" + S_Birthday
                            + " | Student Number(Username): " + S_Student_Number + " | Password: " + S_password
                            + " | Email: " + S_Email + " | Address: " + S_Address + " | Phone Number: " + S_Phone_Number
                            + " | Major: " + S_Major + " | Degree: " + S_Degree + " | Enter Year: " + S_Enter_Year
                            + " | Grade: " + S_Grade + " | Supervisor: " + S_Supervisor + "\n")
        file.close()

    def Choosing_Units(Courses):
        Unit = []
        for i in range(5):
            Unit.append(Courses)
        return Unit

    @staticmethod
    def print_student_info(username, password, captcha):
        # Attempt to log in
        if Student.S_LogIn(username, password, captcha):
            # Open the file for reading
            with open("Students_Database.csv", "r") as file_Print:
                # Read the contents of the file
                text_Print = file_Print.read()
                # Split the text into lines
                lines = text_Print.split("\n")
                # Print the header (assuming it's the first line)
                print(lines[0])
                # Print the rest of the lines
                for line in lines[1:]:
                    print(line)
        else:
            print("Login failed. Please check your username, password, and captcha.")

    @staticmethod
    def Tuition(tuition):
        if tuition < 0:
            return f"Amount you owe: {tuition}"
        elif tuition == 0:
            return "You dont need to pay"
        else:
            return f"Your credit amount: {tuition}"

    def ShowName(self):
        return self.Name_Lname

    def Change_Password(New_Password):
        file = open("Students_Database.csv", "r")
        text = file.read()
        data = text.split("\n")
        lines = []
        for i in range(len(data)):
            L = data[i].split("|")
            lines.append(L)
            for i in lines:
                p = i[4].split(":")[1]
                p = New_Password
                name = i[0].split(":")[1]
                user = i[3].split(":")[1]
                print(f"Password changed successfully for {user} by {name}")
    @staticmethod
    def S_LogIn(username, Password, captcha):

        file = open("Students_Database.csv", "r")
        text = file.read()
        data = text.split("\n")
        lines = []
        for i in range(len(data)):
            L = data[i].split("|")
            lines.append(L)
        if captcha != "":
            entered_captcha = input("Enter the captcha: ")
            if entered_captcha != captcha:
                print("Incorrect captcha. Please try again.")
            else:
                flag = 0
                for i in lines:
                    user = i[3].split(":")[1]
                    p = i[4].split(":")[1]
                    if username == user.strip() and Password == p.strip():
                        name = i[0].split(":")[1]
                        flag = 0
                        break
                    else:
                        flag = flag + 1
                if flag == 0:
                    print(f"Welcome {name}")
                    print(f"What do you want to do now dear {name}? \n")
                    return True
                else:
                    print("Invalid username or password.")
                    return False

print("**** Welcome to our University ****")

while True:
    order = input("Specify whether you are a 1)Professor, 2)Employee or 3)Student\n")

    if order == "3" or order.lower() == "student":
        print("What Do you Want to do now dear Student: ")
        order = input("1)Sign Up  2)Sign in \n")

        if order == "1" or order.lower() == "sign up":
            values = []

            S_Name_Lname = input("Enter your Full Name: ")
            S_ID_Number = input("Enter your ID Numer: ")
            S_Birthday = input("Enter your Year of Birth: ")
            S_Email = input("Enter your Email: ")
            S_Address = input("Enter your Address: ")
            S_Phone_Number = input("Enter your Phone Number: ")

            # Set the length of the password
            password_length = 6
            S_password = secrets.token_urlsafe(password_length)

            Student_Number = random.randint(300000, 300999)
            S_Student_Number = str(Student_Number)
            Tuition = random.randint(-100000000000, +100000000000)
            S_Tuition = str(Tuition)
            S_Major = input("Enter your Major: ")
            S_Degree = input("Enter your Degree: (Bachelor? Master? Or PHD? ")
            S_Enter_Year = input("Enter the year of your Enter: ")
            S_Grade = input("Enter your Grade: ")
            S_Supervisor = input("Enter the name of your Supervisor: ")

            SRegister = Student(S_Name_Lname, S_ID_Number, S_Birthday, S_Email, S_Address, S_Phone_Number, S_Major,
                                S_Enter_Year, S_Student_Number, S_Grade, S_Degree, S_Supervisor, S_Tuition, Tuition)

            SRegister.Register_Student()

            print("Your Student Number is:", S_Student_Number, "Your Password is:", S_password)
            print(S_Name_Lname, "Registered Successfully")

            break


        elif order == "2" or order.lower() == "sign in":
            captcha = ''
            for i in range(5):
                n = random.choice(L)
                captcha = captcha + n
            file = open("Students_Database.csv", "r")
            text = file.read()
            username = input("Enter your Username please: ")
            Password = input("Enter your Password please: ")
            print(f"Captcha: {captcha}")

            student = Student("", "", "", "", "", "", "",
                              "", "", "", "", "", "", "")

            login_result = student.S_LogIn(username, Password, captcha)

            if login_result == True:
                order = input("1)Preview Info 2)Choosing Unit 3)Tuition 4)Change Password \n")

                if order == "1" or order.lower() == "preview":
                    Pr = Student("", "", "", "", "", "", "",
                                 "", "", "", "", "", "", "")
                    print(Pr.print_student_info(username, Password, captcha))

                elif order == "2" or order.lower() == "unit":
                    Courses = input("Enter your Courses: ")
                    un = Student("", "", "", "", "", "", "", "",
                                "", "", "", "", "", "")
                    print(un.Choosing_Units())


                elif order == "3" or order.lower() == "tuition":
                    tuition = random.randint(-20000000, +20000000)
                    t = Student("", "", "", "", "", "", "", "",
                                "", "", "", "", "", "")
                    f = t.Tuition(tuition)
                    print(f)
                    if tuition < 0:
                        print("Do you want to Pay it Now?\n 1)Yes 2)No")
                        Pay = input().strip().lower()
                        if Pay == "2" or Pay.lower() == "no":
                            print(t.Tuition(tuition))
                            break
                        elif Pay == "1" or Pay.lower() == "yes":
                            order = input("Do you have any discount?")
                            if order.lower() == "yes":
                                discount = eval(input("Enter the amount of your discount in % "))
                                cal_dis = (100 - discount) / 100
                                after_discount = tuition * cal_dis
                                print(f"Your Tuition after the discount = {after_discount}")
                                amount = float(input("Enter the amount which you want to Pay:"))
                                final = (-1 * after_discount) - amount
                                print("Your actual tuition is: ", final)
                        else:
                            print("Invalid")
                            break

                elif order == "4" or order.lower() == "change":
                    c = Student("", "", "", "", "", "", "", "",
                                "", "", "", "", "", "")
                    New_Password = input("Enter your New password: ")
                    New_Pass = input("Enter your New password Again: ")
                    if New_Password == New_Pass:
                        print(c.Change_Password())
                    else:
                        print("Password do not match")

            else:
                print("Invalid Username or Password")
                break



    class Employee(Human):
        def __init__(self, Name_Lname, ID_Number, Birthday, Email, Address, Phone_Number, Salary, Position, Employee_ID,
                     Department, Hire_Date, Work_schedule):
            super().__init__(Name_Lname, ID_Number, Birthday, Email, Address, Phone_Number)

            self.Salary = Salary
            self.Position = Position
            self.Employee_ID = Employee_ID
            self.Department = Department
            self.Hire_Date = Hire_Date
            self.Work_schedule = Work_schedule

        def Register_Employee(self):
            file = open("Employee_Database.csv", "a")
            file.write("Full Name: " + E_Name_Lname + " | ID Number: " + E_ID_Number
                       + " | Year of Birth :" + E_Birthday
                       + " | Employee ID(Username) " + E_Employee_ID + " | Password: " + E_password
                       + " | Email: " + E_Email + " | Address: " + E_Address + " | Phone Number: " + E_Phone_Number
                       + " | Position: " + E_Position + " | Salary: " + E_Salary + " | Department: " + E_Department
                       + " | Hiring Date: " + E_Hire_Date + " | Work Schedule: " + E_Work_schedule + "\n")
            file.close()

        def print_Employee_info(self):
            file = open("Employee_Database.csv", "r")
            text = file.read()
            print(text)

        def Loan(self, Principal, annual_interest_rate, Duration):

            r = (annual_interest_rate / 100) / 12
            n = Duration * 12
            y = (1 + r) ** n
            z = r * y
            x = Principal * z
            MonthlyPayment = x / (y - 1)
            Rounded_MonthlyPayment = round(MonthlyPayment, 6)

            return f"You are going to pay {Rounded_MonthlyPayment} Monthly"

        @staticmethod
        def E_LogIn(username, Password, captcha):
            file = open("Employee_Database.csv", "r")
            text = file.read()
            data = text.split("\n")
            lines = []
            for i in range(len(data)):
                L = data[i].split("|")
                lines.append(L)
            if captcha != "":
                entered_captcha = input("Enter the captcha: ")
                if entered_captcha != captcha:
                    print("Incorrect captcha. Please try again.")
                else:
                    flag = 0
                    for i in lines:
                        user = i[3].split(":")[1]
                        p = i[4].split(":")[1]
                        if username == user.strip() and Password == p.strip():
                            name = i[0].split(":")[1]
                            flag = 0
                            break
                        else:
                            flag = flag + 1
                    if flag == 0:
                        print(f"Welcome {name}")
                        print(f"What do you want to do now dear {name}? \n")
                        return True
                    else:
                        print("Invalid username or password.")
                        return False

    if order == "2" or order.lower() == "employee":
        print("What Do you Want to do now dear Employee: ")
        order = input("1)Sign Up  2)Sign in 3)Preview your info\n")

        if order == "1" or order.lower() == "sign up":
            E_Name_Lname = input("Enter your Full Name: ")
            E_ID_Number = input("Enter your ID Numer: ")
            E_Birthday = input("Enter your Year of Birth: ")
            E_Email = input("Enter your Email: ")
            E_Address = input("Enter your Address: ")
            E_Phone_Number = input("Enter your Phone Number: ")

            # Set the length of the password
            password_length = 6
            E_password = secrets.token_urlsafe(password_length)

            Employee_ID = random.randint(100000, 100999)
            E_Employee_ID = str(Employee_ID)
            E_Salary = input("Enter your Salary: ")
            E_Position = input("Enter your Position: ")
            E_Department = input("Enter your Department: ")
            E_Hire_Date = input("Enter your Hiring Date: ")
            E_Work_schedule = input("Enter your Work Schedule: ")

            ERegister = Employee(E_Name_Lname, E_ID_Number, E_Birthday, E_Email, E_Address, E_Phone_Number,
                                 E_Employee_ID, E_Salary, E_Position, E_Department, E_Hire_Date, E_Work_schedule)

            ERegister.Register_Employee()

            print("Your Employee Number is:", E_Employee_ID, "Your Password is:", E_password)
            print(E_Name_Lname, "Registered Successfully")

            pass

        elif order == "2" or order.lower() == "sign in":
            captcha = ''
            for i in range(5):
                n = random.choice(L)
                captcha = captcha + n
            file = open("Employee_Database.csv", "r")
            text = file.read()
            username = input("Enter your Username please: ")
            Password = input("Enter your Password please: ")
            print(f"Captcha: {captcha}")

            employee = Employee("", "", "", "", "", "", "", "",
                                "", "", "", "")
            login_result = employee.E_LogIn(username, Password, captcha)
            #print(login_result)

            if login_result == True:
                order = input("1)Loan \n")
                if order == "1" or order.lower() == "loan":
                    Principal = eval(input("Enter The total amount of the loan: "))
                    annual_interest_rate = eval(input("Enter the interest rate of the loan: "))
                    duration = eval(input("Enter the duration of the loan in years: "))

                    l = Employee("", "", "", "", "", "", "", "",
                                "", "", "", "" )
                    print(l.Loan(Principal, annual_interest_rate, duration))
                    break


        elif order == "3" or order.lower() == "preview":
            Pr = Employee("", "", "", "", "", "", "", "",
                          "", "", "", "")
            print(Pr.print_Employee_info())

    class Professor(Human):
        def __init__(self, Name_Lname, ID_Number, Birthday, Email, Address, Phone_Number, Professor_ID, Department,
                 Courses_Teaching, Research_Interests, Attendance_Time):
            super().__init__(Name_Lname, ID_Number, Birthday, Email, Address, Phone_Number)
            self.Attendance_Time = Attendance_Time
            self.Research_Interests = Research_Interests
            self.Courses_Teaching = Courses_Teaching
            self.Department = Department
            self.Professor_ID = Professor_ID


        def Register_Professor(self):
            file = open("Professors_Database.csv", "a")
            file.write("Full Name: " + P_Name_Lname + " | ID Number: " + P_ID_Number
                       + " | Year of Birth :" + P_Birthday
                       + " | Employee ID(Username) " + P_professor_ID + " | Password: " + P_password
                       + " | Email: " + P_Email + " | Address: " + P_Address + " | Phone Number: " + P_Phone_Number
                       + " | Courses Teaching: " + P_Courses_Teaching + " | Research Interests: " + P_Research_Interest
                       + " | Attendance Time: " + P_Attendance_time + " | Department: " + P_Department + "\n")
            file.close()



        def print_Professors_info(self):
            file = open("Professors_Database.csv", "r")
            text = file.read()
            print(text)

        @staticmethod
        def P_LogIn(username, Password, captcha):
            file = open("Professors_Database.csv", "r")
            text = file.read()
            data = text.split("\n")
            lines = []
            for i in range(len(data)):
                L = data[i].split("|")
                lines.append(L)
            if captcha != "":
                entered_captcha = input("Enter the captcha: ")
                if entered_captcha != captcha:
                    print("Incorrect captcha. Please try again.")
                else:
                    flag = 0
                    for i in lines:
                        user = i[3].split(":")[1]
                        p = i[4].split(":")[1]
                        if username == user.strip() and Password == p.strip():
                            name = i[0].split(":")[1]
                            flag = 0
                            break
                        else:
                            flag = flag + 1
                    if flag == 0:
                        print(f"Welcome {name}")
                        print(f"What do you want to do now dear {name}? \n")
                        return True
                    else:
                        print("Invalid username or password.")
                        return False

    if order == "1" or order.lower() == "professor":
        print("What Do you Want to do now dear Professor: ")
        order = input("1)Sign Up  2)Sign in 3)Preview your info\n")

        if order == "1" or order.lower() == "sign up":
            P_Name_Lname = input("Enter your Full Name: ")
            P_ID_Number = input("Enter your ID Numer: ")
            P_Birthday = input("Enter your Year of Birth: ")
            P_Email = input("Enter your Email: ")
            P_Address = input("Enter your Address: ")
            P_Phone_Number = input("Enter your Phone Number: ")

            # Set the length of the password
            password_length = 6
            P_password = secrets.token_urlsafe(password_length)

            Professor_ID = random.randint(200000, 200999)
            P_professor_ID = str(Professor_ID)
            P_Department = input("Enter your Department: ")
            P_Courses_Teaching = input("Enter your Courses: ")
            P_Research_Interest = input("Enter your Research Interest: ")
            P_Attendance_time = input("Enter your Attendance time: ")

            PRegister = Professor(P_Name_Lname, P_ID_Number, P_Birthday, P_Email, P_Address, P_Phone_Number,
                                  P_professor_ID, P_Department, P_Courses_Teaching, P_Research_Interest, P_Attendance_time)

            PRegister.Register_Professor()

            print("Your Professor ID is:", P_professor_ID, "Your Password is:", P_password)
            print(P_Name_Lname, "Registered Successfully")

            pass

        elif order == "2" or order.lower() == "sign in":
            captcha = ''
            for i in range(5):
                n = random.choice(L)
                captcha = captcha + n
            file = open("Professors_Database.csv", "r")
            text = file.read()
            username = input("Enter your Username please: ")
            Password = input("Enter your Password please: ")
            print(f"Captcha: {captcha}")

            professor = Professor("", "", "", "", "", "", "",
                                  "", "", "", "")
            login_result = professor.P_LogIn(username, Password, captcha)
            #print(login_result)

            if login_result == True :
                order = input("What do you want to do?")

        elif order == "3" or order.lower() == "preview":
            Pr = Professor("", "", "", "", "", "", "",
                           "", "", "", "")
            print(Pr.print_Professors_info())
