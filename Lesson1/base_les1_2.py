"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
print(f'Переведем секунды в удобный формат')
while True:
    number = input(f'Введите число секунд:\n')
    if number.isdigit():
        number = int(number)
        days = number // 86400
        hours = (number - days * 86400) // 3600
        minutes = (number - days * 86400 - hours*3600) // 60
        seconds = (number - days * 86400 - hours*3600) % 60
        if hours < 10: hours = '0' + str(hours)
        if minutes < 10: minutes = '0' + str(minutes)
        if seconds < 10: seconds = '0' + str(seconds)
        if days % 10 == 1:
            print(f'Ответ: {days} день {hours}:{minutes}:{seconds}')
        elif 1 < days % 10 < 5:
            print(f'Ответ: {days} дня {hours}:{minutes}:{seconds}')
        else:
            print(f'Ответ: {days} дней {hours}:{minutes}:{seconds}')
        break
    else:
        print(f'Ошибка!\nНачнем заново!')
        continue
