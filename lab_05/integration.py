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


def toTetaFunc(func, tau, phi):
    """
        Получение функции для интегрирования по teta
    """
    return lambda teta : func(tau, phi, teta)


def toPhiFunc(func, tau):
    """
        Получение функции для интегрирования по tau
    """
    return lambda phi : func(tau, phi)


def getTauFunc(treeArgsFunc, tetaConf, phiConf):
    """
        Последовательное интегрирование
    """
    twoArgsFunc = (
        lambda tau, phi :
        gauss(
            toTetaFunc(treeArgsFunc, tau, phi),
            tetaConf[0][0],
            tetaConf[0][1],
            tetaConf[1]
        )
    )

    oneArgFunc = (
        lambda tau :
        simpson(
            toPhiFunc(twoArgsFunc, tau),
            phiConf[0][0],
            phiConf[0][1],
            phiConf[1]
        )
    )

    return oneArgFunc