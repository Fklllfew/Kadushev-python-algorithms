m = list(map(int, input().split())) #задача 1 готово
missed = -1
m.sort()
for i in range(m[-1]-2):
  if m[i] + 1 != m[i + 1]:
    missed = m[i] + 1
if missed == -1:
  missed = m[-1]
print(missed)