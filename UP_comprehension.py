#list comprehesion
#базовый лист
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for el in lst:
    result.append(el**2)

print(result)

#ili
print([el**2 for el in lst])


t = list(range(51))
print(t)
from math import sin
print(list(map(sin, t)))
#ili
print([sin(ti) for ti in t])


#добавление условий
lst1 = [1, [1, 2], [3, 4, 5], 10]
print([len(el) for el in lst1 if isinstance(el, list)])
print([len(el) if isinstance(el, list) else 1 for el in lst1 ])

#neskolko listov
lst11 =[[1, 2, 3], [3, 4], [], [5, 6, 7, 8]]
result = []
for sub in lst11:
    for el in sub:
        result.append(el)
print(result)
#ili

print([el for sub in lst11 for el in sub ])

#Generator mno;tcnd

lst2 = [[1, 2, 3],[], [1, 5, 18], [], [2, 4, 7, 9,10]]
result = []
for sub in lst2:
    for el in sub:
        if el%2 == 0 and el not in result:
            result.append(el)
print(result)
#ili

print({el for sub in lst2 for el in sub if el%2 == 0})



#zip_longest

nums = [1,2,3]
nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 3, 4, 5]
for x, y, z in zip(nums1, nums2, nums):
    print(x, y, z)

#ili
from itertools import zip_longest
for x, y, z in zip_longest(nums1, nums2, nums, fillvalue=0):
    
    print(x, y, z)



