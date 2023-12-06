# Author: Shailja Manoj Maheshwari
# Date: 05th Dec 2023
# Description: This program is the subclass of creature class.


from Creature import Creature


class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "R")



