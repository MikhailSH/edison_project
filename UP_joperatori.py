#*

a = 5
print(a * 5)
print(a**5)

#raspakovka obektov
l = [1, 2, 3, 4, 5]
b = l[0]
c = l[1:]
print(b)
print(c)
#ili
s, *k = l
print(s)
print(k)

q = [1, 2, 3]
q1 = (4, 5, 6)
q2 = {7, 8, 9}
print(*q, *q1, *q2)
from math import *
print(sin(pi))
print(cos(pi))