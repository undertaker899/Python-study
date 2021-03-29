from circle1 import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

square_1 = Square(5)
square_2 = Square(10)

circle_1 = Circle(1)
circle_2 = Circle(2)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print('Area of current square =', figure.get_area_square())
    elif isinstance(figure, Circle):
        print('Area of current circle =', figure.get_area_circle())
    else:
        print('Area of current rectangle =', figure.get_area())
