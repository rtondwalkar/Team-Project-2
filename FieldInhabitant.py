# Author: Pankajbharathi
# Date: 28/11/23
# Descrption: This program will create a game called
#             Captain veggie in which rabbit has to harvest
#             all the vegetables before they are consumed by
#             leporine menace. The capatins who harvested the
#             most, their scores will display on the screen.
class FieldInhabitant:
    def __init__(self, symbol):
        self.__symbol = symbol

    def g_symbol(self):
        return self.__symbol

    def s_symbol(self, new_symbol):
        self.__symbol = new_symbol
