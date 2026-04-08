#считывает время
import time

current_time = time.asctime()
print(current_time)

def find_longest_word(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        words = content.split()
        longest_word = max(words, key=len)
        longest_word_length = len(longest_word)
        longest_words = []
        for word in words:
            if len(word) == longest_word_length:
                longest_words.append(word)

    return longest_word_length, longest_words

file_path = input("Enter the file path: ")
word_length, longest_words = find_longest_word(file_path)

print("The length of the longest word(s) is:", word_length)
print("The longest word(s) is/are:", longest_words)
#-------------------------

source_file = input("Введите имя исходного файла: ")
target_file = input("Введите имя целевого файла: ")

with open(source_file, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

with open(target_file, 'w', encoding='utf-8') as outfile:
    for i, line in enumerate(lines, start=1):
        outfile.write(f"{i}: {line}")

print(f"Нумерация завершена. Результат сохранен в '{target_file}'")