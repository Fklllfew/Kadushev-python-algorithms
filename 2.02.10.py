rad, side = map(int, input().split())

a = 2 * 3.141592 * rad
b = 3.141592 * rad ** 2
c = side ** 2

acertainratio = b / c * 100

print(
    f'Длина окружности равно {a:.2f}. \n'
    f'Площадь круга составляет {acertainratio:.2f} % от площади квадрата.'
)