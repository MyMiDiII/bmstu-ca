"""
    Модуль для запуска программы
    ЛАБОРАТОРНАЯ РАБОТА №3
    ПОСТРОЕНИЕ И ПРОГРАММНАЯ РЕАЛИЗАЦИЯ АЛГОРИТМА
    СПЛАЙН-ИНТЕРПОЛЯЦИИ ТАБЛИЧНЫХ ФУНКЦИЙ
"""

import argparse

import table_func, newton, spline


def create_args():
    """
        Добавление аргументов командной строки
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', nargs='?', default='data/data.csv')
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    ARGS = create_args()

    try:
        func_table = table_func.read_table(ARGS.file_name)

        func_table.sort(key=lambda table: table[0])
        table_func.print_table(func_table)

        x = float(input("\nВведите значения аргумента для интерполяции: "))

    except FileNotFoundError:
        print("\nТакого файла не существует!")

    except ValueError:
        print("\nНечисловые данные недопустимы!")
        print("\nПроверьте содержимое файла или введенный аргумент!")

    except EOFError:
        print("\nПустой файл!")

    except TypeError:
        print("\nВ файле должно быть три столбца с данными!")

    else:
        print("Результат сплайн-интерполяции:")
        print(spline.count_spline(func_table, x))

        print("Результат инерполяции полиномом Ньютона 3-ей степени:")
        print(newton.find_newton_y(func_table, x, 3))
