class Liquid:
    def __init__(self, name, density:float)->None:
        self.__name = name
        if density>0:
            self.__density = density
        else:
            raise Exception("Invalid value for density")
       
    @property
    def name(self)->str:
        return self.__name
   
    @property
    def density(self)->float:
        return self.__density
       
    @density.setter
    def density(self, density)->None:
        if density>0:
            self.__density = density
        else:
            raise Exception("Invalid value for density")

    def display_info(self):
        print(f"Liquid Name: {self.name}, Liquid Density: {self.density}")
       
class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        if strength in range(0, 101):
            self.__strength = strength
        else:
            raise Exception("Not valid value for strength")
    @property
    def strength(self)->float:
        return self.__strength
       
    @strength.setter
    def strength(self, strength)->None:
        if strength in range(0, 101):
            self.__strength = strength
        else:
            raise Exception("Not valid value for strength")

    def display_info(self):
        print(f"Alcohol name: {self.name}, Alcohol Density: {self.density}, Alcohol Strength: {self.strength}")

try:
    liquid = Liquid("juice", 20.5)
    liquid.display_info()
    liquid.density = -1
    liquid.density = 500
    liquid.display_info()

    alcohol = Alcohol("drink", 30.5, 100)
    alcohol.display_info()
    alcohol.strength=120
    alcohol.display_info()
except Exception as e:
    print("Unexpected exception occured: ", e)