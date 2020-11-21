"""Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""


def def_count(start=1, stop=100):
    from itertools import count
    for i in count(start):
        print(i, end=" ")
        if i == stop:
            break


def def_cycle(in_list: list, end_count=10):
    from itertools import cycle
    count = 1
    for i in cycle(in_list):
        count += 1
        print(i, end=" ")
        if count == end_count:
            break


if __name__ == "__main__":
    from sys import argv

    try:
        if len(argv) != 4:
            print("Укажие верное число аргументов!")
        elif argv[1] == "count":
            def_count(int(argv[2]), int(argv[3]))
        elif argv[1] == "cycle":
            def_cycle(list(map(lambda x: int(x), list(argv[2]))), int(argv[3]))
        else:
            print(f'Введите правильные параметры!')
    except IndexError:
        print(f'Введите верне число аргументов!')
    except ValueError:
        print(f'Введите правильные значения аргументов!')
