from catgirl import Catgirl
from catboy import Catboy
from dogboy import Dogboy
from doggirl import Doggirl


def display_instructions():
    #Выводит инструкции по игре.
    print("Добро пожаловать в Тамагочи!")
    print("Заботьтесь о питомце, у него есть здоровье, голод, возраст, доверие и мораль.")
    print("Действия:")
    print("  q - выход")
    print("  b - бить (10 урона, -10 доверия, -20 морали)")
    print("  h - лечить (+15 здоровья, +5 доверия, +5 голода)")
    print("  f - кормить (-20 голода, +5 морали)")
    print("  u - обнимать (зависит от доверия)")
    print("  p - играть ('ball' или 'chase')")
    print("  s - говорить ('insult' или 'support')")
    print("Если мораль = 0, питомец может сбежать или покончить с собой!")
    print("  a - вывести меню действий")

def main():
    player_name = input("Как к вам обращаться? ")
    print(f"Привет, {player_name}!")

    pet_type = input("Выберите тип питомца :\n"
                     "  c - кошка \n"
                     "  d - собака \n"
                     "").lower()
    pet_sex = input("Выберите пол питомца :\n"
                    "  m - мальчик\n"
                    "  f - девочка").lower()
    pet_name = input("Дайте имя вашему питомцу: ")
    if pet_type == "c":
        if pet_sex == "m":
            pet = Catboy(pet_name)
        else:
            pet = Catgirl(pet_name)
    elif pet_type == "d":
        if pet_sex == "m":
            pet = Dogboy(pet_name)
        else:
            pet = Doggirl(pet_name)
    else:
        print("Нет такого варианта.")
        return

    display_instructions()
    print(pet)


    action = input("Выберите действие: ")
    while action != 'q':
        if action == 'b':
            pet.bit()
        elif action == 'h':
            pet.heal()
        elif action == 'f':
            pet.feed()
        elif action == 'u':
            pet.hug()
        elif action == 'p':
            activity = input("Выберите игру ('ball' или 'chase'): ").lower()
            pet.play(activity)
        elif action == 's':
            speech_type = input("Выберите тип речи ('insult' или 'support'): ").lower()
            pet.speak(speech_type)
        elif action == 'a':
            display_instructions()
        else:
            print("Неверный ввод.")
        if action != 'a':
            pet.age_up()
        print(pet)
        action = input("Выберите действие: ")

    print(f"До свидания, {player_name}!")

if __name__ == "__main__":
    main()