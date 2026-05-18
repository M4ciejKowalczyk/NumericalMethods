import pandas as pd
import numpy as np

def wczytaj_dane(sciezka):
    df = pd.read_csv(sciezka)
    return df[["Dystans (m)","Wysokość (m)"]].to_numpy()

def wezly_rownomierne(dane, n):
    indeksy = np.linspace(0, len(dane) - 1, n, dtype=int)
    wezly = dane[indeksy]
    return wezly

def wezly_czebyszewa(dane, n):
    x_dane = dane[:, 0]
    a, b = x_dane.min(), x_dane.max()

    # Wyznaczamy węzły Czebyszewa w [a, b]
    i = np.arange(n)
    x_czeb = 0.5 * (a + b) + 0.5 * (b - a) * np.cos((2 * i + 1) * np.pi / (2 * n))

    # Dla każdego x_czeb znajdujemy najbliższy punkt z danych
    x_dane_indices = np.searchsorted(x_dane, np.sort(x_czeb))
    x_dane_indices = np.clip(x_dane_indices, 0, len(dane) - 1)

    wezly = dane[x_dane_indices]
    return wezly