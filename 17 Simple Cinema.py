class Cinema:
    def __init__(self, Title, Director, time, ticketPrice):
        self.title = Title
        self.director = Director
        self.time = time
        self.ticketPrice = ticketPrice

    def ShowTime(self):
        return self.time

Films = []
Name = input("Enter the Name of your Film: ")
A = Cinema("Temsah Khooni","Javad Ezati",18,60000)
B = Cinema("Karkhe ta Rhein","Ebrahim HatamiKia",19,60000)
C = Cinema("Fosil","Karim Amini",20,60000)
D = Cinema("HezarPa","AbolHasan Davoudi",22,60000)
E = Cinema("Jodaii Nader az Simin","Asghar Farhadi",24,60000)
Films.append(A)
Films.append(B)
Films.append(C)
Films.append(D)
Films.append(E)

match Name:

    case "Fosil":
        print(C.ShowTime())

    case "Temsah Khooni":
        print(A.ShowTime())

    case "Hezarpa":
        print(D.ShowTime())

    case "Karkhe ta Rhein":
        print(B.ShowTime())

    case "Jodaii Nader az Simin":
        print(E.ShowTime())
