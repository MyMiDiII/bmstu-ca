"""
    Модуль для запуска программы
    ЛАБОРАТОРНАЯ РАБОТА №1
    ПОСТРОЕНИЕ И ПРОГРАММНАЯ РЕАЛИЗАЦИЯ АЛГОРИТМА ПОЛИНОМИАЛЬНОЙ
    ИНТЕРПОЛЯЦИИ ТАБЛИЧНЫХ ФУНКЦИЙ
"""

# -> подсчет полинома Эрмита
# -> обратная интерполяция
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

        func_table.sort(key=lambda table: table[0])
        interp.print_table(func_table)

        x = float(input("Введите значения аргумента для интерполяции: "))

    except FileNotFoundError:
        print("Такого файла не существует!")

    except ValueError:
        print("Файл не должен содержать нечисловой информации!")

    except EOFError:
        print("Пустой файл!")

    except TypeError:
        print("Значение аргумента должно быть вещественным числом!")

    else:
        newton = []
        hermit = []
        for n in range(LOWER, UPPER + 1):
            newton.append(interp.newton_find_y(func_table, x, n))
            hermit.append(interp.hermit_find_y(func_table, x, n))

        print(newton)
        print(hermit)
        #interp.print_result(newton, hermit)

        #print(interp.newton_find_root(func_table))
