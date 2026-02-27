a = "первая строка"
b= 'вторая строка'
c = a + ' ' + b
d = a * 5
e = (a + ' ') * 5
print(len(e))
print(a, b, c, d, e, sep='\n')
print("он сказал 'нет'")
print("он сказал \"нету\"")
print("он сказал 'нет' \nона сказала да")
print("он сказал 'нет' \n\tона сказала да")
print("он сказал 'нет' \\n\tона сказала да")
print("он сказал 'нет' \n\tона сказала да", end='!\n')

greeting = """привет друг!
ты совершил покупку и скоро ее получишь"""
print(greeting)
name = 'Миша'
bundle = "персональ"
days = 5
print("""привет {}!
ты совершил покупку {} и скоро ее получишь {}""".format(name, bundle, days))
#f строки
print(f"""привет {bundle}!
ты совершил покупку {name} и скоро ее получишь {days}""")
#пример формата числа
print("это число П: {0:.2f}".format(3.14268687726439))

#как убрать пробелы и лишние символы
prob = '   Iпробел   x'
print(prob)
print(prob.strip())
print(prob.strip(' x'))



#как разбить строку по разделителю
keyword = 'питон, анализ данных, программирование, я люблю котэ'
print(keyword.split(', '))
chep = """
первое предложение
второе предложение
третье и перенос строки"""
print(chep.split('\n'))

#обьединение строк
arr = ["меня зовут миша", "моя собака Грут", "я учу Питон"]
print(arr)
print('\n'.join(arr))

#Как проверять и изменять регистр букв
f ='СЕКу РегиСТР меНять'
print(f)
print(f.capitalize(), f.upper(), f.title(),f.lower(),f.swapcase(),  sep='\n')

#проверить находится ли строка в каком то одном регистре
print(f.islower(), f.lower().islower())

#Как проверять наличие символов и подстрок и заменять элементы
arr1 = 'Обычное предложение'
arr2 = 'Предложение с восклицанием!'
print(arr1.startswith('Обычное'))
print(arr2.startswith('Обычное'))
print(arr1.endswith('!'))
print(arr2.endswith('!'))
#наличие подстроки
arr3 = 'Длинная строка с некоторым текстом внутри текста'
print(arr3.find('некоторым'))#позиция
print('некоторым' in arr3)#проверит да или нет
print(arr3.replace(' ', ','))# заменв

#Как индексируются строки
print(arr3[17])
print(arr3[17:])
print(arr3[17:20])
#=====================================
# Присваивание строки переменной text
text = "Python - замечательный язык программирования!"
# Разворот строки задом наперед с помощью среза [::-1]
reversed_text = text[::-1]
# Проверка результата
print(reversed_text)
#===============================

data = '42'
integer_data = int(data)
print(integer_data)
float_data = float(data)
print(float_data)
string_data = data
print(string_data)
list_data = list(data)
print(list_data)
st = len(arr3)
print(st)

number = 42
message = f"Ваше любимое число - {number}."

str = '  Привет, мир!  '
stripped_text = str.strip(' ')
#-------------------------------------------
# Создаем список элементов
elements_list = ["Hello", "World", "Python"]

# Объединяем элементы списка в строку через пробел
joined_string = " ".join(elements_list)

# Проверка результата
print(joined_string)
#___________________________----------------

text = 'Программирование на Python - это весело и мощно!'
starts_with_programming = text.startswith('Программирование')
ends_with_powerful = text.endswith('мощно')
print(starts_with_programming, ends_with_powerful)

#===============================
#заменить одно слово на другое
text = 'Python - замечательный язык программирования!'
old_substring = 'замечательный'
new_substring = 'удивительный'
modified_text = text.replace(old_substring, new_substring)
print(modified_text)