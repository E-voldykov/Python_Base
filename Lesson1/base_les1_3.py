"""Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369"""

while True:
    var = input(f'Введите число:\n')
    if var.isdigit():
        print(f'Считаем {var} + {var * 2} + {var * 3}')
        print(f'Ответ: {int(var) + int(var * 2) + int(var * 3)}')
        break
    else:
        print(f'Ошибка! "{var}" не число!\nПопробуем еще раз.')
        continue
