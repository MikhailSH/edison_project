def foo(a, b):
    try:
        return a/b
    except:
        print(f"произошла ошибка a = {a}, b = {b}")
print(foo(1, 0))