"""
    Модуль для работы с табличными функциями
"""

EPS = 1e-6

def read_table(file_name):
    """
        Чтение табличной функции из файла
    """
    func_table = []

    with open(file_name, "r") as file:
        for rec in file:
            func_table.append(list(map(float, rec.split())))

    if not func_table:
        raise EOFError

    return func_table


def print_table(table):
    """
        Вывод табличной функции
    """

    if table:
        print("Загруженная таблица:")
        print("      x        y         y'")
    else:
        print("Пустой файл!")

    for rec in table:
        print("    {:.2f}  {:9.6f}  {:.5f}".format(rec[0], rec[1], rec[2]))


def find_x_position(table, arg):
    """
        Поиск положения заданного аргумента в таблице
    """
    prev_arg_index = 0
    num_table_args = len(table)

    while (prev_arg_index < num_table_args and
           arg > table[prev_arg_index][0]):
        prev_arg_index += 1

    return prev_arg_index - 1


def newton_find_y(table, arg, degree):
    """
        Поиск значения отсортированной по аргументу табличной
        функции с помощью интерполяции полиномом Ньютона
    """
    pass
