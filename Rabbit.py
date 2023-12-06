# Author: Shailja Manoj Maheshwari
# Date: 05th Dec 2023
# Description: This program is the subclass of creature class.


from Creature import Creature


class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "R")

    def get_x(self):
        return self.x

    def set_x(self,x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self,y):
        self.y = y

