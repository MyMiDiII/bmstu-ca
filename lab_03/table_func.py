"""
    Модуль ввода-вывода табличных функций
"""


def read_table(file_name):
    """
        Чтение табличной функции из файла
    """

    func_table = []

    with open(file_name, "r") as file:
        for i, rec in enumerate(file):
            func_table.append(list(map(float, rec.split())))

            if len(func_table[i]) != 2:
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
        print("      x        y")
    else:
        print("Пустой файл!")

    for rec in table:
        print("    {:.2f}  {:9.2f}".format(rec[0], rec[1]))

