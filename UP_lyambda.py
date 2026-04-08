#базовый синтаксис

'''lambda  аргументы : тело функции
всегда пишется в одну строку и нет имени'''
from slovari import result

#пример одной переменной
make_sgear = lambda x: x**2
print(make_sgear(10))

#пример несколько переменных
adder = lambda x, y, z: x + y + z
print(adder(4, 5, 6))

#пример без переменных
PI = 3.14
return_pi = lambda : PI
print(return_pi())


#а что нельзя в лямбда
'''return, assert, pass, многострочность '''

#сценарии программирования
#декларативный стиль
lst = [1,2,3,4,5,6]
print(lst)
result = []
for el in lst:
    if el % 2 == 0:
        result.append(el)

print(result)


#filter + lambda
#функциональное программировани
print(list(filter(lambda x: x % 2 == 0, lst)))

# map + lambda
# возводим в квадрат
print(list(map(lambda x: x**2, lst)))
#приводим к целому числу
lst1 = [1.5, 1e-5, 1.23e+1, 5, 1.108]
print(list(map(lambda x: int(x), lst1)))

lst2 = [1.5, 1e-5, 1.23e+1, 5, '1.108']
print(list(map(lambda x: x if isinstance(x, (int, float)) else eval(x), lst2)))

#несколько переменных
ls1 = [1, 2, 3, 4, 5]
ls2 = [5, 4, 3, 2, 1]
print(list(map(lambda x, y: x > y, ls1, ls2)))

#условия
lst2 = [1.5, 1e-5, 1.23e+1, 5, '1.108']
print(list(map(lambda x: x if isinstance(x, (int, float)) else eval(x), lst2)))

#reduce + lambda
from  functools import reduce
lst5 = [1, 10, -1, 5, 6, 3]
print(reduce(lambda x, y: x +y, lst5))

#находим самое большое значение в списке
print(reduce(lambda x,y: x if x > y else y, lst5))

#lambda + сортировка
class Person:
    age = 0
    name = ''

Mike = Person()
Mike.name = 'Mike'
Mike.age = 15

Joe = Person()
Joe.name = 'Joe'
Joe.age = 20

Mary = Person()
Mary.name = 'Mary'
Mary.age = 13

lst6 = [Mike, Joe, Mary]
print(lst6)
#отсортировали по возрасту
lst6.sort(key=lambda x: x.age)
print(lst6)
for person in lst6:
    print(person.name)


#сортировка по второму признаку
bc =[['Andron', 5], ['Ivan', 7], ['Kiril', 3], ['Aaron', 1]]
print(sorted(bc, key=lambda x: x[1]))



#как проверить что перед нами Лямбдф
from types import LambdaType
x = lambda x: x**2
print(isinstance(x, LambdaType))


