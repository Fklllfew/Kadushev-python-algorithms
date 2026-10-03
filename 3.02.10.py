s1, s2 = map(str, input().split())
s1 = s1[1::-1] + s1[2:]
s2 = s2[1::-1] + s2[2:]
print(s1 + '-' + s2)