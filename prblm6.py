def to_dec(base, number):
    number_str = str(number)
    hex_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    result = 0
    power = 0
    for digit in reversed(number_str):
        value = hex_map[digit]
        result += value * (base ** power)
        power += 1
    return result

def from_dec(dec_num, base):
    if dec_num == 0:
        return "0"
    hex_map = {
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
    result = ""
    num = dec_num
    while num > 0:
        remainder = num % base
        if remainder >= 10:
            result = hex_map[remainder] + result
        else:
            result = str(remainder) + result
        num //= base
    return result

calc = open('input.txt', 'r+')
s = calc.read()
m = s.split()
base = m[-1]
n1 = int(to_dec(int(base), m[0]))
n2 = int(to_dec(int(base), m[1]))
op = m[2]
res = ''
if op == '-':
    res = from_dec((n1-n2), int(base))
elif op == '+':
    res = from_dec((n1+n2), int(base))
elif op == '*':
    res = from_dec((n1*n2), int(base))
calc.write('\n' + res)

calc.close()