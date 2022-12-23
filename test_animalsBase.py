import unittest
from importAll import *

class Tests_animalsBase(unittest.TestCase):
    def test_eat(self):
        print("--------1--------")
        bear1 = bear("Серёга",2,33)
        bear1.eat("мясо")

