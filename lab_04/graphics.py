import matplotlib.pyplot as plt

def getEquationSystem(table, degree):
    slae = [[0] * (degree + 2) for i in range(degree + 1)]

    for i in range(degree + 1):
        for j in range(degree + 1):
            curA = 0
            for k in range(len(table)):
                curA += table[k][2] * pow(table[k][0], i) * pow(table[k][0], j)
            slae[i][j] = curA

        curB = 0
        for k in range(len(table)):
            curB += table[k][2] * table[k][1] * pow(table[k][0], i)
        slae[i][degree + 1] = curB

    return slae


def solveSLAE(slae):
    length = len(slae)
    for j in range(length):
        for i in range(j + 1, length):
            curCoef = slae[i][j] / slae[j][j]

            for k in range(j, length + 1):
                slae[i][k] -= curCoef * slae[j][k]

    answer = [0. for i in range(length)]

    for i in range(length - 1, -1, -1):
        for j in range(length - 1, i, -1):
            slae[i][length] -= slae[i][j] * answer[j]

        answer[i] = slae[i][length] / slae[i][i]

    return answer


def getPointsFunc(polinomial, span):
    step = (span[1] - span[0]) / 1000

    xData = []
    yData = []

    xCur = span[0] - step

    while (xCur < span[1] + step):
        yCur = 0

        for i, coef in enumerate(polinomial):
            yCur += coef * pow(xCur, i)

        xData.append(xCur)
        yData.append(yCur)

        xCur += step

    return xData, yData


def getXs(table):
    return [rec[0] for rec in table]


def getYs(table):
    return [rec[1] for rec in table]


def findMaximumX(table):
    return max(getXs(table))


def findMinimumX(table):
    return min(getXs(table))


def getPlot(table, degree):
    slae = getEquationSystem(table, degree)
    polinomial = solveSLAE(slae)
    minX = findMinimumX(table)
    maxX = findMaximumX(table)
    pointsFunc = getPointsFunc(polinomial, [minX, maxX])

    return pointsFunc
