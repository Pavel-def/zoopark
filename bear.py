class bear():
    def __init__(self,name,weightFoodConsumed,age):
        self.__name=name
        self.__biome="taiga"
        self.__eating="рыба","мясо","ягоды"
        self.__predator=True
        self.__sound="yyyeyyeyeeeayyaayayaaaa"
        self.weightFoodConsumed=weightFoodConsumed
        self.__age=age

    def doSoud(self):
        print(self.__sound)

    def eat(self, sfoodType):
        if (sfoodType in self.__eating):
            print(self.__name, ": Я покушал", sfoodType)
        else:
            print(self.__name, ": Я не буду", sfoodType)

    def play(self):
        print("*", self.__name, "играет*")
    @property
    def Age(self):
        return self.__age
    @property
    def Biome(self):
        return self.__biome
    @property
    def Eating(self):
        return self.__eating
    @property
    def Predator(self):
        return self.__predator
    @property
    def Sound(self):
        return self.__sound
    @property
    def Name(self):
        return self.__name