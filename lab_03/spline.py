"""
    Модуль сплайн-интерполяции табличных функций
"""

def find_h_coefs(func):
    """
        Поиск коэффициентов h
    """
    h_coefs = [0.]

    for i in range(1, len(func)):
        h_coefs.append(func[i][0] - func[i - 1][0])

    return h_coefs


def find_f_coefs(func, h_coefs):
    """
        Поиск коэффициентов f
    """
    f_coefs = [0., 0.]

    for i in range(2, len(func)):
        dy1 = func[i][1] - func[i - 1][1]
        dy2 = func[i - 1][1] - func[i - 2][1]
        f_coefs.append(3 * (dy1 / h_coefs[i] - dy2 / h_coefs[i - 1]))

    return f_coefs


def find_ksi_coefs(func, h):
    """
        Поиск коэффициентов ξ
    """
    ksi_coefs = [0., 0., 0.]

    for i in range(3, len(func)):
        cur_ksi = - h[i - 1] / (h[i - 2] * ksi_coefs[i - 1] + 2 * (h[i - 2] + h[i - 1]))
        ksi_coefs.append(cur_ksi)

    return ksi_coefs


def find_eta_coefs(func, ksi, h, f):
    """
        Поиск коэффициентов η
    """
    eta_coefs = [0., 0., 0.]

    for i in range(3, len(func)):
        cur_eta = (f[i - 1] - h[i - 2] * eta_coefs[i - 1]) / (h[i - 2] * ksi[i - 1] + 2 * (h[i - 2] + h[i - 1]))
        eta_coefs.append(cur_eta)

    return eta_coefs


def find_c_coefs(ksi, eta):
    """
        Подсчет коэффициентов с
    """
    num = len(eta)
    c_coefs = [eta[num - 1]]


    for i in range(num - 1, 1, -1):
        print(c_coefs)
        c_coefs.insert(0, ksi[i] * c_coefs[0] + eta[i])

    return c_coefs


def get_c_coefs(func, arg):
    """
        Поиск коффициентов при второй степени сплайна
    """
    h_coefs = find_h_coefs(func)
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

    if pos > len(func) - 1:
        pos = len(func) - 1

    return pos


def count_spline(func, x):
    """
        Подсчет значения функции сплайн-интерполяцией
    """
    position = get_x_position(func, x)

    a_coef = func[position][1]
    return a_coef
