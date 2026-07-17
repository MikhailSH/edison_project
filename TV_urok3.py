results = [65, 72, 81, 88, 65, 72, 76, 88, 92, 7]

# Среднее значение
mean = sum(results) / len(results)

# Мода
frequencies = {}
for result in results:
    if result not in frequencies:
        frequencies[result] = 1
    else:
        frequencies[result] += 1
max_frequence = max(frequencies.values())
mode = [k for a, v in frequencies.items() if a == max_frequence]

# Дисперсия
delta = [(result - mean) ** 2 for result in results]
dispersion = sum(delta) / len(results)

# Вывод результатов
print(f"Среднее значение: {mean}")
print(f"Мода: {mode}")
print(f"Дисперсия: {dispersion}")