from animalsBase import *
class cat(animals):
    def __init__(self,name,weightFoodConsumed,age):
        super(cat, self).__init__(name,weightFoodConsumed,age)
        self._biome = "taiga"
        self._eating = ["рыба", "мясо"]
        self._predator = True
        self._sound = "yyyeyyeyeeeayyaayayaaaa"




