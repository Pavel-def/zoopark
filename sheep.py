from animalsBase import *
class sheep(animals):
    def __init__(self,name,weightFoodConsumed,age):
        super(sheep, self).__init__(name,weightFoodConsumed,age)
        self._type = "sheep"
        self._biome = "equals"
        self._eating = "трава"
        self._predator = False
        self._sound = "*Звуки sheep*"
        self._square = 100