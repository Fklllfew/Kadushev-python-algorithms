a = list(map(str, input().split()))  #задача 6 готово
for i in a:
    if a.count(i) == 1:
        print(i)