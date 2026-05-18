import matplotlib.pyplot as plt
from matrix_builder import build_matrix_and_vector
from iterative_methods import jacobi_method, gauss_seidel_method
from direct_methods import direct_method

def zadanieB(index_number, size):
    A, b, N = build_matrix_and_vector(index_number, size, False)
    print(f"Macierz A {N}x{N} i wektor b wygenerowane.")
    x, r_norm, iteration_count, elapsed_time = jacobi_method(A, b)
    print("zadanie B")
    print("Metoda Jacobiego:")
    print(f"Liczba iteracji: {iteration_count}")
    print(f"Końcowa norma residuum: {r_norm[-1]:.2e}")
    print(f"Czas wykonania: {elapsed_time:.4f} s")

    plt.semilogy(range(len(r_norm)), r_norm)
    plt.xlabel("Numer iteracji")
    plt.ylabel("Norma residuum")
    plt.title("Zbieżność metody Jacobiego")
    plt.grid(True)
    plt.show()

    x, r_norm, iteration_count, elapsed_time = gauss_seidel_method(A, b)

    print("Metoda Gaussa-Seidla:")
    print(f"Liczba iteracji: {iteration_count}")
    print(f"Końcowa norma residuum: {r_norm[-1]:.2e}")
    print(f"Czas wykonania: {elapsed_time:.4f} s")

    plt.semilogy(range(len(r_norm)), r_norm)
    plt.xlabel("Numer iteracji")
    plt.ylabel("Norma residuum")
    plt.title("Zbieżność metody Gaussa-Seidla")
    plt.grid(True)
    plt.show()

def zadanieC(index_number, size):
    A, b, N = build_matrix_and_vector(index_number, size, True)

    print(f"Macierz A {N}x{N} i wektor b wygenerowane.")

    x, r_norm, iteration_count, elapsed_time = jacobi_method(A, b)
    print("zadanie C")
    print("Metoda Jacobiego:")
    print(f"Liczba iteracji: {iteration_count}")
    print(f"Końcowa norma residuum: {r_norm[-1]:.2e}")
    print(f"Czas wykonania: {elapsed_time:.4f} s")

    plt.semilogy(range(len(r_norm)), r_norm)
    plt.xlabel("Numer iteracji")
    plt.ylabel("Norma residuum")
    plt.title("Zbieżność metody Jacobiego")
    plt.grid(True)
    plt.show()

    x, r_norm, iteration_count, elapsed_time = gauss_seidel_method(A, b)

    print("Metoda Gaussa-Seidla:")
    print(f"Liczba iteracji: {iteration_count}")
    print(f"Końcowa norma residuum: {r_norm[-1]:.2e}")
    print(f"Czas wykonania: {elapsed_time:.4f} s")

    plt.semilogy(range(len(r_norm)), r_norm)
    plt.xlabel("Numer iteracji")
    plt.ylabel("Norma residuum")
    plt.title("Zbieżność metody Gaussa-Seidla")
    plt.grid(True)
    plt.show()

def zadanieD(index_number, size):
    A, b, N = build_matrix_and_vector(index_number, size, True)

    print(f"Macierz A {N}x{N} i wektor b wygenerowane.")

    print("Zadanie D")
    x, r_norm, elapsed_time = direct_method(A, b)
    print("Metoda bezpośrednia:")
    print(f"Końcowa norma residuum: {r_norm:.2e}")
    print(f"Czas wykonania: {elapsed_time:.4f} s")

if __name__ == "__main__":
    index_number = 198202
    size = 1202

    zadanieB(index_number, size)

    #zadanieC(index_number, size)

    #zadanieD(index_number, size)
    #TODO wypisywać dane do tabeli
    print("Zadanie E")
    matrix_sizes = [100, 300, 500, 1000, 1500, 2000, 2500, 3000]
    times_jacobi = []
    times_gauss = []
    times_direct = []

    iterations_jacobi = []
    iterations_gauss = []

    norm_jacobi = []
    norm_gauss = []
    norm_direct = []
    for i in range(len(matrix_sizes)):
        A, b, N = build_matrix_and_vector(198202, matrix_sizes[i], False)
        print(f"Rozmiar macierzy: {N}")

        _, n_jacobi, i_jacobi,t_jacobi = jacobi_method(A,b)
        times_jacobi.append(t_jacobi)
        iterations_jacobi.append(i_jacobi)
        norm_jacobi.append(min(n_jacobi))

        _, n_gauss, i_gauss, t_gauss = gauss_seidel_method(A, b)
        times_gauss.append(t_gauss)
        iterations_gauss.append(i_gauss)
        norm_gauss.append(min(n_gauss))

        _, n_direct, t_direct = direct_method(A, b)
        times_direct.append(t_direct)
        norm_direct.append(n_direct)

    print(times_jacobi)
    print(times_gauss)
    print(times_direct)

    print(iterations_jacobi)
    print(iterations_gauss)

    print(norm_jacobi)
    print(norm_gauss)
    print(norm_direct)

    # Wykres 1: Skala liniowa
    plt.figure(figsize=(10, 5))
    plt.plot(matrix_sizes, times_jacobi, marker='o', label='Jacobi')
    plt.plot(matrix_sizes, times_gauss, marker='o', label='Gauss-Seidel')
    plt.plot(matrix_sizes, times_direct, marker='o', label='Bezpośrednia (LU)')
    plt.title('Czas wykonania metod vs rozmiar macierzy (skala liniowa)')
    plt.xlabel('Liczba niewiadomych (N)')
    plt.ylabel('Czas [s]')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Wykres 2: Skala logarytmiczna
    plt.figure(figsize=(10, 5))
    plt.plot(matrix_sizes, times_jacobi, marker='o', label='Jacobi')
    plt.plot(matrix_sizes, times_gauss, marker='o', label='Gauss-Seidel')
    plt.plot(matrix_sizes, times_direct, marker='o', label='Bezpośrednia (LU)')
    plt.yscale('log')
    plt.title('Czas wykonania metod vs rozmiar macierzy (skala logarytmiczna)')
    plt.xlabel('Liczba niewiadomych (N)')
    plt.ylabel('Czas [s] (log)')
    plt.grid(True, which='both', linestyle='--')
    plt.legend()
    plt.tight_layout()
    plt.show()