class animals:
    def __init__(self,name,weightFoodConsumed,age):
        self._name=name
        self._biome= ""
        self._eating= ""
        self._predator=True
        self._sound= ""
        self.weightFoodConsumed=weightFoodConsumed
        self._age=age

    def eat(self, sfoodType):
        if (sfoodType in self._eating):
            print(self._name, ": Я покушал", sfoodType)
        else:
            print(self._name, ": Я не буду", sfoodType)

    def play(self):
        print("*", self._name, "играет*")
    @property
    def Age(self):
        return self._age
    @property
    def Biome(self):
        return self._biome
    @property
    def Eating(self):
        return self._eating
    @property
    def Predator(self):
        return self._predator
    @property
    def Sound(self):
        return self._sound
    @property
    def Name(self):
        return self._name