"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
change_list = input(f'Введите набор данных, отделив каждый элемент пробелом!\n').split()

print("-" * 50)

print(f'Введеный набор данных - {change_list}\n')

for item in range(0, len(change_list)-1, 2):
    if item != len(change_list):
        change_list[item], change_list[item + 1] = change_list[item + 1], change_list[item]

print(f'Измененный набор данных - {change_list}')

print("-"*50)