#рекурсия

#факториал
def fak(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(fak(4))

def fak2(n):
    if n == 1:
        return 1
    return fak2(n-1) * n

print(fak2(5))


#фибаначи
def fib(n):
    if n == 0:
        return 0
    if n == 2:
        return 1

    a, b = 0, 1
    cnt = 1
    while cnt < n:
        a, b = b, a + b
        cnt += 1
    return a

for i in range(1, 100):
    print(fib(i))


def fib2(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib2(n-1) + fib2(n-2)

for i in range(1, 10):
    print(fib2(i))