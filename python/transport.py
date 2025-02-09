class Vehicle:
    def __init__(self, name, speed, wheelQuantity ):
        if speed>0:
            self.__speed = speed
        else:
            raise Exception("Speed can't be negative")
        if wheelQuantity>1:
            self.__wheelQuantity = wheelQuantity
        else:
            raise Exception("Vehicle wheel quantity must be at least 2.")
        self.__name = name
    
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, speed):
        if speed>0:
            self.__speed = speed
        else:
            raise Exception("Speed can't be negative")
        
    @property
    def wheelQuantity(self):
        return self.__wheelQuantity
    
    @property
    def name(self):
        return self.__name
    
    def calculate_travel_time(self, distance):
        print(f"Total time: {str(round(distance/self.speed, 2))}")

    def display_info(self):
        print(f"Name: {self.name}, \t Speed: {self.speed}, \t Wheel quantity: {self.wheelQuantity}")


class Car(Vehicle):
    def __init__(self, name, speed, wheelQuantity, condPresence):
        super().__init__(name, speed, wheelQuantity)
        self.__condPresence = condPresence

    @property
    def condPresence(self):
        return self.__condPresence
    
    @condPresence.setter
    def condPresence(self, condPresence):
        self.__condPresence = condPresence
    def display_info(self):
        flag = ""
        if self.condPresence == True:
            flag = "Present"
        else:
            flag = "Not present"
        print(f"Name: {self.name}, \t Speed: {self.speed}, \t Wheel quantity: {self.wheelQuantity}, \t Conditioner: {flag}")

class Bicycle(Vehicle):

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, speed=100):
        self.__speed = round(speed/3)

    def display_info(self):
        print(f"Speed: {self.speed}, \t Wheel quantity: {self.wheelQuantity}")
        
ob1 = Vehicle("Vehicle1", 60.54, 4)
ob1.display_info()
ob1.speed = 70
ob1.display_info()
ob1.calculate_travel_time(120)

ob2 = Car("BMW", 130, 4, False)
ob2.display_info()
ob2.calculate_travel_time(900)

obBicycle = Bicycle(2, ob2.speed)
obBicycle.display_info()
obBicycle.calculate_travel_time(240)



