m = list(map(int, input().split()))
result = True
for i in range(len(m) // 2):
    first = i*2 + 1
    second = i*2 + 2
    if first < len(m) and m[first] < m[i]:
        result = False
        break
    if second < len(m) and m[second] < m[i]:
        result = False
        break
if result:
    print(1)
else:
    print(0)