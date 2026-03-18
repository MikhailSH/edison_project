##args, kwargs
def foo(*args, **kwargs):
    print(args)
    print(kwargs)
foo(5, 3, 4, 2, 'начало', n = 1, m = 2, c = 3, d = 4, f = 'конец')
"""args массив позиционных аргументов
    kwargs словарь именованных аргументов"""
