calc = open('input.txt', 'r+')        # задача 4
s = calc.read()

m = s.split()
n1 = int(m[0])
n2 = int(m[1])
op = m[2]

if op == '-':
    res = n1-n2
elif op == '+':
    res = n1+n2
elif op == '*':
    res = n1*n2
calc.write('\n' + str(res))

calc.close()