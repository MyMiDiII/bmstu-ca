"""
    Модуль среднеквадратичного приближения
"""
EPS = 1e-6

def getEquationSystem(table, degree):
    """
        Поиск коэффициентов СЛАУ для
        метода наименьших квадратов
    """
    slae = [[0] * (degree + 2) for i in range(degree + 1)]

    for i in range(degree + 1):
        for j in range(degree + 1):
            curA = 0
            for row in table:
                curA += row[2] * pow(row[0], i) * pow(row[0], j)
            slae[i][j] = curA

        curB = 0
        for row in table:
            curB += row[2] * row[1] * pow(row[0], i)
        slae[i][degree + 1] = curB

    return slae


def solveSLAE(slae):
    """
        Решение СЛАУ
    """
    length = len(slae)
    for j in range(length):
        for i in range(j + 1, length):
            if abs(slae[j][j]) < EPS:
                continue

            curCoef = slae[i][j] / slae[j][j]

            for k in range(j, length + 1):
                slae[i][k] -= curCoef * slae[j][k]

    answer = [0. for i in range(length)]

    for i in range(length - 1, -1, -1):
        for j in range(length - 1, i, -1):
            slae[i][length] -= slae[i][j] * answer[j]

        if abs(slae[i][i]) < EPS:
            answer[i] = slae[i][length]
            continue

        answer[i] = slae[i][length] / slae[i][i]

    return answer
