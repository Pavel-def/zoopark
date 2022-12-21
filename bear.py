from animalsBase import *
class bear(animals):
    def __init__(self,name,weightFoodConsumed,age):
        super(bear, self).__init__(name,weightFoodConsumed,age)
        self._type = "bear"
        self._biome="taiga"
        self._eating="мясо"
        self._predator=True
        self._sound="*Звуки медведя*"
        self._square = 100
