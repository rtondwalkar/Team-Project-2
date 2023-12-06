from FieldInhabitant import FieldInhabitant


class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        super().__init__(symbol)
        self._x = x
        self._y = y

    def g_x(self):
        return self._x

    def s_x(self, new_x):
        self._x = new_x

    def g_y(self):
        return self._y

    def s_y(self, new_y):
        self._y = new_y
