from tamagochi import Tamagochi


class Catboy(Tamagochi):
    def __init__(self, name):
        super().__init__(name)
        self.view = " рисунок кошкомальчика"