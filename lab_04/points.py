"""
    Модуль для генерации табличной
    функции с весами узлов
"""
from numpy import random

def random_list(min, max, num):
    return [round(el[0], 2) for el in 
            random.uniform(min, max, size=(num, 1)).tolist()]

def generateTable(num, equal=[False, 0.]):
    table = []

    xlist = random_list(-100, 100, num) 
    ylist = random_list(-100, 100, num)

    if equal[0]:
        rolist = [equal[1]] * num
    else:
        rolist = random_list(0, 100, num)

    for i in range(num):
        rec = [xlist[i], ylist[i], rolist[i]]
        table.append(rec)

    return table
