from animalsBase import *
class bear(animals):
    def __init__(self,name,weightFoodConsumed,age):
        super(bear, self).__init__(name,weightFoodConsumed,age)
        self._biome="taiga"
        self._eating="рыба","мясо","ягоды"
        self._predator=True
        self._sound="yyyeyyeyeeeayyaayayaaaa"

