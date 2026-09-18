def mnk(x, y):
    koefs = []
    sumx = sum(x)
    sumy = sum(y)
    sumsqx = 0
    summxy = 0
    n = len(x)
    for i in x:
        sumsqx += i**2
    for i in x:
        for j in y:
            summxy += i * j
    a = (n*summxy - sumx*sumy)/(n*sumsqx - sumx ** 2)
    b = (sumy - a * sumx)/(n)
    koefs.append(a)
    koefs.append(b)
    return koefs

x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(mnk(x, y))