"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
# Несколько переусложнил. но пусть будет так.
start = [7, 5, 3, 3, 2]
final = 'end'
print(f'Структура "Рейтинг"\n{"+" * 60}\nСтартовый список - {start}\n{"+" * 60}')
while True:
    new_item = input(f'Введите новое значение:\n')
    if new_item == final or new_item == final.istitle() or new_item == final.isupper():
        print(f'Завершаем программу!\nКонечный список - {start}')
        break
    if not new_item.isdigit():
        print(f'Ошибка! Введите число!')
        continue
        new_item = int(new_item)
    if new_item <= start[-1]:
        start.append(new_item)
        print(f'Измененный список - {start}')
        continue
    elif new_item > start[0]:
        start.insert(0, new_item)
        print(f'Измененный список - {start}')
        continue
    elif new_item in start:
        start.insert(start.index(new_item) + start.count(new_item), new_item)
        print(f'Измененный список - {start}')
    else:
        difference, index = start[0] - new_item, 0
        for item in range(len(start)):
            if (start[item] - new_item) < 0 and abs(start[item] - new_item) < difference:
                difference = start[item] - new_item
                index = item
        start.insert(index, new_item)
        print(f'Измененный список - {start}')
        continue
