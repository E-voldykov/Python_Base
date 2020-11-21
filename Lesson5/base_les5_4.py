"""Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

rus_digits = {1: "Один", 2: 'Два', 3: 'Три', 4: 'Четыре'}

with open("base_les5_4.txt", 'r', encoding="utf-8") as file:
    for line in file:
        rus_line = line.split()
        rus_line[0] = rus_digits[int(line.split()[-1])]
        rus = open("les4_answer.txt", 'a', encoding="utf-8")
        rus.write(f'{" ".join(rus_line)}\n')
        rus.close()
