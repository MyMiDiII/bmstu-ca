"""
    Модуль отображения графиков
"""

import matplotlib.pyplot as plt


def getPointFunc(func, xRange):
    """
        Формирование списков точек функции
        в заданном диапазоне
    """
    step = (xRange[1] - xRange[0]) / 100

    xData = []
    yData = []

    xCur = xRange[0]

    while xCur < xRange[1] + step:
        xData.append(xCur)
        yData.append(func(xCur))
        xCur += step

    return xData, yData


def getGraph(func, xRange, N, M):
    """
        Добавление графика на изображение
    """

    xList, yList = getPointFunc(func, xRange)

    plt.plot(xList, yList, label="при N = {:d}, M = {:d}".format(N, M))


def show():
    """
        Отображение графиков
    """
    plt.gcf().canvas.set_window_title("Численное интегрирование")
    plt.legend()
    plt.title("ε(τ)")
    plt.show()
