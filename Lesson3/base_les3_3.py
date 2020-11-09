"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


# Решение через 3 позиционных агрумента.
def biggest_sum(arg_1: int, arg_2: int, arg_3: int) -> int:
    answer = sorted([arg_1, arg_2, arg_3])
    return answer[-1] + answer[-2]


# Решение через любое количество аргументов.
def biggest_sum_args(*args) -> int:
    answer = sorted(list(map(int, *args)))
    return answer[-1] + answer[-2]


if __name__ == "__main__":
    trio = input(f'Найдем сумму 2х наибольших чисел из трех.\nВведите 3 числа через пробел:\n').split()
    print(biggest_sum(int(trio[0]), int(trio[1]), int(trio[2])))

    infinite = input(f'Найдем сумму 2х наибольших чисел из введеных.\nВведите числа через пробел:\n').split()
    print(biggest_sum_args(infinite))
