#Как задавать аргументы и работать с ними
#задание аргументов
def pow(x, n):
    return x ** n
print(pow(5, 3))

#аргументы по умолчанию
def pow1(x, n=2):
    return x ** n
print(pow1(5))

#контроль за именовынами аргументами
def pow3(a, b, c, d = 100):
    return a + b + c + d
print(pow3(1, 2, 3))

#задаем аргументы которые обязаны быть указаны как именованые
def pow4(x, n, *, c, d = 100):
    return x * n + c * d
print(pow4(1, 2, c = 3))

