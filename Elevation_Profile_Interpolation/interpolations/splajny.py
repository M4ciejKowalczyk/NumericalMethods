import numpy as np


def splajny(wezly):

    x_wezly = wezly[:,0]
    y_wezly = wezly[:,1]
    n = len(x_wezly)

    # Obliczenie różnic między węzłami
    h = np.diff(x_wezly)

    # Utworzenie macierzy układu równań
    A = np.zeros((n, n))
    rhs = np.zeros(n)

    # Warunki brzegowe (druga pochodna = 0 na końcach)
    A[0, 0] = 1
    A[-1, -1] = 1

    # Równania dla węzłów wewnętrznych (1 do n-2)
    for i in range(1, n - 1):
        # Współczynniki dla M_{i-1}, M_i, M_{i+1}
        A[i, i - 1] = h[i - 1]  # Współczynnik dla M_{i-1}
        A[i, i] = 2 * (h[i - 1] + h[i])  # Współczynnik dla M_i
        A[i, i + 1] = h[i]  # Współczynnik dla M_{i+1}

        # Prawa strona równania
        term1 = (y_wezly[i + 1] - y_wezly[i]) / h[i]
        term2 = (y_wezly[i] - y_wezly[i - 1]) / h[i - 1]
        rhs[i] = 6 * (term1 - term2)

    # Rozwiązanie układu równań dla drugich pochodnych
    M = np.linalg.solve(A, rhs)

    # Obliczenie współczynników wielomianów sklejanych
    a = y_wezly[:-1]  # a_i = y_i
    c = M[:-1] / 2  # c_i = M_i / 2
    d = np.diff(M) / (6 * h)  # d_i = (M_{i+1} - M_i) / (6 * h_i)
    b = np.diff(y_wezly) / h - h * (2 * M[:-1] + M[1:]) / 6  # b_i = (y_{i+1}-y_i)/h_i - h_i(2M_i+M_{i+1})/6

    # Generowanie gęstej siatki punktów
    x_plot = np.linspace(x_wezly[0], x_wezly[-1], 500)
    y_plot = np.zeros(500)

    # Obliczenie wartości interpolowanych
    for i in range(500):
        # Znalezienie przedziału dla danego punktu
        idx = np.searchsorted(x_wezly, x_plot[i]) - 1
        idx = max(0, min(idx, n - 2))  # Ograniczenie do zakresu

        # Obliczenie wartości wielomianu
        dx = x_plot[i] - x_wezly[idx]
        y_plot[i] = a[idx] + b[idx] * dx + c[idx] * dx ** 2 + d[idx] * dx ** 3

    return np.column_stack((x_plot, y_plot))
