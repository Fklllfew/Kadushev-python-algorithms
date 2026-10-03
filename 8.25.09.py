bliny = ['мука', 'молоко', 'яйца', 'сахар', 'соль', 'масло', 'сода']
syrniki = ['творог', 'яйца', 'мука', 'сахар', 'сметана', 'ванилин']

s1 = set(bliny)
s2 = set(syrniki)

print(s1 - s2)
print(s2 - s1)
print(s1 ^ s2)
print(s1 & s2)