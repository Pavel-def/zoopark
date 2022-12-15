from animalsBase import *
class sheep(animals):
    def __init__(self,name,weightFoodConsumed,age):
        super(sheep, self).__init__(name,weightFoodConsumed,age)
        self._type = "cat"
        self._biome = "taiga"
        self._eating = "ягоды", "трава"
        self._predator = False
        self._sound = "*Звуки sheep*"
        self._square = 100

