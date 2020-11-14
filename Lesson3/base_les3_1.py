"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


# Не понял, стоит ли оборачивать в функцию операции ручного ввода и вывода через print.

def division(dividend: int, divisor: int) -> int:
    if divisor == 0:
        return False
    else:
        return round(dividend / divisor, 2)


if __name__ == "__main__":

    digits = input(f'{"+" * 50}\nДля деления введите 2 числа через пробел: '
                   f'сначала делимое, затем делитель\n{"+" * 50}\nВведите числа:\n').split()

    quotient = division(int(digits[0]), int(digits[1]))

    if not quotient:
        print(f'Деление на ноль в данной программе запрещено!')
    else:
        print(f'Ответ:\n{quotient}')
