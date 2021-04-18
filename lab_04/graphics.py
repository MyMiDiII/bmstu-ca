"""
    Модуль получения данных для графиков
"""
import rms

def getPointsFunc(polinomial, span):
    """
        Получение точек для построения графика
    """
    step = (span[1] - span[0]) / 1000

    if abs(step) < rms.EPS:
        step = 10

    xData = []
    yData = []

    xCur = span[0] - step

    while xCur < span[1] + step:
        yCur = 0

        for i, coef in enumerate(polinomial):
            yCur += coef * pow(xCur, i)

        xData.append(xCur)
        yData.append(yCur)

        xCur += step

    return xData, yData


def getXs(table):
    """ Получение списка координат x """
    return [rec[0] for rec in table]


def getYs(table):
    """ Получение списка координат y """
    return [rec[1] for rec in table]


def findMaximumX(table):
    """ Получение максимума из координат x """
    return max(getXs(table))


def findMinimumX(table):
    """ Получение минимума из координат x """
    return min(getXs(table))


def getPlot(table, degree):
    """
        Получение списка точек по
        исходной таблице и степени полинома
    """
    slae = rms.getEquationSystem(table, degree)
    polinomial = rms.solveSLAE(slae)
    minX = findMinimumX(table)
    maxX = findMaximumX(table)
    pointsFunc = getPointsFunc(polinomial, [minX, maxX])

    return pointsFunc
