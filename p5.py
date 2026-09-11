a = list(map(str, input().split()))  #задача 5 готово
m = list(a[-1]) + a[0:(len(a)-1)]
print(*m)