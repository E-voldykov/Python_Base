"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
while True:
    var = input(f'Введите число:\n')
    if var.isdigit():
        var, max_digit = int(var), 0
        while var:
            if var % 10 > max_digit:
                max_digit = var % 10
            var = var // 10
        print(f'Наибольшая цифра: {max_digit}')
        break
    else:
        print(f'Ошибка! "{var}" не число!\nПопробуем еще раз.')
        continue
