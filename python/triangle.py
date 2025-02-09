import math
class Triangle:
    def __init__(self, a, b, c):
        if a>0 and b>0 and c>0 and a +b > c and b + c > a and a + c > b:
            self.__a = a
            self.__b = b
            self.__c = c
        else:
            raise Exception("Not valid credentials are given!")
        
    def display(self):
        print(f"Side1: {self.__a}, \t Side2: {self.__b}, \t Side3: {self.__c}\n")

    def setter(self, a, b, c):
        if a>0 and b>0 and c>0 and a + b > c and b + c > a and a + c > b:
            self.__a = a
            self.__b = b
            self.__c = c
        else:
            raise Exception("Not valid credentials are given!")
        
    def getter(self):
        return (self.__a, self.__b, self.__c)
    
    def perimeter(self):
        return self.__a+self.__b+self.__c
    
    def area(self):
        half_per = self.perimeter()
        return math.sqrt(half_per *(half_per-self.__a)*(half_per-self.__b)*(half_per-self.__c))
    
    def find(self, a, b, c):
        if a**2>b**2+c**2:
            print("Obtuse")
        elif a**2<b**2+c**2:
            print("Acute")
        else:
            print("Rectangle")

    def triangle_type(self):
        if self.__a == self.__b and self.__b == self.__c:
            print("Equilateral ")
        elif self.__a == self.__b or self.__a == self.__c or self.__a == self.__b:
            print("Equidistant")
        side_max = max(self.__a, self.__b, self.__c)
        if side_max == self.__a:
            self.find(self.__a, self.__b, self.__c)
        elif side_max == self.__b:
            self.find(self.__b, self.__a, self.__c)
        else:
            self.find(self.__c, self.__a, self.__b)
        print("Triangle")
                    
        
ob = Triangle(1,2,3)
ob.display()
print(ob.getter())
print(ob.area())
ob.triangle_type()