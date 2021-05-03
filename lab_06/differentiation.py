"""
    Модуль численного дифференцирования
"""

def getLeftHandDerList(func):
    """
        Первая левосторонняя производная в каждой точке
    """
    result = [0]
    print(func)

    for i, point in enumerate(func):
        if i:
            der = ((point[1] - func[i - 1][1])
                   / (point[0] - func[i - 1][0]))
            result.append(der)

    return result
