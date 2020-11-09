"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


# Реализуем без встроенного метода str.title().
def title_func(text: str) -> str:
    return text.replace(text[0], chr(ord(text[0]) - 32), 1)


# Создадим случайный текст. Знаю, import не проходили, но текст каждый раз писать неудобно.
def random_text(length: int) -> str:
    import random
    text = ""
    for i in range(length):
        text += chr(random.randint(ord('a'), ord('z')))
    return text.replace(text[random.randint(0, len(text))], " ")


# Решим поставленную задачу. Здесь проще преобразовать через map, но используем старый добрый цикл.
if __name__ == "__main__":
    words_set = random_text(int(input(f'Введите количество символов в тексте!\n')))
    print(f'Полученный текст:\n{"+" * 50}\n{words_set}\n{"+" * 50}')
    words_set = words_set.split()
    for item in range(len(words_set)):
        words_set[item] = title_func(words_set[item])
    words_set = " ".join(words_set)
    print(f'Измененный текст:\n{words_set}\n{"+" * 50}')
