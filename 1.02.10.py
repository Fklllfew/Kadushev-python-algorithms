s = input()
num = s.count('student')
m = s.split(sep='student_')
m.pop(0)
nmax = ''
maxscore = 0

for i in m:
    if int(i[-2:-1]) > maxscore:
        maxscore = int(i[-2:-1])
for i in m:
    if int(i[-2:-1]) == maxscore:
        nmax += '-' + i[:-2]
print(nmax[1:])
