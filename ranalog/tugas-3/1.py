# in order to show that an algorithm is not unique, design
# two different algorithmt that solve the same problem

import numpy as np


def isPowerOfTwo(n):
    return n and not (n & n - 1)


def matmul(
    A: np.ndarray,
    B: np.ndarray,
) -> np.ndarray:
    assert A.shape[1] == B.shape[0]
    C = np.zeros((A.shape[0], B.shape[1]))

    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i, j] += A[i, k] * B[k, j]

    return C


def matmul_dnc(
    A: np.ndarray,
    B: np.ndarray,
    C: np.ndarray,
    n: int = None,
) -> np.ndarray:
    """
    matmul dnc on nxn matrix it's O(n^3)
    """
    if n == 1:
        C += A * B
        return
    n_init = n
    # if n not power of 2:
    if not isPowerOfTwo(n):
        n = max(A.shape[0], A.shape[1], B.shape[0], B.shape[1])
        n = 2 ** (n - 1).bit_length()
        A = np.pad(A, ((0, n - A.shape[0]), (0, n - A.shape[1])))

        B = np.pad(B, ((0, n - B.shape[0]), (0, n - B.shape[1])))
        C = np.pad(C, ((0, n - C.shape[0]), (0, n - C.shape[1])))

    # conquer
    A_11 = A[: n // 2, : n // 2]
    A_12 = A[: n // 2, n // 2 :]
    A_21 = A[n // 2 :, : n // 2]
    A_22 = A[n // 2 :, n // 2 :]
    B_11 = B[: n // 2, : n // 2]
    B_12 = B[: n // 2, n // 2 :]
    B_21 = B[n // 2 :, : n // 2]
    B_22 = B[n // 2 :, n // 2 :]
    C_11 = C[: n // 2, : n // 2]
    C_12 = C[: n // 2, n // 2 :]
    C_21 = C[n // 2 :, : n // 2]
    C_22 = C[n // 2 :, n // 2 :]

    matmul_dnc(A_11, B_11, C_11, n // 2)
    matmul_dnc(A_12, B_21, C_11, n // 2)
    matmul_dnc(A_11, B_12, C_12, n // 2)
    matmul_dnc(A_12, B_22, C_12, n // 2)
    matmul_dnc(A_21, B_11, C_21, n // 2)
    matmul_dnc(A_22, B_21, C_21, n // 2)
    matmul_dnc(A_21, B_12, C_22, n // 2)
    matmul_dnc(A_22, B_22, C_22, n // 2)

    C = np.vstack((np.hstack((C_11, C_12)), np.hstack((C_21, C_22))))

    if not isPowerOfTwo(n_init):
        C = C[:n_init, :n_init]
        return C

    return C


if __name__ == "__main__":
    n = 13
    C = np.zeros((n, n))
    A = np.random.randint(0, 10, (n, n))
    B = np.random.randint(0, 10, (n, n))

    C_matmul_dnc = matmul_dnc(A, B, np.zeros((n, n)), n)
    C_matmul = matmul(A, B)
    C_builtin = A @ B
    print(f"==>> C_matmul: {C_matmul}")
    print(f"==>> C_matmul_dnc: {C_matmul_dnc}")
    print(f"==>> C_builtin: {C_builtin}")
