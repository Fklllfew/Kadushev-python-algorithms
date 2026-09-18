import numpy as np

n, m = map(int, input().split())
matrix = np.zeros((n, m), dtype=int)
num = 1
x, y = 0, 0

while num <= n * m:
    while x < m and matrix[y][x] == 0:
        matrix[y][x] = num
        num += 1
        x += 1
    x -= 1
    y += 1

    while y < n and matrix[y][x] == 0:
        matrix[y][x] = num
        num += 1
        y += 1
    y -= 1
    x -= 1

    while x >= 0 and matrix[y][x] == 0:
        matrix[y][x] = num
        num += 1
        x -= 1
    x += 1
    y -= 1

    while y >= 0 and matrix[y][x] == 0:
        matrix[y][x] = num
        num += 1
        y -= 1
    y += 1
    x += 1

for i in range(n):
    for j in range(m):
        matrix[i][j] = matrix[i][j] * (i+1)


print(matrix)