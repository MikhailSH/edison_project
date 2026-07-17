# Данные из таблицы
exam_tickets = ["Да", "Нет", "Да", "Да", "Нет", "Да", "Да", "Да", "Нет", "Да", "Да", "Да", "Да"]

# Вероятность успешной сдачи, если пойдет вечером гулять
probability_walk = exam_tickets.count("Да") / len(exam_tickets)

# Вероятность успешной сдачи, если не пойдет гулять и выучит еще 2 билета
probability_study = (exam_tickets.count("Да") + 2) / len(exam_tickets)

# Изменение вероятности
probability_delta = probability_study - probability_walk

# Вывод результатов
print(f"Вероятность успешной сдачи (гулянка): {probability_walk:.2%}")
print(f"Вероятность успешной сдачи (учеба): {probability_study:.2%}")
print(f"Изменение вероятности: {probability_delta:.2%}")