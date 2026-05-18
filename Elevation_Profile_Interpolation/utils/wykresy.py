import matplotlib.pyplot as plt

def rysuj_profil_trasy(dane):
    plt.figure(figsize=(10, 5))
    plt.plot(dane[:, 0], dane[:, 1], label="Profil trasy", color="blue")
    plt.xlabel("Dystans [m]")
    plt.ylabel("Wysokość [m n.p.m.]")
    plt.title("Profil wysokościowy trasy")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def rysuj_wykres(dane, wezly, interpolacja, tytul="Interpolacja"):
    plt.figure(figsize=(10, 5))
    y_max = (max(dane[:,1]) - min(dane[:,1]))*1.2 + min(dane[:,1])
    y_min = min(dane[:,1]) - (max(dane[:,1]) - min(dane[:,1]))*0.2
    plt.ylim(y_min, y_max)
    plt.plot(dane[:, 0], dane[:, 1], 'b--', label="Dane rzeczywiste")
    plt.plot(wezly[:, 0], wezly[:, 1], 'ro', label="Punkty węzłowe", markersize=5)
    plt.plot(interpolacja[:, 0], interpolacja[:, 1], 'k-', label="Interpolacja")
    plt.xlabel("Dystans [m]")
    plt.ylabel("Wysokość [m n.p.m.]")
    plt.title(tytul)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()