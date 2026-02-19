#получаем Коэфициенты
first_coefficient= int(input('a = ', ))
second_coefficient = int(input('b = ', ))
third_coefficient = int(input('c = ', ))

# решение по сокращенной формуле, т.к. b - четное
if first_coefficient != 0 and second_coefficient % 2 == 0 and third_coefficient!= 0:
    k = second_coefficient / 2
    d1 = k ** 2 - first_coefficient * third_coefficient
    root_1  = (-k + d1 ** 0.5) / first_coefficient
    root_2 = (-k - d1 ** 0.5) / first_coefficient
    print('так как коэффициент b - четное число, решаем по сокращенной формуле')
    print(f'первый корень = {root_1}')
    print(f'второй корень = {root_2}')

# решение полного уравнения
if first_coefficient != 0 and second_coefficient % 2 != 0 and third_coefficient != 0:
    d = second_coefficient ** 2 - 4 * first_coefficient * third_coefficient

    if d > 0:
        k1 = (-second_coefficient + d ** 0.5) / (2 * first_coefficient)
        print(f'дискриминант равен: {d}')
        print(f'первый корень равен: {round(k1, 2)}')
        k2 = (-second_coefficient - d ** 0.5) / (2 * first_coefficient)
        print(f'второй корень равен: {round(k2, 2)}')

    elif d < 0:
        print(f'так как дискриминант меньше нуля и равен: {d}')
        print('действительных корней нет')

    else:
        k = -second_coefficient / (2 * first_coefficient)
        print(f'уравнение имеет один корень: {k}')

        # решение уравнения при b = 0
        if first_coefficient != 0 and third_coefficient != 0 and second_coefficient == 0:
            if (-third_coefficient / first_coefficient) >= 0:
                k1 = ( -third_coefficient / first_coefficient ) ** 0.5
                print(f'первый корень равен: {k1}')
                k2 = (-1) * ((-third_coefficient / first_coefficient) ** 0.5)
                print(f'второй корень равен: {k2}')

        if ( -third_coefficient / first_coefficient ) < 0:
            print(f' -c / peremennaya1 = : {-third_coefficient / first_coefficient}, т.е. < 0, поэтому действительных корней нет')

# решение уравнения при с = 0
if first_coefficient != 0 and third_coefficient== 0 and second_coefficient != 0:
    print(f'корень уравнения равен либо нулю, либо {-second_coefficient / first_coefficient}')

# решение уравнения при b = 0 и c = 0
if first_coefficient != 0 and second_coefficient== 0 and third_coefficient == 0:
    print(f'корни уравнения равны нулю, first_coefficient * x ** 2 = 0')
