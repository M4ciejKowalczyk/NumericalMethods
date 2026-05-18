import numpy as np
import time

def jacobi_method(A, b, tolerance = 1e-9):
    N = len(b)
    x = np.ones(N)

    iteration_count = 0

    r_norm = []

    inorm = np.linalg.norm(A @ x - b)
    r_norm.append(inorm)

    start_time = time.perf_counter()

    while inorm>tolerance:
        x_new = np.zeros_like(x)
        for i in range(N):
            sigma = A[i, :i] @ x[:i] + A[i, i + 1:] @ x[i + 1:]
            x_new[i] = (b[i] - sigma) / A[i, i]
        x = x_new
        inorm = np.linalg.norm(A @ x - b)
        iteration_count += 1
        r_norm.append(inorm)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    return x, r_norm, iteration_count, elapsed_time


def gauss_seidel_method(A, b, tolerance = 1e-9):
    N = len(b)
    x = np.ones(N)

    iteration_count = 0

    r_norm = []

    inorm = np.linalg.norm(A @ x - b)
    r_norm.append(inorm)

    start_time = time.perf_counter()

    while inorm > tolerance:
        for i in range(N):
            sigma = A[i, :i] @ x[:i] + A[i, i + 1:] @ x[i + 1:]
            x[i] = (b[i] - sigma) / A[i, i]
        inorm = np.linalg.norm(A @ x - b)
        iteration_count += 1
        r_norm.append(inorm)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    return x, r_norm, iteration_count, elapsed_time

