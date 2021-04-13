"""
    Модуль интерполяции полиномом Ньютона
"""


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


def create_calc_table(table, arg_position, coef_num):
    """
        Выбор значений для подсчета коэффициентов полинома
    """

    res_table = []

    begin = arg_position - coef_num // 2 + 1
    begin = begin if begin >= 0 else 0
    begin = begin if begin + coef_num < len(table) else len(table) - coef_num

    for i in range(begin, begin + coef_num):
        res_table.append([x for x in table[i]])

    return res_table


def calc_divided_difference(y0, y1, x0, x1):
    """
        Подсчет разделенной разности
    """

    return (y0 - y1) / (x0 - x1)


def calc_coef(calc_table, first_col):
    """
        Подсчет коэффициентов полинома
        с помощью разделенных разностей
    """

    for y in range(first_col, len(calc_table)):
        for i in range(0, len(calc_table) - y):
            calc_table[i].append(calc_divided_difference(
                calc_table[i][y],
                calc_table[i + 1][y],
                calc_table[i][0], calc_table[i + y][0]))


def calc_func(calc_table, arg):
    """
        Подсчет значения функции с помощью таблицы разделенных разностей
    """

    result = 0
    mul = 1

    for i in range(1, len(calc_table[0])):
        result += calc_table[0][i] * mul
        mul *= arg - calc_table[i - 1][0]

    return result


def find_newton_y(table, arg, power):
    """
        Поиск значения отсортированной по аргументу табличной
        функции с помощью интерполяции полиномом Ньютона
    """

    arg_position = find_x_position(table, arg)
    calculaton_table = create_calc_table(table, arg_position, power + 1)
    calc_coef(calculaton_table, 1)
    result = calc_func(calculaton_table, arg)

    return result
