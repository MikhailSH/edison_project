#наследование
class Animal:
    def move(self):
        print("я гордый хожу как хочу")

    def say_about(self):
        print("я животное в широком смысле слова")

class Cat(Animal):#так наследуется
    def move(self):
        print("я тихая кошка, окуратная")

    def talk(self):
        print("ьяу ьяу")
        super().say_about()# запрашивает метод из родителтского класса


c = Cat()
print(c.move())
print(c.talk())
print(c.say_about())

class Caunter:
    def __init__(self, value):
        self.value = value
    def add_value(self, value):
        self.value += value

class SecondCaunter(Caunter):
    def add_value(self, value):
        self.value += 2 * value
        print(1)

sc = SecondCaunter(5)
print(sc.value)
sc.add_value(10)
print(sc.value)



