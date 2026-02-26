
from math import floor, ceil
a = 1
type(a)
print(type(a))
print(a + 1)
print("buba")

exponential_num = 1.5e-3
print(exponential_num)
decimal_num = exponential_num
print(decimal_num)

number = 10.832468
rounded_number = round(number, 3)
print(rounded_number)

number = 78.57234825
rounded_down_number = floor(number)
print(rounded_down_number)

complex_num = 4 + 6j
real_part = complex_num.real
imaginary_part = complex_num.imag
print(real_part)
print(imaginary_part)

# Создаем комплексное число
complex_num = 7 + 2j

# Находим комплексно-сопряжённое число
conjugate_num = complex_num.conjugate()

print("Комплексное число:", complex_num)
print("Комплексно-сопряжённое число:", conjugate_num)