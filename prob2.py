def func(n):
    devs = []
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            devs.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        devs.append(n)
    return devs
k = int(input())
pritn(func(k))