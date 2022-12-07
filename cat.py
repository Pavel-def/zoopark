class cat:
    def __init__(self, name, weightFoodConsumed, age):
        self.__name = name
        self.__biome = "taiga"
        self.__eating = "рыба", "мясо"
        self.__predator = True
        self.__sound = "yyyeyyeyeeeayyaayayaaaa"
        self.weightFoodConsumed = weightFoodConsumed
        self.__age = age

    def doSoud(self):
        print(self.sound)

    def eat(self):
        print(self.name, " ест -", self.eating, " весом на ", self.weightFoodConsumed)

    def play(self):
        print("*", self.name, "играет*")


