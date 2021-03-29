class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_str(self):
        return f'Rectangle ({self.x}, {self.y}, {self.width}, {self.height})'


rect_01 = Rectangle(5, 10, 50, 100)
print(rect_01.get_str())
