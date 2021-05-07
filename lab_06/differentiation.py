"""
    Модуль численного дифференцирования
"""

def getLeftHandDer(cur, prev):
    """
        Первая левосторонняя разностная производная
    """

    return (cur[1] - prev[1]) / (cur[0] - prev[0])


def getCentralDer(prevP, nextP):
    """
        Первая центральная разностная
        производная в каждой точке
    """
    return (nextP[1] - prevP[1]) / (nextP[0] - prevP[0])


def getRungeDer(prev2P, prevP, curP):
    """
        2-ая формула Рунге с использованием
        односторонней производной
    """
    step1Der = getLeftHandDer(curP, prevP)
    step2Der = getLeftHandDer(curP, prev2P)

    return 2 * step1Der - step2Der

def getAlignVarDer(cur, nextP):
    """
        Первая производная при
        введенных выравнивающих переменных
    """
    alignVarCoef = (1 / nextP[1] - 1 / cur[1]) / (1 / nextP[0] - 1 / cur[0])
    return cur[1] * cur[1] / cur[0] / cur[0] * alignVarCoef


def getSecondDer(prevP, curP, nextP):
    """
        Вторая разностная производная
    """
    return ((prevP[1] - 2 * curP[1] + nextP[1])
            / (nextP[0] - curP[0])
            / (curP[0] - prevP[0]))
