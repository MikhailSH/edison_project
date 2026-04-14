#ploskiy rorteq
#1
def flatten_tuple(tup):
    return [item for subtuple in tup for item in subtuple]

lst =[[1, 2, 3], [3, 4], [], [5, 6, 7, 8]]
print(flatten_tuple(lst))

#2
def sum_positive_numbers(numbers):
    return sum(num for num in numbers if num > 0)
lst1 = [1, -2, 3, 4, -5, 6]
print(sum_positive_numbers(lst1))

#3
def process_array(numbers):
    return [num * 2 for num in numbers if num > 0]
lst1 = [1, -2, 3, 4, -5, 6]
print(process_array(lst1))

#4
def list_to_dict(keys, values):
    return {k: v for k, v in zip(keys, values)}
lst2 = ['1', '3', '5']
lst3 = ['Musik', 'sound', 'Pevez']
result = list_to_dict(lst2, lst3)
print(result)

#5
def sum_n_dimensional_vectors(vectors):
    return [sum(components) for components in zip(*vectors)]

vek = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = sum_n_dimensional_vectors(vek)
print(result)


def sum_n_dimensional_vectors(vectors):
    result = [0] * len(vectors[0])
    for vector in vectors:
        result = list(map(lambda x, y: x + y, result, vector))

    return tuple(result)
vek = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = sum_n_dimensional_vectors(vek)
print(result)
#6
def lim_max(nums, limit):
    max_value = -1

    for num in nums:
        if num < limit and num > max_value:
            max_value = num

    return max_value
num = (1, 5, 3, 9, 2, 7)
result = lim_max(num, 8)
print(result)

#7

def lim_max(nums, limit):
    filtered = [num for num in nums if num < limit]
    return max(filtered) if filtered else -1
num = (1, 5, 3, 9, 2, 7)
result = lim_max(num, 8)
print(result)