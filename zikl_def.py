#использование в функциях
def number_estim(a):
    if a < 5:
         return 'маленькое число'
    elif a < 10:
        return 'среднее число'
    elif a < 20:
        return 'приличное число'
    else:
        return 'реально большое число'

print(number_estim(10))
print(number_estim(50))
print(number_estim(5))

#комбиниров
a = 10
b = 100
c = 50
if a > 5 and b >10 and c > 15:
    print('все числа большие')

a = 1
b = 100
c = 50
if a > 5 or b >10 or c > 15:
    print('все числа большие')