from tamagochi import Tamagochi


class Dogboy(Tamagochi):
    def __init__(self, name):
        super().__init__(name)
        self.view = " рисунок щенка мальчика"