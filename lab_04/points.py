"""
    Модуль для генерации табличной
    функции с весами узлов
"""
from numpy import random

def generateRandomList(left, right, num):
    """
        Генерация списка со случайными
        значениями в заданном диапазоне
        заданного размера
    """
    return [round(el[0], 2) for el in
            random.uniform(left, right, size=(num, 1)).tolist()]

def generateTable(num, equal=[False, 0.]):
    """
        Генерация таблицы точек заданного размера
    """
    table = []

    xlist = generateRandomList(-100, 100, num)
    ylist = generateRandomList(-100, 100, num)

    if equal[0]:
        rolist = [equal[1]] * num
    else:
        rolist = generateRandomList(0, 100, num)

    for i in range(num):
        rec = [xlist[i], ylist[i], rolist[i]]
        table.append(rec)

    return table
