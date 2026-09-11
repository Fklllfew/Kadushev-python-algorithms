vowels = set('аеёиоуыэюяАЕЁИОУЫЭЮЯ')
s = input()
s = ' ' + s + ' '
sn = ''
for i in range(len(s)):
    sn += s[i]
    if s[i] in vowels and not(s[i-1] in vowels) and not(s[i+1] in vowels):
        sn += ('с'+s[i])
    elif s[i] in vowels and s[i+1] in vowels:
        if s[i-1] != ' ':
            sn+=('с'+s[i])
print(sn[1:-1])
