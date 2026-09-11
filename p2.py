m = list(map(str, input().split())) #задача 2 готово
slices = int(m[0])
s0 = m[1]
s = ''
for i in range(0, len(m[1]), slices):
    s1 = s0[i:i+3]
    for j in range(2, -1, -1):
        s += s1[j]
print(s)
