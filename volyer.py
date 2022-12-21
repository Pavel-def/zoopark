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
        if Animal._predator == True and len(self.Animals) == 0 and self.__square-Animal._square:
            self.__predatorType1 = True
            self.__predatorType2 = Animal._type
        if Animal._predator == self.__predatorType1 and Animal._biome == self.__biome:
            if Animal._predator == True and Animal._type == self.__predatorType2:
                self.Animals.append(Animal)
                print("живатное",Animal._type ,"успешно импортировано")
            elif Animal._predator == True:
                print("ошибка живатное",Animal._type ,"не импортировано")
            else:
                self.Animals.append(Animal)
        else:
            print("ошибка живатное",Animal._type ,"не импортировано")

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
                    print("     еда кончилась")
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
                print("     Мы не будем есть:", foodType)
       #print("q",q)

    def Remove_Animal(self,Animal:animals):
        if Animal in self.Animals:
            self.Animals.remove(Animal)
            print("животное",Animal._name ,"удалено")
        else:
            print("ошибка живатное",Animal._type ,"не удалено")

    @property
    def do_All_Sound(self):
        for i in self.Animals:
            i.doSoud()



    @property
    def Animals_list(self):
        for i in self.Animals:
            print(i._name,":",i._type)

    @property
    def feed_info(self):
        #print(self.__temp_food)
        eat_shortage=0
        for i in self.Animals:
            q=i._eating
            if i._sieve:
                print(i._type,i._name,"наелся")
            else:
                print(i._type,i._name,"не наелся")
                eat_shortage=eat_shortage+i._weightFoodConsumed
        print("нужно:",eat_shortage-self.__temp_food,q)