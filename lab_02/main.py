"""
    Модуль для запуска программы
    ЛАБОРАТОРНАЯ РАБОТА №2
    ПОСТРОЕНИЕ И ПРОГРАММНАЯ РЕАЛИЗАЦИЯ АЛГОРИТМА ПОЛИНОМИАЛЬНОЙ
    ИНТЕРПОЛЯЦИИ ТАБЛИЧНЫХ ФУНКЦИЙ
"""

import argparse

import interpolation as interp


LOWER = 1
UPPER = 3

INPUT_MSG = "\nВведите значения аргументов (x, y) для интерполяции: "


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
        #func_table.sort(key=lambda table: table[0])
        interp.print_table(func_table)

        x, y = map(float, input(INPUT_MSG).split())

    except FileNotFoundError:
        print("\nТакого файла не существует!")

    except ValueError:
        print("\nНечисловые данные недопустимы!")
        print("Проверьте содержимое файла или введенный аргумент!")

    except EOFError:
        print("\nПустой файл!")

    except TypeError:
        print("\nНеверный формат файла!")

    else:
        result = []

        for n in range(LOWER, UPPER + 1):
            for m in range(LOWER, UPPER + 1):
                result.append(interp.find_z(func_table, x, y, n, m))

        interp.print_result(result)
