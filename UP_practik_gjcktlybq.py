#1

def process_args(*args, **kwargs):
    result = {}

    for index, value in enumerate(args, start=1):
        key = f"positional_{index}"
        result[key] = value

    for key, value in kwargs.items():
        result[key] = value

    return result

result = process_args(1, 2, 3, a=10, b=20)

print(result)

#2
def multiply_string(text, multiplier=1):
    return text * multiplier

print(multiply_string("hi"))        # "hi"
print(multiply_string("hi", 3))     # "hihihi"
print(multiply_string("python", 0))
#3
from functools import reduce

def sum_of_squares(nums):
    return reduce(lambda acc, x: acc + x * x, nums, 0)
print(sum_of_squares([1, 2, 3, 4]))

#4
def divide_numbers(a, b):
    try:
        return a/b
    except ZeroDivisionError as err:
        return str(err)
    except TypeError as err:
        return str(err)
    except Exception as err:
        return str(err)
'''def divide_numbers(a, b):
    try:
        return a/b
    except:
        print(f"произошла ошибка a = {a}, b = {b}")
print(divide_numbers(1, 0))
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        return f"Ошибка: деление на ноль ({e})"
    except TypeError as e:
        return f"Ошибка: некорректные типы данных ({e})"'''

print(divide_numbers(10, 2))     # 5.0
print(divide_numbers(10, 0))     # "Ошибка: деление на ноль (...)"
print(divide_numbers("10", 2))
#5
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as err:
        return str(err)
    except TypeError as err:
        return str(err)
    except Exception as err:
        return str(err)
    else:
        return result
    finally:
        print("Завершение операции деления")

print(divide_numbers(10, 2))
#6
def validate_and_format_phones(phones):
    result = []

    allowed_separators = {' ', '-', '(', ')'}

    for raw in phones:
        s = str(raw)
        plus_count = 0
        for i, ch in enumerate(s):
            if ch == '+':
                plus_count += 1
                if i != 0 or plus_count > 1:
                    result.append("Invalid")
                    break
            elif not (ch.isdigit() or ch in allowed_separators):
                result.append("Invalid")
                break
        else:
            digits = ''.join(ch for ch in s if ch.isdigit())
            if len(digits) != 11:
                result.append("Invalid")
                continue
            if digits[0] not in ('7', '8'):
                result.append("Invalid")
                continue
            digits = '7' + digits[1:]

            country = digits[0]
            code = digits[1:4]
            part1 = digits[4:7]
            part2 = digits[7:11]

            formatted = f"+{country}({code}){part1}-{part2}"
            result.append(formatted)

    return result
phones = [
    "+7 (123) 456-7890",
    "8-123-456-7890",
    "71234567890",
    "7(123)45-6-78-90",
    "9(123)456-7890",
    "7(123)456-78"
]

print(validate_and_format_phones(phones))
#7
import re

def find_dates_in_text(text):
    pattern = r"\d{4}-\d{2}-\d{2}"
    return re.findall(pattern, text)
text = "Встреча 2024-01-15, дедлайн 2025-12-31, а это просто 2024-99-99."
print(find_dates_in_text(text))
#8
import re

def extract_url_without_scheme(web_url):
    pattern = r"^[a-zA-Z]+://"
    result = re.sub(pattern, "", web_url)
    return result

print(extract_url_without_scheme("https://example.com/path"))   # example.com/path
print(extract_url_without_scheme("http://test.ru"))             # test.ru
print(extract_url_without_scheme("ftp://server.local/file"))    # server.local/file
print(extract_url_without_scheme("example.com/no-scheme"))



