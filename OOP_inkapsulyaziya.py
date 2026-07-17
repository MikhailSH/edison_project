#inkapsulyaziya
#public, privete, protected

class Person:
    def __init__(self, name, salary, secret):
        self.name = name # public доступен везде
        self._salary = salary #protected из вне не можем вызвать но внутри классса и дочерние классы видят
        self.__secret = secret #privete только внутри класса
    def print_name(self):
        print(self.name)

    def print_salary(self):
        print(self._salary)

    def print_secret(self):
        print(self.__secret)

p = Person(name='Mikhael', salary=20000, secret=123456)
p.print_name()
p.print_salary()
p.print_secret()
print(p.name)
print(p._salary)
#print(p.__secret) #выдаст ошибку
print(p._Person__secret)#данные можно вытащить

class Person1:
    def __init__(self):
        self.is_hungry = False

    def eat(self):
        self.is_hungry = True

p = Person1()

print(f"до еды: {p.is_hungry}")
p.eat()
print(f'после еды: {p.is_hungry}')


