def nod(a, b):
    if b == 0:
        return a, 1, 0
    else:
        nodvalue, x1, y1 = nod(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return nodvalue, x, y
print(nod(8, 14))