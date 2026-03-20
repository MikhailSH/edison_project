#как избегать длинных условий
class Competition:
    is_active = True
    rem = 10

    @property
    def is_actual(self):
        if comp.is_active and comp.rem > 0:
            return True
        return False

class Person:
    age = 15
    level =5
    @property
    def mach_con(self):
        if per.age > 15 and per.level > 3:
            return True
        return False

comp = Competition()
per = Person()

if comp.is_actual and per.mach_con:
    ...
else:
    print('вы не соответствуете условиям начисления балов')

    """можно зашивать проверки в класы и функции"""
