#приемы понятного кода
#статические методы
from collections.abc import async_generator


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def mul(self):
        return self.x * self.y
    @staticmethod #позволяет вызвать экземпляр класса не сщздввая
    def mul_any(x, y):
        return x**y

a = A(10, 15)
print(a.mul())
print(a.mul_any(10, 15))
print(A.mul_any(10, 15))
#классовые методы
class A1:
    age =15
    def __init__(self, age):
        self.age = age
    @classmethod#позволяет получать атрибуты классовые
    def show(cls):
        return cls.age

a = A1(25)
print(a.show(), a.age)

#геттеры и сеттеры
class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

p = Person(20)
print(p.get_age())
p.set_age(30)
print(p.get_age())


#магические методы
class Two_Div:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    def __add__(self, other):
        return Two_Div(self.value + other.value)

a =Two_Div(256)
b = Two_Div(100)
print((a + b) + a)

#Шаблон проектирования Синглтон


class FileRider:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            #ули обьекта еще нет
            cls.instance = super().__new__(cls)
            return cls.instance
        return cls.instance #если обьект уже есть

    def __init__(self, psth):
        self.psth = psth


a = FileRider('1.txt')
b = FileRider('2.txt')

print(a is b)
