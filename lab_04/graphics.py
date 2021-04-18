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


    print(slae)

    return slae



def getPlot(table, degree):
    slae = getEquationSystem(table, degree)

    return ([1, 2, 3, 4, 5], [degree] * 5)
