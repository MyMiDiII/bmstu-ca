"""
    Модуль сплайн-интерполяции табличных функций
"""

def find_h_coefs(func):
    """
        Поиск коэффициентов h
    """
    h_coefs = []

    for i in range(1, len(func)):
        h_coefs.append(func[i][0] - func[i - 1][0])

    return h_coefs


def find_f_coefs(func, h):
    """
        Поиск коэффициентов f
    """
    f_coefs = [0.]

    for i in range(2, len(func)):
        dy1 = func[i][1] - func[i - 1][1]
        dy2 = func[i - 1][1] - func[i - 2][1]
        f_coefs.append(3 * (dy1 / h[i - 1] - dy2 / h[i - 2]))

    return f_coefs


def find_ksi_coefs(func, h):
    """
        Поиск коэффициентов ξ
    """
    ksi_coefs = [0., 0.]

    for i in range(2, len(func)):
        cur_ksi = - h[i - 1] / (h[i - 2] * ksi_coefs[i - 1] + 2 * (h[i - 2] + h[i - 1]))
        ksi_coefs.append(cur_ksi)

    return ksi_coefs


def find_eta_coefs(func, ksi, h, f):
    """
        Поиск коэффициентов η
    """
    eta_coefs = [0., 0.]

    for i in range(2, len(func)):
        cur_eta = (f[i - 1] - h[i - 2] * eta_coefs[i - 1]) / (h[i - 2] * ksi[i - 1] + 2 * (h[i - 2] + h[i - 1]))
        print("cur eta", cur_eta)
        eta_coefs.append(cur_eta)

    return eta_coefs


def find_c_coefs(ksi, eta):
    """
        Подсчет коэффициентов с
    """
    num = len(eta)
    c_coefs = [0., 0.]
    print("ksi:")
    for k in ksi:
        print("{:.6f}".format(k))
    print("eta:")
    for e in eta:
        print("{:.6f}".format(e))

    for i in range(num - 1, 1, -1):
        c_coefs.insert(1, ksi[i] * c_coefs[1] + eta[i])

    return c_coefs[:-1]


def get_c_coefs(func, h_coefs):
    """
        Поиск коффициентов при второй степени сплайна
    """
    ksi_coefs = find_ksi_coefs(func, h_coefs)
    f_coefs = find_f_coefs(func, h_coefs)
    eta_coefs = find_eta_coefs(func, ksi_coefs, h_coefs, f_coefs)
    c_coefs = find_c_coefs(ksi_coefs, eta_coefs)

    return c_coefs


def get_x_position(func, x):
    """
        Поиск положения элемента в таблице
    """

    pos = 0

    while x > func[pos][0]:
        pos += 1

    pos -= 1

    if pos < 0:
        pos = 0

    return pos


def get_b_coefs(func, h, c):
    """
        Подсчет коэффициентов b
    """
    b_coefs = []
    N = len(func) - 1

    print("b_debug")
    print(N)

    for i in range(1, N):
        print(h[i-1])
        print(func[i][1] - func[i - 1][1])
        print(c[i], c[i - 1])
        # разобарться с этой формулой
        cur_b = (func[i][1] - func[i - 1][1]) / h[i - 1] - (h[i - 1] * (c[i] + 2 * c[i - 1])) / 3

        print(cur_b)
        b_coefs.append(cur_b)

    b_coefs.append((func[N][1] - func[N - 1][1]) / h[N - 1] - h[N - 1] * 2 * c[N - 1] / 3)

    return b_coefs


def get_d_coefs(h, c):
    """
        Подсчет коэффициентов b
    """
    d_coefs = []
    N = len(h)

    for i in range(1, N):
        cur_d = (c[i] - c[i - 1]) / (3 * h[i - 1])
        d_coefs.append(cur_d)

    d_coefs.append(- c[N - 1] / (3 * h[N - 1]))

    return d_coefs


def count_spline(func, x):
    """
        Подсчет значения функции сплайн-интерполяцией
    """
    position = get_x_position(func, x)

    a_coefs = [point[1] for point in func[:-1]]

    print("a:")
    for a in a_coefs:
        print("{:.6f}".format(a))

    h_coefs = find_h_coefs(func)

    print("h:")
    for h in h_coefs:
        print("{:.6f}".format(h))

    c_coefs = get_c_coefs(func, h_coefs)

    print("c:")
    for c in c_coefs:
        print("{:.6f}".format(c))

    b_coefs = get_b_coefs(func, h_coefs, c_coefs)

    print("b:")
    for b in b_coefs:
        print("{:.6f}".format(b))

    d_coefs = get_d_coefs(h_coefs, c_coefs)

    print("d:")
    for d in d_coefs:
        print("{:.6f}".format(d))
    print()

    print("pos ", position)
    dif = x - func[position][0]
    print(dif)

    answer = a_coefs[position] + b_coefs[position] * dif + c_coefs[position] * dif ** 2 + d_coefs[position] * dif ** 3

    return answer
