class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_perimeter(self):
        return self.width * 2 + self.length * 2

    def get_area(self):
        return self.width * self.length


r1 = Rectangle(6, 9)
print('Width =', r1.width, '| Length =', r1.length, '| Perimeter =', r1.get_perimeter(), '| Area =', r1.get_area())
