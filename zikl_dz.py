
#пример кода, которые проверяет, являются ли два слова анаграммами
'''def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)
word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")
if is_anagram(word1, word2):
    print("Слова являются анаграммами.")
else:
    print("Слова не являются анаграммами.")'''

'''days_per_month = {
    'январь': 31,
    'февраль': '28 или 29',
    'март': 31,
    'апрель': 30,
    'май': 31,
    'июнь': 30,
    'июль': 31,
    'август': 31,
    'сентябрь': 30,
    'октябрь': 31,
    'ноябрь': 30,
    'декабрь': 31
}

# Получаем от пользователя название месяца и приводим к нижнему регистру для унификации
user_input = input('Введите название месяца: ').strip().lower()

# Проверяем, есть ли введённый месяц в нашем словаре
if user_input in days_per_month:
    days = days_per_month[user_input]
    # Форматируем вывод: первый символ названия месяца — заглавный
    month_name = user_input.capitalize()
    if user_input == 'февраль':
        print(f'{month_name}: {days} дней (зависит от високосного года).')
    else:
        print(f'{month_name}: {days} дней.')
else:
    print('Ошибка: месяц с таким названием не найден. Проверьте правильность написания.')'''

# Инициализируем общую стоимость билетов
'''total_cost = 0.0
print("Для подсчета ввода введите пустой ввод (просто нажмите Enter)")
while True:
    age_input = input("Введите возраст посетителя (или нажмите Enter для завершения): ").strip()
    if age_input == "":
        break

    else:
        # Преобразуем ввод в целое число
        age = int(age_input)
        if age <= 2 or age > 65:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 200
        else:
            ticket_price = 1000
        total_cost += ticket_price
print(f"\nОбщая стоимость билетов для группы: {total_cost:.2f} руб.")'''
'''import calendar
def get_days_in_month(month, year):
    if not (1 <= month <= 12):
        raise ValueError("Номер месяца должен быть в диапазоне от 1 до 12")
    _, num_days = calendar.monthrange(year, month)
    return num_days


month_input = input("Введите номер месяца (1–12): ").strip()
yearinput = input("Введите год (четырёхзначное число): ").strip()
month = int(month_input)
year = int(yearinput)
days = get_days_in_month(month, year)

print(f"В месяце {month} {year} года {days} дней.")'''

'''x = 10
y = 0
while x != 5:
    x = x - 1
    y = y + 2 * y - 3
if x == y:
    x = x - y                     # после этого блока x = 0
    y = y + x                     # после этого блока y == y
else:
    x = x + y
    y = y - x                      # после этого блока y = -x
print(y)

Этот код можно упростить, если убрать из него выражения, которые выдают одинаковый результат независимо от значений переменных:

x = 10
y = 0
while x != 5:
    x = x - 1
    y = y + 2 * y - 3
if x == y:
    print(y)
else:
    y = -x
print(y)'''

'''def caesar_cipher(text, shift=3):
    result = []

    for char in text:
        if not char.isalpha():
            result.append(char)
        else:
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))

    return ''.join(result)

input_text = input("Введите текст для шифрования: ")
encrypted_text = caesar_cipher(input_text)

print(f"Зашифрованный текст: {encrypted_text}")'''

'''list = [2, 4, 8]


print(list[::-1])
print(list)

list = [2, 4, 8]
list.reverse()
print(list)'''

'''a = [1, 1, 2, 3, 5, 8, 34, 55, 89]
b = []
for i in a:
    if i < 5:
        b.append(i)
print(b)'''

'''a = int(input("Введите число: "))
if a % 2 == 0:
    print(f"{a} — чётное")
else:
    print(f"{a} — нечётное")'''

'''A = int(input('Введите число А: '))
B = int(input('Введите число B: '))
C = int(input('Введите число C: '))
if A == B:
    С = A + B
    E = B + C
else:
    if B < C:
        A = A + B
        E = A + C
    else:
        B = C + B
        E = A + B
print(E)'''

# Ширина ячейки для форматирования (4 символа, выравнивание по правому краю)
'''sh = 4
print(" " * sh, end="")
for col in range(1, 11):
    print(f"{col:>{sh}}", end="")
print()

for row in range(1, 11):
    print(f"{row:>{sh}}", end="")
    for col in range(1, 11):
        product = row * col
        print(f"{product:>{sh}}", end="")

    print()
'''


'''import random

def chisla():
    numbers = random.sample(range(1, 50), 6)
    numbers.sort()
    return numbers

chis = chisla()
print(chis)'''


'''def chisla():
    chis = []
    while True:
        number = int(input("Введите целое число: "))
        if number == 0:
            break
        chis.append(number)
    return chis

chis = chisla()
for i in sorted(chis):
    print(i)'''

def add_numbers():
    user_input = input("Введите число: ")
    if user_input == "":
        return 0.0
    else:
        return float(user_input) + add_numbers()
sum = add_numbers()
print("Сумма чисел составляет:", sum)