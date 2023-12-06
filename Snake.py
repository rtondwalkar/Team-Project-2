# Author: Rutvik Tondwalkar
# Date: 12/05/2023
# Description: Snake.py Creates a class that inherits from a class Creature.

from Creature import Creature


class Snake(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "S")
