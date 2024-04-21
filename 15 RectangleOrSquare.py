class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        return f"the area of the Rectangle is = {area}"

    def is_square(self):
        if self.width == self.height:
            return "Square"
        else:
            return "Rectangle"

    def perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return f"the perimeter is = {perimeter}"

width = eval(input("Enter the width of the Rectangle: "))
height = eval(input("Enter the height of the Rectangle: "))
Rect = Rectangle(width,height)

print(Rect.area())
print("Is it Square or Rectangle ?",Rect.is_square())
print(Rect.perimeter())