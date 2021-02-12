"""
    Модуль для работы с табличными функциями
"""


def print_table(table):
    """
        Вывод табличной функции
    """

    print("      x        y         y'")
    for rec in table:
        print("    {:.2f}  {:9.6f}  {:.5f}".format(rec[0], rec[1], rec[2]))


def read_table(file_name):
    """
        Чтение табличной функции из файла
    """
    func_table = []

    with open(file_name, "r") as file:
        for str in file:
            func_table.append(list(map(float, str.split())))

    return func_table


