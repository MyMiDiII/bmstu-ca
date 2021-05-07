"""
    Модуль для запуска программы
    ЛАБОРАТОРНАЯ РАБОТА №5
    ПОСТРОЕНИЕ И ПРОГРАММНАЯ РЕАЛИЗАЦИЯ
    АЛГОРИТМОВ ЧИСЛЕННОГО ИНТЕГРИРОВАНИЯ
"""

from math import sin, cos, exp, pi
import matplotlib.pyplot as plt

import integration
import graphics

subFunc = (lambda phi, teta :
           2 * cos(teta) / (1 - sin(teta) ** 2 * cos(phi) ** 2))
fullFunc = (lambda tau, phi, teta :
            4 / pi * (1 - exp(-tau * subFunc(phi, teta)))
            * cos(teta) * sin(teta))


if __name__ == "__main__":
    notEnd = True

    while notEnd:
        try:
            N = int(input("Введите количество узлов по θ: "))
            if N < 1:
                raise TypeError

            M = int(input("Введите количество узлов по φ: "))
            if M < 1:
                raise TypeError

            tau = float(input("Введите параметр τ: "))

        except ValueError:
            print("\nНечисловые данные недопустимы!")

        except TypeError:
            print("\nКоличество узлов -- натуральное число!")

        else:
            tetaRange = [0, pi / 2]
            phiRange = [0, pi / 2]
            tauFunc = integration.getTauFunc(fullFunc, (tetaRange, N), (phiRange, M))
            print("Вычисленное значение интеграла:", "{:6.3f}".format(tauFunc(tau)))

            graphics.getGraph(tauFunc, [0.05, 10], N, M)

            notEnd = input("\nДля выхода нажмите Enter"
                           + "\nДля продолжения введите что-либо\n")

    graphics.show()