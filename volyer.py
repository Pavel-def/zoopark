from importAll import *

class volyer:
    def __init__(self,name,biome,square):
        self.__name = name
        self.Animals = []
        self.__biome = biome
        self.__square = square
        self.__predatorType1 = False
        self.__predatorType2 = ""
        self.__temp_food = 0
        self.__food_type = ""

    def Add_Animal(self,Animal:animals):
        #if Animal._predator == True and len(self.Animals) == 0 and self.__square-Animal._square >= 0:
            #self.__predatorType1 = True
            #self.__predatorType2 = Animal._type
            #print("1+ self.__predatorType2",self.__predatorType2) #хз но это штука довала баг
        if Animal._predator == self.__predatorType1 and Animal._biome == self.__biome:

            if Animal._predator == True and Animal._type == self.__predatorType2:
                self.Animals.append(Animal)
                temp=str(Animal._type)
                print("\033[32m{}".format("живатное"),"\033[32m{}".format(temp) ,"\033[32m{}".format("успешно импортировано"),"\033[0m{}".format(""))
            elif Animal._predator == True:
                print("\033[31m{}".format("ошибка живатное"), "\033[31m{}".format(Animal._type),"\033[31m{}".format("не импортировано"), "\033[0m{}".format(""))
            else:
                temp = str(Animal._type)
                print("\033[32m{}".format("живатное"),"\033[32m{}".format(temp) ,"\033[32m{}".format("успешно импортировано"),"\033[0m{}".format(""))
                self.Animals.append(Animal)
        else:
            print("\033[31m{}".format("ошибка живатное"),"\033[31m{}".format(Animal._type) ,"\033[31m{}".format("не импортировано"),"\033[0m{}".format(""))

    def feed(self,foodType,amount_food):
        #q=0
        if foodType != self.__food_type:
            self.__food_type = foodType
        for i in self.Animals:
            #q+=1
            if (foodType in i._eating):
                if i._sieve:
                    continue
                if amount_food+self.__temp_food == 0:
                    #print("     0 + еда кончилась amount_food",amount_food,"self.__temp_food",self.__temp_food)
                    print("\033[31m{}".format("еда кончилась"))
                    break
                if (self.__temp_food+amount_food)-i._weightFoodConsumed >= 0:
                    i.eat(foodType)
                    i._sieve = True
                    temp=self.__temp_food+amount_food
                    #print("     1 + amount_food",amount_food,"self.__temp_food",self.__temp_food)
                    if amount_food-i._weightFoodConsumed>=0:
                        amount_food= amount_food - i._weightFoodConsumed
                        #print("     2 + amount_food",amount_food,"self.__temp_food",self.__temp_food)
                    else:
                        amount_food = 0
                        self.__temp_food = temp - i._weightFoodConsumed
                        #print("     2 - amount_food",amount_food,"self.__temp_food",self.__temp_food)
                else:
                    #print("1     1 - amount_food", amount_food, "self.__temp_food", self.__temp_food)
                    self.__temp_food=self.__temp_food + amount_food
                    amount_food=0
                    #print("2     1 - amount_food",amount_food,"self.__temp_food",self.__temp_food)
            else:
                print("\033[31m{}".format("Мы не будем есть:"), "\033[31m{}".format(foodType),"\033[0m{}".format(""))
       #print("q",q)

    def Remove_Animal(self,Animal:animals):
        if Animal in self.Animals:
            self.Animals.remove(Animal)
            print("\033[32m{}".format("животное"),"\033[32m{}".format(Animal._name) ,"\033[32m{}".format("удалено"),"\033[0m{}".format(""))
        else:
            print("\033[31m{}".format("ошибка живатное"),"\033[31m{}".format(Animal._type) ,"\033[31m{}".format("не удалено"),"\033[0m{}".format(""))

    @property
    def do_All_Sound(self):
        for i in self.Animals:
            i.doSoud()



    @property
    def Animals_list(self):
        for i in self.Animals:
            print("\033[36m{}".format(i._name),"\033[36m{}".format(":"),"\033[36m{}".format(i._type),"\033[0m{}".format(""))

    @property
    def feed_info(self):
        #print(self.__temp_food)
        eat_shortage=0
        for i in self.Animals:
            q=i._eating
            if i._sieve:
                print("\033[32m{}".format(i._type),"\033[32m{}".format(i._name),"\033[32m{}".format("наелся"),"\033[0m{}".format(""))
            else:
                print("\033[31m{}".format(i._type),"\033[31m{}".format(i._name),"\033[31m{}".format("не наелся"),"\033[0m{}".format(""))
                eat_shortage=eat_shortage+i._weightFoodConsumed
        print("\033[31m{}".format("нужно:"),"\033[31m{}".format(eat_shortage-self.__temp_food),"\033[31m{}".format(q),"\033[0m{}".format(""))

    @property
    def info_all(self):
        print("\033[36m{}".format("self.__name"),"\033[31m{}".format("\033[31m{}".format(self.__name),"\033[0m{}".format("")))
        print("\033[36m{}".format("self.Animals"), "\033[31m{}".format(self.Animals),"\033[0m{}".format(""))
        print("\033[36m{}".format("self.__biome"),"\033[31m{}".format(self.__biome),"\033[0m{}".format(""))
        print("\033[36m{}".format("self.__square"), "\033[31m{}".format(self.__square),"\033[0m{}".format(""))
        print("\033[36m{}".format("self.__predatorType1"), "\033[31m{}".format(self.__predatorType1),"\033[0m{}".format(""))
        print("\033[36m{}".format("self.__predatorType2"), "\033[31m{}".format(self.__predatorType2),"\033[0m{}".format(""))
        print("\033[36m{}".format("self.__temp_food"), "\033[31m{}".format(self.__temp_food),"\033[0m{}".format(""))
        print("\033[36m{}".format("self.__food_type"), "\033[31m{}".format(self.__food_type),"\033[0m{}".format(""))
