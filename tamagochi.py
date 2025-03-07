import random

class Tamagochi:
    def __init__(self, name: str):
        self.name = name
        self.__hp = 100
        self.__max_hp = 100
        self.__hunger = 0
        self.__age = 0
        self.__trust = 50
        self.__morale = 50
        self.view = ""

    # Фиксированные действия
    def bit(self):
        #Бить питомца: фиксированный урон 10, уменьшает доверие и мораль.
        self.__hp = max(0, self.__hp - 10)
        self.__trust = max(0, self.__trust - 10)
        self.__morale = max(0, self.__morale - 20)
        self.check_morale()
        print(f"Вы ударили {self.name}. Ему не понравилось...")

    def heal(self):
        #Лечить питомца: фиксированное лечение 15, увеличивает доверие и голод.
        self.__hp = min(self.__max_hp, self.__hp + 15)
        self.__trust = min(100, self.__trust + 5)
        self.__hunger = min(100, self.__hunger + 5)
        print(f"Вы вылечили {self.name} на 15 HP.")

    def feed(self):
        #Кормить питомца: фиксированное уменьшение голода на 20, увеличивает мораль.
        self.__hunger = max(0, self.__hunger - 20)
        self.__morale = min(100, self.__morale + 5)
        self.__trust = min(100, self.__trust + 5)
        print(f"Вы покормили {self.name}.")

    def hug(self):
        #Обнять питомца: эффект зависит от доверия.
        if self.__trust >= 60:
            self.__morale = min(100, self.__morale + 15)
            self.__trust = min(100, self.__trust + 5)
            print(f"{self.name} доволен вашим объятием!")
        else:
            self.__morale = max(0, self.__morale - 10)
            print(f"{self.name} не хочет ваших объятий и отстраняется.")
        self.check_morale()

    def play(self, activity: str):
        #Играть с питомцем: выбор игры влияет на характеристики.
        if activity == "ball":
            self.__morale = min(100, self.__morale + 10)
            self.__hunger = min(100, self.__hunger + 10)
            print(f"Вы поиграли с {self.name} в мяч!")
        elif activity == "chase":
            if self.__trust >= 50:
                self.__morale = min(100, self.__morale + 15)
                self.__trust = min(100, self.__trust + 5)
                print(f"{self.name} весело гонялся за вами!")
            else:
                self.__morale = max(0, self.__morale - 5)
                print(f"{self.name} не доверяет вам и отказался играть.")
        else:
            print("Такой игры нет.")
        self.check_morale()

    def speak(self, speech_type: str):
        #Говорить с питомцем: оскорбить или поддержать.
        if speech_type == "insult":
            self.__morale = max(0, self.__morale - 15)
            self.__trust = max(0, self.__trust - 10)
            print(f"Вы оскорбили {self.name}. Он расстроен.")
        elif speech_type == "support":
            if self.__trust >= 50:
                self.__morale = min(100, self.__morale + 10)
                self.__trust = min(100, self.__trust + 5)
                print(f"{self.name} ценит вашу поддержку!")
            else:
                self.__morale = max(0, self.__morale - 5)
                print(f"{self.name} не верит вашим словам.")
        else:
            print("Неверный тип речи.")
        self.check_morale()

    # Служебные методы
    def age_up(self):
        #Увеличивает возраст и обновляет характеристики.
        self.__age += 1
        self.__hunger = min(100, self.__hunger + 5 + (self.__age // 10))
        if self.__age % 20 == 0:
            self.__hp = max(0, self.__hp - 1)
        if self.__hunger >= 100:
            self.__hp = max(0, self.__hp - 5)

    def check_morale(self):
        #Проверяет мораль: при 0 возможен побег или самоубийство.
        if self.__morale <= 0:
            if random.random() < 0.5:
                print(f"{self.name} не выдержал и покончил с собой...")
                exit()
            else:
                print(f"{self.name} сбежал от вас...")
                exit()

    def __str__(self):
        #Отображает текущее состояние питомца.
        return (self.view + "\n" +
                f"Имя: {self.name}, HP: {self.__hp}, Голод: {self.__hunger}, "
                f"Возраст: {self.__age}, Доверие: {self.__trust}, Мораль: {self.__morale}")

