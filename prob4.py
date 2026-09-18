size, symb = map(str, input().split())
if int(size) % 2 != 0:
    for i in range((int(size) // 2) + 1):
        print(symb * (i + 1))
    for j in range(int(size)  // 2, 0, -1):
        print(symb * j)
else:
    for i in range(int(size) // 2):
        print(symb * (i + 1))
    for j in range(int(size)  // 2, 0, -1):
        print(symb * j)
