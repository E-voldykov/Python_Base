"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict."""

seasons  = ["зима", "весна", "лето", "осень"]
months, seasons_list = [], tuple(seasons)
for i in range(12):
    months.append(i + 1)


# Ввод месяца.
print("*" * 50)
while True:
    months_number = input(f'Введите номер месяца!\n')
    if months_number.isdigit() and int(months_number) in months:
        break
    else:
        print(f'Ошибка! Повторите Ввод!')
        continue
months_number = int(months_number)

# Кусок как сделать словарь используя только то, что изучали.
months_dict, count = {}, 0

for n in range(3, 12):
    count += 1
    months_dict[n] = seasons[1]
    if count == 3:
        del seasons[1]
        count = 0
    months[n - 1] = 0

for item in months:
    if item != 0:
        months_dict[item] = seasons[0]

# Выбор способа решения и само решение.
print("*" * 50)
while True:
    choose = input(f'Введите list или dict для того чтобы решить через словарь или список соответсвенно:\n')
    if choose == "dict":
        print(f'{months_number}-й месяц это {months_dict[months_number]}')
        break
    elif choose == 'list':
        if months_number in [1, 2, 12]:
            print(f'{months_number}-й месяц это {seasons_list[0]}!')
        if months_number in [3, 4, 5]:
            print(f'{months_number}-й месяц это {seasons_list[1]}!')
        if months_number in [6, 7, 8]:
            print(f'{months_number}-й месяц это {seasons_list[2]}!')
        if months_number in [9, 10, 11]:
            print(f'{months_number}-й месяц это {seasons_list[3]}!')
        break
    else:
        print(f'Ошибка! Повторите Ввод! ')
        continue
print("*" * 50)
