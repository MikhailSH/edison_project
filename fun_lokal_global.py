#Как работать с локальными и глобальными переменными
def foo(x):
    return x * x
x = 100
z = foo(x)
print(z)
print(x)


#это редко используется
def foo(y):
    global a
    a +=5
    return a
a= 100
z = foo(a)
print(z)
print(a)