from animalsBase import *
class cat(animals):
    def __init__(self,name,weightFoodConsumed,age):
        super(cat, self).__init__(name,weightFoodConsumed,age)
        self._type = "cat"
        self._biome = "forest"
        self._eating = ["рыба"]
        self._predator = True
        self._sound ="*Звуки кота*"
        self._square = 100




