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


def delete_derivative(table):
    """
        Удаление слобца производных
    """
    for rec in table:
        rec.pop()


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
        print("y =", y)
        for i in range(0, len(calc_table) - y):
            print("i = ", i)
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


def newton_find_y(table, arg, power):
    """
        Поиск значения отсортированной по аргументу табличной
        функции с помощью интерполяции полиномом Ньютона
    """

    arg_position = find_x_position(table, arg)
    calculaton_table = create_calc_table(table, arg_position, power + 1)
    delete_derivative(calculaton_table)
    calc_coef(calculaton_table, 1)
    result = calc_func(calculaton_table, arg)

    return result


def add_node(table, power):
    """
        Добавление повторных узлов
    """

    i = 0
    count_node = len(table)
    while count_node < power + 1:
        new_diff = ([] if i == count_node
                       else [calc_divided_difference(
                                table[i][1], table[i + 1][1],
                                table[i][0], table[i + 1][1])])
        new_rec = table[i][:2] + new_diff
        table = table[:i + 1] + [new_rec] + table[i + 1:]
        count_node += 1
        i += 2

    return table


def hermit_find_y(table, arg, power):
    """
        Поиск значения отсортированной по аргументу табличной
        функции с помощью интерполяции полиномом Эрмита
    """
    print("new pow")
    arg_position = find_x_position(table, arg)
    calculaton_table = create_calc_table(table, arg_position, power // 2 + 1)
    calculaton_table = add_node(calculaton_table, power)
    print(calculaton_table)
    calc_coef(calculaton_table, 2)
    result = calc_func(calculaton_table, arg)

    return result
