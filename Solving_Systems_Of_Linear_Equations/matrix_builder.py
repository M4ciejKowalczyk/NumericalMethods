import numpy as np

def build_matrix_and_vector(index_number: int, N: int, is_c: bool):
    index_str = str(index_number)
    e = int(index_str[3])
    f = int(index_str[2])

    A = np.zeros((N,N))
    if(not is_c):
        a1 = 5 + e
    else:
        a1 = 3
    a2 = -1
    a3 = -1

    for i in range(N):
        A[i, i] = a1
        if i < N - 1:
            A[i, i+1] = a2
        if i > 0:
            A[i, i-1] = a2
        if i < N - 2:
            A[i, i+2] = a3
        if i > 1:
            A[i, i-2] = a3

    b = np.array([np.sin(n * (f + 1)) for n in range(N)])

    return A, b, N