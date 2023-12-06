from FieldInhabitant import FieldInhabitant


class Veggie(FieldInhabitant):
    def __init__(self, name, symbol, points):
        super().__init__(symbol)
        self._name = name
        self._points = points

    def g_name(self):
        return self._name

    def s_name(self, new_name):
        self._name = new_name

    def g_points(self):
        return self._points

    def s_points(self, new_points):
        self._points = new_points

    def __str__(self):
        return f"Symbol: {self.g_symbol()}, Name: {self.g_name()}, Points: {self.g_points()}"
