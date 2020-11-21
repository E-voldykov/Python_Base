"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
"""
answer_dict = {}
with open("base_les5_6.txt","r",encoding="utf-8") as file:
    for line in file:
        discipline, point_sum, point = line.split(":")[0], 0, ""
        for item in line:
            if item.isdigit():
                point += item
                print(point)
            else:
                if point.isdigit():
                    point_sum += int(point)
                    point = ""
            answer_dict[discipline] = point_sum
print (f'Выводим словарь на экран:\n{answer_dict}')


