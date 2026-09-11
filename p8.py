n = int(input())                     #задача 8 готово
m = list(map(int, input().split()))
b = 0
s = 0
med = 0
for i in range(n):
    for j in range(n):
        if m[i] > m[j]:
            b += 1
        elif m[i] < m[j]:
            s += 1
    if b == s:
        med = m[i]
        break
    b = 0
    s = 0
print(med)