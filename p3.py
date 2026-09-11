sym = {
    'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O',
    'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
    'Y': 'Y', '1': '1', '8': '8',
    'E': '3', 'J': 'L', 'S': '2', 'Z': '5',
    '3': 'E', 'L': 'J', '2': 'S', '5': 'Z',
}

s = input()
n = 0
m = len(s) - 1
mir = 1
pal = 1

for _ in range(len(s) // 2 + 1):
    if not (s[n] in sym and sym[s[n]] == s[m]):
        mir = 0
    if not (s[n] == s[m]):
        pal = 0
    n += 1
    m -= 1

if mir == 0 and pal == 0:
    print(f"{s} is not a palindrome.")
elif mir == 1 and pal == 0:
    print(f"{s} is a mirrored string.")
elif mir == 0 and pal == 1:
    print(f"{s} is a regular palindrome.")
elif mir == 1 and pal == 1:
    print(f"{s} is a mirrored palindrome.")