#name = input("Введите имя: ")
#10print(f"Привет, {name}!")


"""def pl(d, sh):
    a = (d * sh) / 100
    return a

dlin = float(input("Введите длинну участка в метрах: "))
shir = float(input("Введите ширину участка в метрах: "))
plosh = pl(dlin, shir)
print ("Площадь участка составалянт: ", plosh, "соток(а)")"""


'''number = input("Введите четырёхзначное число: ")
suma = 0
if len(number) != 4:# or not number.isdigit():
    print("Ошибка: введено неверное число.")
else:
    # Преобразуем каждую цифру в число и складываем их
    #sum_digits = sum(int(digit) for digit in number)
    for  digit in number:
        suma += int(digit)

    # Выводим результат

print(f"Сумма цифр числа равна: {suma}")'''

'''kolvo = int(input("Введите количество товаров: "))
dostavka = (kolvo * 30) +70
print(f"Сумма доставки: {dostavka}рублей")'''
'''import statistics

def med(*args):
    medi = statistics.median(args)
    return medi

print(med(5, 6, 7))'''


d = int(input("Введите количество дней: "))
h = int(input("Введите количество часов: "))
m = int(input("Введите количество минут: "))
s = int(input("Введите количество секунд: "))

smma_s = d * 86400 + h * 3600 + m * 60 + s

print(f"Ваш указанный период составляет {smma_s} секунд.")