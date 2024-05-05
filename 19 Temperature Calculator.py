class Temperature:
    def __init__(self, Grade):
        self.Grade = Grade

    @staticmethod
    def celsius_to_fahrenheit(grade):
        return f"Temperature in Fahrenheit: {((grade * 9) / 5) + 32}"

    @staticmethod
    def fahrenheit_to_celsius(grade):
        return f"Temperature in Celsius: {(grade - 32) * 5 / 9}"


while True:
    print("Select Your order: ")
    print("1)Celsius To Fahrenheit 2)Fahrenheit To Celsius 3)Exit the program")
    order = input()
    match order:
        case "1":
            Celsius = eval(input("Enter your grade in Celsius: "))
            calc1 = Temperature(Celsius)
            print(calc1.celsius_to_fahrenheit(Celsius))

        case "2":
            Fahrenheit = eval(input("Enter your grade in Fahrenheit: "))
            calc2 = Temperature(Fahrenheit)
            print(calc2.fahrenheit_to_celsius(Fahrenheit))

        case "3":
            print("See You Again")
            break


