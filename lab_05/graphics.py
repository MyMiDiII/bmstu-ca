"""
    Модуль отображения графиков
"""

import matplotlib.pyplot as plt

def getPointFunc(func, xRange):
    """
        Формирование списков точек функции
        в заданном диапазоне
    """
    step = (xRange[1] - xRange[0]) / 1000

    xData = []
    yData = []

    xCur = xRange[0]

    while xCur < xRange[1] + step:
        xData.append(xCur)
        yData.append(func(xCur))
        xCur += step

    return xData, yData

def getGraph(func, xRange):
    """
        Отображение графика
    """

    xList, yList = getPointFunc(func, xRange)

    plt.plot(xList, yList, label="ε(τ)")
    plt.legend()
    plt.show()

