a = list(map(int, input().split())) #задача 7 готово
most = -1
for i in a:
    if a.count(i) > most:
        most = i
print(most)