"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def person_info(**values) -> None:
    for info_name, info_value in values.items():
        print(f'{info_name} - {info_value}', end="|")


if __name__ == "__main__":
    person_info(name="Lenya", surname="Golubkov", current_status="Partner", phone=88005553535)
