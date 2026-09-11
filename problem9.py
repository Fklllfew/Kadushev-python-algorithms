s = input()               #задача 9 готово
s += ' '
m = ['.', '?', '!']
counter = 0
for i in range(len(s)):
    if s[i-1] in m and not(s[i] in m):
        counter += 1
if counter == 0 and len(s) != 0:
    counter += 1
print(counter)
