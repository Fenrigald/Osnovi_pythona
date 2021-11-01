class ComplNum:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма:')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение:')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'Число = {self.a} + {self.b} * i'


z_1 = ComplNum(1, -2)
z_2 = ComplNum(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)