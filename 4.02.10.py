def che(s):
    if len(s) < 4:
        if s.isupper():
            return s.upper()
        return s

    num = 0
    for i in range(4):
        if s[i].isupper():
            num += 1

    if num >= 3:
        return s.upper()

    return s
