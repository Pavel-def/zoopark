from importAll import *
class volyer:
    def __int__(self,name,biome,square):
        self.__name = name
        self.Animals= []
        self.__biome = biome
        self.__square = square
        self.__predatorType1 = False
        self.__predatorType2 = ""

    def add(self,Animals: animalsBase):
        if Animals._predator == True and len(self.Animals)==0:
            self.__predatorType= True
        if Animals._predator == self.__predatorType :
            self.Animals.append(Animals)
        else:
            print("no")





