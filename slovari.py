#Как работать со словарями
#Что такое словари и как их создавать
d = {}
s = {
    'a':1,
    'b':[1, 2, 3],
    'c':'abc'
}
print(d)
print(s)
s[1] = 123
print(s)
de = dict([(1, 'a'), (2, 'b'), (3, 'c')])
print(de)


#требования к ключам и значениям
#ключи не изменяемые  лист не может быть ключем
b = (1, 2, [1, 2, 3])
print(b)

#встроенные методы
#очистка
s.clear()
print(s)

print(de[2])
"""если ключа нее существует то выдаст ошибку  для этого используют метод
get() и если ключа нет то вернет nan"""
print(s.get(1000, -1))
#получение пар элементов
print(de.items())
print(de.keys())
print(de.values())

#обьудинение
q = {100:'abd', 1:'ddd'}
print(q)
q1 = {2: 'b', 1: 'a', (1, 2, 3): 'c'}
print(q1)
#перезапишет совпадающие кл≥чи и добавит новые
q.update(q1)
print(q)
q | q1
print(q)
#удаление pop удалит из словаря и вернет значение
print(q.pop(100))
print(q)
#удаляет последнее добавленное значение
q[(1, 2, 3)] = 'xyz'
print(q)
print(q.popitem())
print(q)
#просто удаляет по индексу
del q[1]
print(q)

fname = 'Mikhael'
sname = 'Shifrin'
tel = '+7926749275'
adr = 'Odinzcovo , Lenin st 54'
print(sname, fname,'\n',tel,'\n',adr)

#11 * 2**2 - 13 / 4 + 7
a = 2**2
b = 11 * a
c = 13 / 4
result = b - c + 7
print(result)
