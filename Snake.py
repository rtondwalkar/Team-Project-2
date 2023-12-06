from Creature import Creature


class Snake(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "S")
