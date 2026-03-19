#тернальный оператор
def pow(x,y):
    return x**y if y else x #проверяет пустое или нет
print(pow(3,None))
print(pow(5,5))
print(pow(2, 2))
