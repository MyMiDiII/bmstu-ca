"""
    Модуль для запуска программы
    ЛАБОРАТОРНАЯ РАБОТА №6
    ПОСТРОЕНИЕ И ПРОГРАММНАЯ РЕАЛИЗАЦИЯ
    АЛГОРИТМОВ ЧИСЛЕННОГО ДИФФЕРЕНЦИРОВАНИЯ
"""

import argparse

import table_func
from differentiation import getLeftHandDer, getCentralDer
from differentiation import getRungeDer, getAlignVarDer
from differentiation import getSecondDer


def create_args():
    """
        Добавление аргументов командной строки
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', nargs='?', default='data/data.csv')
    args = parser.parse_args()

    return args


def getLeftHandString(i, func):
    """
        Получение строки для вывода
        левосторонней разностной производной
    """

    return ("{:7.3f}".format(getLeftHandDer(func[i], func[i - 1]))
            if i else "{:>7s}".format("--"))


def getCentralString(i, func):
    """
        Получение строки для вывода
        центральной разностной производной
    """

    return ("{:7.3f}".format(getCentralDer(func[i - 1], func[i + 1]))
            if i and i != len(func) - 1 else "{:>7s}".format("--"))


def getRungeString(i, func):
    """
        Получение строки для вывода
        разностной производной по формуле
        Рунге
    """

    return ("{:7.3f}".format(getRungeDer(func[i - 2], func[i - 1], func[i]))
            if i > 1 else "{:>7s}".format("--"))


def getAlignVarString(i, func):
    """
        Получение строки для вывода
        строки при введенных выравнивающих
        переменных
    """

    return ("{:7.3f}".format(getAlignVarDer(func[i], func[i + 1]))
            if i != len(func) - 1 else "{:>7s}".format("--"))


def getSecondDerString(i, func):
    """
        Получение строки для вывода
        второй разностной производной
    """

    return ("{:7.3f}".format(getSecondDer(func[i - 1], func[i], func[i + 1]))
            if i and i != len(func) - 1 else "{:>7s}".format("--"))


if __name__ == "__main__":
    ARGS = create_args()

    try:
        func_table = table_func.read_table(ARGS.file_name)

        func_table.sort(key=lambda table: table[0])
        table_func.print_table(func_table)

    except FileNotFoundError:
        print("\nТакого файла не существует!")

    except ValueError:
        print("\nНечисловые данные недопустимы!")
        print("\nПроверьте содержимое файла!")

    except EOFError:
        print("\nПустой файл!")

    except TypeError:
        print("\nВ файле должно быть два столбца с данными!")

    else:
        print("\nТаблица разностных производных")
        print("    1       2       3       4       5   ")
        for i in range(len(func_table)):
            print(getLeftHandString(i, func_table), end=" ")
            print(getCentralString(i, func_table), end=" ")
            print(getRungeString(i, func_table), end=" ")
            print(getAlignVarString(i, func_table), end=" ")
            print(getSecondDerString(i, func_table), end="\n")

        print()
        print("1 -- левая разностная производная;")
        print("2 -- центральная разностная производная;")
        print("3 -- 2-ая формула Рунге с использованием\n"
              + "     односторонней (левой) производной;")
        print("4 -- введены выравнивающие переменные;")
        print("5 -- вторая разностная производная.")
