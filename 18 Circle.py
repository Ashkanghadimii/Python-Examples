import math

class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

class Circle(Point):
    def __init__(self, X, Y, Radius):
        super().__init__(X, Y)
        self.Radius = Radius


    def Str(self, X, Y):
        return f"Our Points are: {self.X, self.Y} "

    def Area(self, Radius):
        return f"The Area of the Circle is: {(Radius * Radius) * math.pi}"

    def Perimeter(self, Radius):
        return f"The Perimeter of the Circle is: {2 * math.pi * Radius}"

    def R(self):
        return f"Radius is: {self.Radius}"


Point1 = eval(input("Enter the First Point: "))
Point2 = eval(input("Enter the Second Point: "))
Radius = eval(input("Enter the Radius: "))

C = Circle(Point1, Point2, Radius)
print(C.Str(Point1, Point2))
print(C.R())
print(C.Area(Radius))
print(C.Perimeter(Radius))