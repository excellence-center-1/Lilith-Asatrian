class Person:
    def __init__(self, name, age):
        self.name = name
        if age in range(1, 101):
            self.age = age
        else:
            print("Unacceptable age")

    def display_info(self):
        print(f"Hello, I am {self.name}. I am {self.age} years old")

class Auto:
    def __init__(self, name):
        self.name = name
    def move(self, speed):
        print(f"{self.name} drives at speed {speed} km/h")