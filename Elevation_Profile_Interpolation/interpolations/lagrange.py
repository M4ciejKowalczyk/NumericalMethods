import numpy as np

def Polynomian(x, x_wezly, y_wezly):
    fi = np.ones(len(x_wezly))
    for i in range(len(x_wezly)):
        for j in range(len(x_wezly)):
            if(i!=j):
                fi[i] = fi[i] * (x - x_wezly[j]) / (x_wezly[i] - x_wezly[j])
    result = 0
    for i in range(len(x_wezly)):
        result += y_wezly[i] * fi[i]
    return result

def lagrange(wezly):
    x_wezly = wezly[:, 0]
    y_wezly = wezly[:, 1]

    # Normalizacja dziedziny[0,1]
    x_min, x_max = np.min(x_wezly), np.max(x_wezly)
    x_norm = (x_wezly - x_min) / (x_max - x_min)


    # Stworzenie gęstej siatki x_norm[0,1]
    x_norm_plot = np.linspace(0,1,500)

    # Obliczenie y=P(x_norm)
    y_plot = []
    for x in x_norm_plot:
        y_plot.append(Polynomian(x, x_norm, y_wezly))

    y_plot = np.array(y_plot)

    # Transformacja odwrotna dziedziny
    x_plot = x_norm_plot * (x_max - x_min) + x_min

    # Zwracamy punkty (x,y)
    return np.column_stack((x_plot, y_plot))
