"""
    Модуль для запуска программы
    ЛАБОРАТОРНАЯ РАБОТА №5
    ПОСТРОЕНИЕ И ПРОГРАММНАЯ РЕАЛИЗАЦИЯ
    АЛГОРИТМОВ ЧИСЛЕННОГО ИНТЕГРИРОВАНИЯ
"""

from math import sin, cos, exp, pi

import integration
import graphics

subFunc = (lambda teta, phi :
           2 * cos(teta) / (1 - sin(teta) ** 2 * cos(phi) ** 2))
fullFunc = (lambda tau, teta, phi :
            4 / pi * (1 - exp(-tau * subFunc(teta, phi)))
            * cos(teta) * sin(teta))


if __name__ == "__main__":

    try:
        N = int(input("Введите количество узлов по x: "))
        M = int(input("Введите количество узлов по y: "))
        tau = float(input("Введите параметр τ: "))

        if N < 1 or M < 1:
            raise TypeError

    except ValueError:
        print("\nНечисловые данные недопустимы!")

    except TypeError:
        print("\nКоличество узлов -- натуральное число!")

    else:
        tetaRange = [0, pi / 2]
        phiRange = [0, pi / 2]
        tauFunc = integration.getTauFunc(fullFunc, (tetaRange, N), (phiRange, M))
        print("Вычисленное значение интеграла:", tauFunc(tau))

        graphics.getGraph(tauFunc, [0.05, 10])