"""
    Модуль для запуска программы
    ЛАБОРАТОРНАЯ РАБОТА №1
    ПОСТРОЕНИЕ И ПРОГРАММНАЯ РЕАЛИЗАЦИЯ АЛГОРИТМА ПОЛИНОМИАЛЬНОЙ
    ИНТЕРПОЛЯЦИИ ТАБЛИЧНЫХ ФУНКЦИЙ
"""

# ?  необходимо ли запрашивать степень полинома
# -> ввод аргумента 
# -> подсчет полинома Ньютона
# -> подсчет полинома Эрмита
# -> отчет

import argparse

import interpolation.interpolation as interp


LOWER = 1
UPPER = 4

def create_args():
    """
        Добавление аргументов командной строки
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', nargs='?', default='data/data_01.txt')
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    ARGS = create_args()

    try:
        func_table = interp.read_table(ARGS.file_name)

    except FileNotFoundError:
        print("Такого файла не существует!")

    except ValueError:
        print("Файл не должен содержать нечисловой информации!")

    else:
        if not func_table:
            print("Пустой файл!")
        else:
            func_table.sort(key=lambda table: table[0])
            print("Загруженная таблица:")
            interp.print_table(func_table)

            newton = []
            hermit = []
            for n in range(LOWER, UPPER + 1):
                newton.append()
                hermit.append()
