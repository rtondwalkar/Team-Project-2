# Author: Shailja Manoj Maheshwari
# Date: 5th Dec 2023
# Descrption: This program is a subclass of creature class.

from Creature import Creature


class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "V")
        self.__veggies = []

    def addVeggie(self, veggie):
        self.__veggies.append(veggie)

    def popVeggie(self):
        self.__veggies.pop()

    def getVeggies(self):
        return self.__veggies
