#как написать while
i =0
while i < 15:
    i = i + 1
    print(i)

num = True
a = 10000
while num:
    a/=2
    if a < 100:
        num = False

print(a)


arr = [1, 2, 3, 4, 5]
while arr:
    print(arr.pop(0))

#for
arr = [1, 2, 3, 4, 5]
for el in arr:
    print(el)

for i in range(len(arr)):# не очень хороший код
    print(arr[i])


arr = ['a', 'b', 'c']
print(list(enumerate(arr)))


for i, el in enumerate(arr):
    print(i, el)

names = ['Миша','Таня', 'Никита', 'Соня']
car = ['ford', 'opel', 'bently', 'mersedes']
col = ['синий', 'белый', 'зеленый', 'красный']
for  name, ca, co in zip(names, car, col):# зип найдет минимальный список
    print(f'у {name} машина {ca} любимый цвет {co}')


#continue break else
#continue прерывает и прыгает на другой круг
arr = [1, 2, 3, 'dfagagag', 4, 5]
for el in arr:
    if not isinstance(el, int):
        continue
    print(el**2)

#    break выбрасывает из цыкла

arr = [1, 2, 3, 'dfagagag', 4, 5]
for el in arr:
    if not isinstance(el, int):
        print('не тот элемент')
        break
    print(el**2)


#else есди цикл закончится сам то else отработает но если прервать не отработает
i = 0
while i < 10:
    i += 1
    print(i)
    if i == 5:
        break
else:
    print('блок else')




