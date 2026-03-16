#создание массивов списков
a = [1, 2, 3, 'd', 4, True]
print(a)

#встроенные методы работы со списками
#добавление в конец списка
a =[]
a.append(1)
print(a)
a.append(2)
print(a)
#очистка списка
a.clear()
print(a)
#копирование списка
arr = [1, 2, 3]
old_arr = arr #не копирует а просто указывает на ту же ячейку и все изменения происходит в обеих переменных
arr[0] = -100
print(arr, old_arr)
old_arr2 = arr.copy() #копирует и создает новую ячейку памяти
arr[0] = 1000
print(arr, old_arr2)
#подсчет элементов
b = [1, 2, 3, 1, 10, 'a', 158, 1]
print(b.count(1))

#Как добавить элемент с помощью метода extend
arr.extend(b)
print(arr)

#Как найти позицию элемента в списке с помощью index
#первое вхождение элемента
users = [1, 2, 3, 4, 1, 15, 3, 28, 1, 100]
dates = ['2022-01-15', '2022-01-16', '2022-03-23', '2011-04-14']
print(users.index(3))
print(dates[2])

#Как добавить элемент в список с помощью insert
arr.insert(2, 100)
print(arr)
arr.insert(int(len(arr) / 2), 'insert')
print(arr)

#Как удалять элементы из списка с помощью методов pop и remove
q = arr.pop(0)
print(arr)
print(q)

arr.remove('insert')
arr.remove('a')
print(arr)

#Как переворачивать и сортировать списки с помощью методов reverse и sort
arr.reverse()
print(arr)
arr.sort()#сортирует числа если попадает стринг выдает ошибку
print(arr)

#Как проверить наличие элемента в списке с помощью оператора in
tree = 3
print(tree in arr)

arr.append(['a', 'b', 'c'])
lst = ['a', 'b', 'c']
print(arr)
print(arr.pop(len(arr) - 1))
print(arr)
s = arr.copy()
c = arr.copy()
s.append(lst)#добавляет список
print(s)
c.extend(lst)#добавляет обьекты
print(c)

#Как работают индексы и срезы в списках
print(s[7])
print(s[3:10])#выводятся элементы в диапазоне е
print(s[-3:-1])#при отрицательной индексации идет с конца
print(s[-1])# последний элемент списка
print(s[0:10:2])#последняя показывает шагт вывода

#Как правильно перевернуть список
print(s)
print(s[::-1])# переворачивает список не изменяя его
print(s)
#сложная сортировка
arr3 = ['aa', 'abb', 'cc', 'bc']#
print(arr3)
arr3.sort()# работает с одинаковыми данными
print(arr3)# распечатка