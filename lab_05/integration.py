"""
    Модуль численного интегрирования
"""

from numpy.polynomial.legendre import leggauss

def simpson(func, left, right, num):
    """
        Интегрирование методом Симпсона
    """
    step = (right - left) / num

    result = 0

    x = left
    
    while x < right:
        xNext = x + step
        result += func(x) + 4 * func(x + step / 2)  + func(xNext)
        x = xNext

    return step / 6 * result


def toX(t, left, right):
    """
        Преобразование переменной
    """
    return (right + left) / 2 + (right - left) / 2 * t


def gauss(func, left, right, num):
    """
        Интегрирование методом Гаусса
    """
    nodes, coefs = leggauss(num)

    result = 0

    for i in range(num):
        result += coefs[i] * func(toX(nodes[i], left, right))

    return (right - left) / 2 * result


def getTauFunc(func, tetaConf, phiConf):
    """
        Получение функции, зависящей только от tau
    """
    return lambda tau : func(tau, 0.5, 0.5)