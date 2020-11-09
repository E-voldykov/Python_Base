"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


# Решение №1
def pow_1(a: int, n: int) -> float:
    return a ** n


# Решение №2
def pow_2(a: int, n: int) -> float:
    answer = 1
    for i in range(abs(n)):
        answer *= a
    if n > 0:
        return answer
    elif n < 0:
        return 1 / answer
    else:
        return 1


# Решение №3
def pow_3(a: int, n: int) -> float:
    if n == 0:
        return 1
    elif n < 0:
        return 1 / a * pow_3(a, n + 1)
    else:
        return a * pow_3(a, n - 1)


if __name__ == "__main__":
    print(pow_1(2, -5))
    print(pow_2(2, -5))
    print(pow_3(2, -5))
