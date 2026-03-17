#Что такое кортежи и как их создавать
#создание кортежа
a = (2,3,4)
c = []
c.extend('abcde')
b = tuple(c)
print(c)
print(a)
print(b)
print(c.__sizeof__(), b.__sizeof__())

#кортеж не изменяемый обьект
#в список в кортеже можно добавить элемент
s = (1, 'fbcde', [100])
print(s)
s[2].append(300)
print(s)

#методы работы с кортежем
f = (1, 2, 3, 1, 5)
print(f)
print(f.count(1))
print(f.index(2))

#распаковка кортежей
tup = (1, 'a', True)
print(tup)
num, st, flag = tup
print(num)
print(st)
print(flag)
