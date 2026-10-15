from math import sqrt


class Vector:
    def __init__(self, x, y, z):
        assert isinstance(x, (float, int)), 'X должен быть числом'
        assert isinstance(y, (float, int)), 'Y должен быть числом'
        assert isinstance(z, (float, int)), 'Z должен быть числом'
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"



v1 = Vector(*map(float, input().split()))
v2 = Vector(1, 1, 1)

print(v1)          # Vector(1, 2, 3)
print(v1 + v2)     # Vector(2, 3, 4)
print(abs(v1))     # длина
print(v1 * v2)     # скалярное произведение
print(v1 * 2)      # вектор