from importAll import *

v = volyer(1,"equals", 1000)
bear1 = bear(1, 2, 3)
bear2 = bear(11, 2, 3)
bear3 = bear(111, 2, 3)
sheep1 = sheep(1111, 2, 3)
sheep2 = sheep(1111, 2, 3)

print("")

v.Add_Animal(bear1)
v.Add_Animal(bear2)
v.Add_Animal(sheep2)
v.Add_Animal(bear3)
v.Add_Animal(sheep1)

print("")

v.Animals_list
#v.Remove_Animal(sheep)
#v.Remove_Animal(bear3)

print("")

v.feed("сухпай",6)

print("")

v.feed("трава",6)

print("")

v.feed_info

print("")

v.do_All_Sound

print("")

v.info_all
#from bear import *
#animals=bear(11,22, 33)
#animals.doSoud()
#animals.play()
#animals.eat("рыба")
#print(animals.Age)
#print(animals.Biome)
#print(animals.Eating)
#print(animals.Predator)
#print(animals.Sound)
#print()
#print()
#animals.ReAge=100
#print(animals.Age)
#print()
#print()
#animals.ReName="gjgjg"
#print(animals.Name)
#print(animals.Square)








