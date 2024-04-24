class Person:
    def __init__(self, name, lname, age, ID, Postal_code):
        self.name = name
        self.lname = lname
        self.age = age
        self.ID = ID
        self.postal_code = Postal_code

    def Showname(self):
        return f"{self.name} {self.lname}"


################################################################
class Student(Person):
    def __init__(self, name, lname, age, ID, Postal_code, average, major):
        super().__init__(name, lname, age, ID, Postal_code)
        self.average = average
        self.major = major

    def Birthyear(self):
        return 1403 - self.age

    def Showname(self):
        return self.name


A = Student("John", "Wick", 23, "0024", 1111111111, 20, "Software Engineering")
print(A.Showname())
print(A.Birthyear())

p = Person("Jason", "Moa", 23, "0085", 2222222222)
print(p.Showname())