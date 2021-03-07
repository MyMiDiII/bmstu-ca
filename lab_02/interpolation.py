"""
    Модуль, реализующий полиномиальную
    интерполяцию табличных функций
"""

import copy


EPS = 1e-7


def read_table(file_name):
    """
        Чтение табличной функции из файла
    """

    func_table = []

    with open(file_name, "r") as file:
        for i, rec in enumerate(file):
            func_table.append(list(map(float, rec.split())))

            if not i and abs(func_table[i][0]) > EPS:
                raise TypeError

            if i and len(func_table[i]) != len(func_table[i - 1]):
                raise TypeError

    if not func_table:
        raise EOFError

    return func_table


def print_table(table):
    """
        Вывод табличной функции
    """

    if table:
        print("Загруженная таблица:")
        print("{:>8s}".format("y\\x"), end="")
    else:
        print("Пустой файл!")

    for i, rec in enumerate(table):
        for j, value in enumerate(rec):
            if i or j:
                print("{:8.3f}".format(value),
                      end=("" if j + 1 < len(rec) else "\n"))


def print_list(res_list):
    """
        Вывод списка для таблицы
    """
    for i, z in enumerate(res_list):
        if i % 3 == 0:
            print("│{:6d}    │".format(i // 3 + 1), end=' ')

        print("{:9.3f}".format(z),
              end=(" " if (i + 1) % 3 else " │\n"))


def print_result(result):
    """
        Вывод таблицы значений функции двух переменных
    """

    print("\n┌──────────┬───────────────────────────────┐")
    print("│ n_x\\n_y  │       1         2         3   │")
    print("├──────────┼───────────────────────────────┤")
    print_list(result)
    print("└──────────────────────────────────────────┘")


def find_x_position(table, x_arg):
    """
        Поиск положения заданного аргумента x в таблице
    """
    prev_arg_index = 1
    num_table_args = len(table[0])

    while (prev_arg_index < num_table_args and
           x_arg > table[0][prev_arg_index]):
        prev_arg_index += 1

    return prev_arg_index - 1


def find_y_position(table, y_arg):
    """
        Поиск положения заданного аргумента y в таблице
    """
    prev_arg_index = 1
    num_table_args = len(table)

    while (prev_arg_index < num_table_args and
           y_arg > table[prev_arg_index][0]):
        prev_arg_index += 1

    return prev_arg_index - 1


def find_begin(max_len, position, coef_num):
    """
        Поиск индекса начала промежутка,
        в котором лежит аргумент
    """
    begin = position - coef_num // 2 + 1
    begin = begin if begin >= 1 else 1
    begin = begin if begin + coef_num < max_len else max_len - coef_num

    return begin


def create_calc_table(table, x_pos, y_pos, x_coef_num, y_coef_num):
    """
        Выбор значений для подсчета коэффициентов полиномов
    """
    res_table = [[0.] * (x_coef_num + 1) for i in range(y_coef_num + 1)]

    x_begin = find_begin(len(table[0]), x_pos, x_coef_num)
    y_begin = find_begin(len(table), y_pos, y_coef_num)

    for i in range(x_begin, x_begin + x_coef_num):
        res_table[0][i - x_begin + 1] = table[0][i]

    for j in range(y_begin, y_begin + y_coef_num):
        res_table[j - y_begin + 1][0] = table[j][0]

    for i in range(x_begin, x_begin + x_coef_num):
        for j in range(y_begin, y_begin + y_coef_num):
            res_table[j - y_begin + 1][i - x_begin + 1] = table[i][j]

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


def interpolate_by_x(table, arg):
    """
        Интерполяция по x
    """
    x_table = []

    for i in range(1, len(table[0])):
        x_table.append([table[0][i], 0.])

    result = []

    for i, y_row in enumerate(table):
        if i:
            for j, z in enumerate(y_row):
                if j:
                    x_table[j - 1][1] = z
            x_table_copy = copy.deepcopy(x_table)
            calc_coef(x_table_copy, 1)
            result.append(calc_func(x_table_copy, arg))

    return result


def interpolate_by_y(table, z_by_x, arg):
    """
        Интерполяция по y
    """
    y_table = []

    for i in range(1, len(table)):
        y_table.append([table[i][0], 0.])

    result = []

    for i, z in enumerate(z_by_x):
        y_table[i][1] = z

    calc_coef(y_table, 1)
    result = calc_func(y_table, arg)

    return result


def find_z(table, x, y, x_power, y_power):
    """
        Поиск значения табличной функции двух
        переменных при заданных значениях аргументов
    """
    x_position = find_x_position(table, x)
    y_position = find_y_position(table, y)
    calculaton_table = create_calc_table(table, x_position, y_position,
                                         x_power + 1, y_power + 1)
    x_interp_result = interpolate_by_x(calculaton_table, x)
    result = interpolate_by_y(calculaton_table, x_interp_result, y)

    return result
