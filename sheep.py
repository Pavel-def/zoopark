class sheep:
    def __init__(self, name, weightFoodConsumed, age):
        self.__name = name
        self.__biome = "taiga"
        self.__eating = "ягоды", "трава"
        self.__predator = False
        self.__sound = "yyyeyyeyeeeayyaayayaaaa"
        self.weightFoodConsumed = weightFoodConsumed
        self.__age = age

    def doSoud(self):
        print(self.sound)

    def eat(self):
        print(self.name, " ест -", self.eating, " весом на ", self.weightFoodConsumed)

    def play(self):
        print("*", self.name, "играет*")