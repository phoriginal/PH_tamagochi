from tamagochi import Tamagochi


class Doggirl(Tamagochi):
    def __init__(self, name):
        super().__init__(name)
        self.view = " рисунок щенка девочки"