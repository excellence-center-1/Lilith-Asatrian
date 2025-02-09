from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, a,b):
        if a>0 and b>0:
            self.__a = a
            self.__b = b
        else:
            raise Exception("Not valid credentials are given")
    @property
    def ab(self):
        return self.__a, self.__b
    
    @ab.setter
    def ab(self, a):
        if a>0:
            self.__a = a

        else:
            print("Not valid")
    def area(self):
        a, b = self.ab
        return round(a*b, 3)
    
    def perimeter(self):
        a, b = self.ab
        return (a+b)/2
    
class Triangle(Shape):
    def __init__(self, a,b,c):
        if a+b>c and a+c>b and b+c>a:
            self.__a = a
            self.__b = b
            self.__c = c
        else:
            raise Exception("Not valid credentials are given")
        
    @property
    def abc(self):
        return self.__a, self.__b, self.__c
    
    @abc.setter
    def abc(self, a,b,c):
        if a+b>c and a+c>b and b+c>a:
            self.__a = a
            self.__b = b
            self.__c = c
        else:
            raise Exception("Not valid credentials are given")

    def perimeter(self):
        a,b,c = self.abc
        return a+b+c   
    def area(self):
        a,b,c = self.abc
        p = self.perimeter()
        return round((p*(p-a)*(p-b)*(p-c))**0.5, 2)
    


my_rectangle = Rectangle(15, 26)
print("p rec", my_rectangle.perimeter())
print("s rec", my_rectangle.area())
my_triangle = Triangle(12,5,9)
print("p tri", my_triangle.perimeter())
print("s tri",my_triangle.area())