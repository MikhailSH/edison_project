#1

def find_unique_elements(lst):
    return sorted(set(lst))
nums = [5, 3, 5, 2, 3, 1]
print(find_unique_elements(nums))

#2
def sums_by_quarter(values):
    if len(values) != 12:
        raise ValueError("Нужно передать ровно 12 значений — по одному на каждый месяц года")

    return [
        sum(values[0:3]),   # 1 квартал: янв–мар
        sum(values[3:6]),   # 2 квартал: апр–июн
        sum(values[6:9]),   # 3 квартал: июл–сен
        sum(values[9:12])   # 4 квартал: окт–дек
    ]

temps = [1, 2, 3,  4, 5, 6,  7, 8, 9,  10, 11, 12]
print(sums_by_quarter(temps))


#3
def sorted_unique_list(nums):
    return sorted(set(nums))

data = [5, 3, 5, 2, 3, 1]
print(sorted_unique_list(data))

#4
def count_frequency(names):
    freq = {}
    for name in names:
        freq[name] = freq.get(name, 0) + 1

    return dict(sorted(freq.items()))

names = ["Anna", "Bob", "Anna", "Clara", "Bob", "Anna"]
print(count_frequency(names))



#5
'''def flatten_nested_list(nested):
    return [item for sublist in nested for item in sublist]'''
def flatten_nested_list(nested):
    flat = []

    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_nested_list(item))
        else:
            flat.append(item)

    return flat
data = [[1, 2, 3], [4, 5], [6]]
print(flatten_nested_list(data))

#6

def process_commands(commands):
    result = []

    for index, command in enumerate(commands):
        if command == "execute":
            result.append(index)
        elif command == "skip":
            continue
        elif command == "stop":
            break

    return result
cmds = ["execute", "skip", "execute", "stop", "execute"]
print(process_commands(cmds))

#7
def forest_adventure(path):
    if path == "left":
        return "Вы выбрали левый путь. По этому пути вы найдете старую пещеру с сокровищами. Остерегайтесь, внутри могут скрываться опасности, но, возможно, вы сможете обнаружить древние сокровища."
    elif path == "center":
        return "Вы выбрали центральный путь. Здесь вас ожидает таинственный храм. Вам предстоит пройти испытание мудрости и смекалки, чтобы получить древние знания."
    elif path == "right":
        return "Вы выбрали правый путь. По этому пути вы наткнетесь на племя дикой природы. Они согласны поделиться с вами своими тайнами, но сначала вам придется доказать свою отвагу в опасной схватке."
    else:
        return "Такого пути нет. Выберите: left, center или right."


choice = 'left'

print(forest_adventure(choice))

'''def forest_adventure(path):
    if path == 'left':
        return "Вы выбрали левый путь. По этому пути вы найдете старую пещеру с сокровищами. Остерегайтесь, внутри могут скрываться опасности, но, возможно, вы сможете обнаружить древние сокровища."
    elif path == 'center':
        return "Вы выбрали центральный путь. Здесь вас ожидает таинственный храм. Вам предстоит пройти испытание мудрости и смекалки, чтобы получить древние знания."
    elif path == 'right':
        return "Вы выбрали правый путь. По этому пути вы наткнетесь на племя дикой природы. Они согласны поделиться с вами своими тайнами, но сначала вам придется доказать свою отвагу в опасной схватке."
    else:
        return "Вы выбрали неизвестный путь. Пожалуйста, выберите 'left', 'center' или 'right'."

# Пример использования:
chosen_path = 'left'
print(forest_adventure(chosen_path))  # Выведет текстовое описание левого пути'''


#8

def de_none(lst):
    res = []
    for item in lst:
        if item is not None:
            res.append(item)
    return res

data = [1, None, 2, None, 3, None, 4]
print(de_none(data))

#9
'''def segment(num, scale):

    if num in scale:
        return (num, num)

    for i in range(len(scale) - 1):
        left = scale[i]
        right = scale[i + 1]

        if num == left or num == right:
            return (left, right)

        if left < num < right:
            return None

    return None'''

'''def segment(num, scale):

    minimum = min(scale)
    maximum = max(scale)

    if num < minimum or num > maximum:
        return None

    if num in scale:
        return (num, num)

    for value in scale:
        if num == value - 1 or num == value + 1:
            idx = scale.index(value)
            left_idx = max(0, idx - 1)
            right_idx = min(len(scale) - 1, idx + 1)
            return (scale[left_idx], scale[right_idx])

    return None'''
def segment(num, scale):
    min_value = min(scale)
    max_value = max(scale)

    if num in scale:
        return (num, num)

    for i in range(len(scale) - 1):
        if scale[i] < num < scale[i+1]:
            return (scale[i], scale[i+1])

    return None

scale = [10, 20, 30, 40]

print(segment(20, scale))   # (20, 20) — num совпадает с элементом
print(segment(10, scale))   # (10, 10) — тоже совпадает
print(segment(25, scale))   # None — между 20 и 30, не сосед
print(segment(15, scale))   # None — между 10 и 20, не сосед
print(segment(30, scale))

