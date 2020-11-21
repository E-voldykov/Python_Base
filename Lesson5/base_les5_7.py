"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Итоговый список сохранить в виде json-объекта в соответствующий файл."""
# Из условия непонятно, с каким знаком ставить убыток, ставил со знаком "-"!
import random, json

answer_list = [{}, {}]
form = ["OOO", "ЗAO", "OAO", "ГК"]
firm_count = input(f'Введите количество фирм, а мы сгенерируем список в файле:\n')
with open("firm_list.txt", "w+", encoding="utf-8") as file:
    for item in range(int(firm_count)):
        firm_list = [f'firm_{item + 1}', random.choice(form), random.randint(5000, 30000), random.randint(1000, 25000)]
        file.write(f'{" ".join([str(i) for i in firm_list])}\n')
    file.seek(0)
    mean_sum, mean_count = 0, 0
    for item in file:
        firm = item.split()
        profit = int(firm[2]) - int(firm[3])
        answer_list[0][firm[0]] = profit
        if profit > 0:
            mean_count += 1
            mean_sum += profit
    answer_list[1]["average_profit"] = round(mean_sum / mean_count)

with open("answer7.json", "w") as js_file:
    json.dump(answer_list, js_file)
