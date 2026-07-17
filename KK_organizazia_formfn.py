
'''def greet_user():
    name = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    print(f"Привет, {name}! Тебе {age} лет")


greet_user()'''


def greet_user():
    name = input("Введите ваше имя: ")

    age_input = input("Введите ваш возраст: ")

    try:
        age = int(age_input)
    except ValueError:
        print("Ошибка: возраст должен быть целым числом!")
        return

    if age < 18:
        print("Доступ ограничен")
    else:
        print(f"Привет, {name}! Тебе {age} лет. Доступ открыт")

greet_user()