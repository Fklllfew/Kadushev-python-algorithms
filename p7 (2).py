import numpy as np

def eq(n, m, matr):
    A = matr[:, :-1]
    B = matr[:, -1]

    det = np.linalg.det(A)

    unknowns = []
    for i in range(n):
        A_i = A.copy()
        A_i[:, i] = B
        det_Ai = np.linalg.det(A_i)
        unknowns.append(round(det_Ai / det))

    return unknowns



a = int(input())
b = int(input())
matrix = np.zeros((a, b), dtype=int)

for i in range(a):
    arr = list(map(int, input().split()))
    matrix[i] = arr

print(eq(a, b, matrix))