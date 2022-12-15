class animals:

    def __init__(self,name,weightFoodConsumed,age):
        self._type=""
        self._name=name
        self._biome= "1_"
        self._eating= ["2_"]
        self._predator=True
        self._square = "12"
        self._sound= "3_"
        self.weightFoodConsumed=weightFoodConsumed
        self._age=age
    def eat(self, sfoodType):
        if (sfoodType in self._eating):
            print(self._name, ": Я покушал", sfoodType)
        else:
            print(self._name, ": Я не буду", sfoodType)
    def doSoud(self):
        print(self._sound)
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
    @property
    def Age(self):
        return self._age
    @property
    def Square(self):
        return self._square

    @Age.setter
    def ReAge(self, valve):
        if type(valve) is int and (valve >= 0):
            self._age=valve
        else:
            print("нельзя сменить возрост на строку или дробь или на число < 0")

    @Name.setter
    def ReName(self, valve):
        if type(valve) == str:
            self._name = valve
        else:
            print("ТОЛЬКО БУКВЫ !!!!!!")