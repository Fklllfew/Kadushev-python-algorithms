def sift(a, i, n):
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < n and a[left] > a[largest]:
            largest = left
        if right < n and a[right] > a[largest]:
            largest = right
        if largest == i:
            break
        a[i], a[largest] = a[largest], a[i]
        i = largest

m = list(map(int, input().split()))
for i in range(len(m) // 2 - 1, -1, -1):
    sift(m, i, len(m))

for i in range(len(m)):
    m[0], m[-1 * i - 1] = m[-1 * i - 1], m[0]
    sift(m, 0, len(m) - i - 1)
print(m)
