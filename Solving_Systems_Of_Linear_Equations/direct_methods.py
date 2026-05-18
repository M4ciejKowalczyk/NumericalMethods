import numpy as np
import copy
import time

def lu_decomposition(A):
    N = A.shape[0]
    U = copy.copy(A)
    L = np.eye(N)
    for i in range(2, N+1):
        for j in range(1, i):
            L[i-1, j-1] = U[i-1, j-1] / U[j-1, j-1]
            U[i-1, :] = U[i-1, :] - L[i-1, j-1] * U[j-1, :]
    return L, U

def forward_substitution(L, b):
    N = L.shape[0]
    y = np.zeros(N)
    for i in range(N):
        y[i] = (b[i] - L[i, :i] @ y[:i]) / L[i, i]
    return y

def backward_substitution(U, y):
    N = U.shape[0]
    x = np.zeros(N)
    for i in reversed(range(N)):
        x[i] = (y[i] - U[i, i+1:] @ x[i+1:]) / U[i, i]
    return x

def direct_method(A, b):
    start_time = time.perf_counter()
    L, U = lu_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    r_norm = np.linalg.norm(A @ x - b)

    return x, r_norm, elapsed_time
