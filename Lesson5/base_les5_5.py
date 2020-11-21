""""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
"""

filename = input(f'Введите название файла для записи:\n')

with open(f'{filename}.txt', 'w', encoding='utf-8') as file:
    while True:
        line = input(f'Введите набор чисел, разделяя их пробелами:\n')
        if len([item for item in line.split() if not item.isdigit()]):
            print(f'Вводить можно только цифры, попробуйте заново!')
            continue
        else:
            print(f'Сумма чисел - {sum(list(map(int, line.split())))}')
            break
