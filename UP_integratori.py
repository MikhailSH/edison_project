#Что такое итераторы и генераторы в Python

lst = [1, 2, 3]
for il in lst:
    print(il)


#lst это список значит итерируемый обьект
it = iter(lst)

# теперь it это итератор
'''
while True:
        print(next(it))'''


#Generatori
#opredelenie  yield
def pow(x):
        while True:
            yield x**2
            x +=1

p = pow(5)
print(p)

print(next(p))

