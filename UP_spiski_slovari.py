#1
from collections.abc import Sequence

def check_list(var):
    if isinstance(var, list):
        return True
    else:
        return False

print(check_list([1, 2, 3]))    # True
print(check_list((1, 2, 3)))    # True
print(check_list("hello"))      # True
print(check_list({1, 2, 3}))

#2
def get_value_by_index(ref_list, index):
    if ref_list is None:
        return None
    if not isinstance(ref_list, list):
        return None
    if index < 0 or index >= len(ref_list):
        return None
    return ref_list[index]

print(get_value_by_index([10, 20, 30, 40, 50], 5))

#3
def list_reorder(list_of_lists):
    result = []
    for sublist in list_of_lists:
        for item in sublist:
            result.append(item)

    return result

print(list_reorder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

#4
'''def list_insert(ref_list, start, num, rep):
    for i in range(rep):
        ref_list.insert(start + i, num)

    return ref_list'''


def list_insert(ref_list, start, num, rep):
    if start < 0 or start > len(ref_list):
        return -1
    ref_list[start:start] += [num] * rep

    return ref_list

result = list_insert([1, 2, 3, 4, 5], 2, 99, 3)
print(result)

result = list_insert([10, 20, 30], 0, 5, 2)
print(result)

result = list_insert([1, 2, 3], 3, 100, 4)
print(result)

result = list_insert(['a', 'b', 'c'], 1, 'X', 1)
print(result)


#5

'''def generate_values(start, end):
    return list(range(start, end + 1))'''


def generate_values(start, end):
    if start <= end:
        step = 1
    else:
        step = -1

    return list(range(start, end + step, step))
print(generate_values(1, 10))

#6
def merge_dicts(dict1, dict2):
    return dict1 | dict2

result = merge_dicts({'a': 1, 'b': 2}, {'d': 20, 'c': 3})
print(result)

#7

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                result[key] = [result[key], value]
        else:
            result[key] = value

    return result
result = merge_dicts({'a': 1, 'b': 2}, {'c': 3, 'd': 4})
print(result)

#8
def count_elements(collection):
    result = {}

    for element in collection:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1

    return result
print(count_elements([1, 2, 3, 2, 1, 3, 3]))

#9

def get_value(data, key):
    return data.get(key, "Key not found")
d = {'a': 1, 'b': 2, 'c': 3}

print(get_value(d, 'a'))  # 1
print(get_value(d, 'c'))  # 3
print(get_value(d, 'x'))

#10

def sort_dict(d, type, order):
    reverse = (order == "desc")

    if type == "keywise":
        items = sorted(d.items(), key=lambda x: x[0], reverse=reverse)
    elif type == "valuewise":
        items = sorted(d.items(), key=lambda x: x[1], reverse=reverse)
    else:
        return d

    return dict(items)

data = {"b": 2, "a": 3, "c": 1}

print(sort_dict(data, "keywise", "asc"))