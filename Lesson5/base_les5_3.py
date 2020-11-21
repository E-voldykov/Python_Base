"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

print(f'В эфире программа "Самый Бедный". Найдем самых бедных из списка:')

poor_dict, mean_sum, mean_count = {}, 0, 1
with open('base_les5_3.txt', 'r', encoding='utf-8') as file:
    for line in file:
        worker = [item for item in line.split() if item.strip('р.''р''руб.''руб').istitle()
                  or item.strip('р.''р''руб.''руб').isdigit()]
        if len(worker) == 2 and worker[1].isdigit():
            mean_count += 1
            mean_sum += int(worker[1])
            if int(worker[1]) < 20000:
                poor_dict[worker[0]] = int(worker[1])

for i in poor_dict:
    print(f'{i} - {poor_dict[i]}')

print(f'Средняя ЗП: {(mean_sum / mean_count):.0f} руб.')
