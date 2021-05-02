"""
    Модуль для запуска программы
    ЛАБОРАТОРНАЯ РАБОТА №5
    ПОСТРОЕНИЕ И ПРОГРАММНАЯ РЕАЛИЗАЦИЯ
    АЛГОРИТМОВ ЧИСЛЕННОГО ИНТЕГРИРОВАНИЯ
"""

import integration
import graphics

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
        tauFunc = integration.getTauFunc(N, M)
        print("Вычисленное значение интеграла:", tauFunc(tau))

        graphics.getGraph(tauFunc, [0.05, 10])