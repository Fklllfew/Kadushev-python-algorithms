s = input()
n = len(s)

if n <= 2:
    print(ord(s[0]))
elif n < 10:
    m = (n - 1) // 2
    print(ord(s[0]) + ord(s[m]) + ord(s[-1]))
else:
    print(ord(s[-1]))