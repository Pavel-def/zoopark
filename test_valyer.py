from volyer import *
import unittest
from importAll import *

class Tests_volyer(unittest.TestCase):
    def test_Add_Animal(self):
        print("--------1--------")
        vr = volyer(1,"taiga", 10000)
        bear1 = bear(11, 22, 33)
        sheep1 = sheep(1111, 2, 3)
        vr.Add_Animal(bear1)
        vr.Add_Animal(sheep1)
        expected = [bear1]
        actual = vr.Animals
        self.assertEqual(expected,actual)

    def test_Remove_Animal(self):
        print("--------2--------")
        vr = volyer(1, "taiga", 10000)
        bear1 = bear(1, 2, 3)
        vr.Add_Animal(bear1)
        vr.Remove_Animal(bear1)
        expected = []
        actual = vr.Animals
        self.assertEqual(expected, actual)

    def test_feed(self):
        print("--------3--------")
        vr = volyer(1, "taiga", 10000)
        bear1 = bear(1, 2, 3)
        vr.Add_Animal(bear1)
        vr.feed("мясо", 2)
        expected = True
        actual = bear1._sieve
        self.assertEqual(expected, actual)
