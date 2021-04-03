class BoardException(Exception):
    pass  # Not for player


class BoardOutException(BoardException):
    def __str__(self):
        return 'You are trying to move out of border'


class BoardUsedException(BoardException):
    def __str__(self):
        return 'You are repeating move'


class WrongShipException(BoardException):
    pass  # Not for player


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Ship:
    def __init__(self, size, front, turn):
        self.size = size
        self.front = front
        self.turn = turn
        self.life = size  # Same value as self.size, but not constant

    def dots(self):
        ship_dots = []  # Empty massive for creating ships

        for i in range(self.size):
            coord_x = self.front.x
            coord_y = self.front.y

            if self.turn == 0:
                coord_x = coord_x + 1  # Vertical ship

            elif self.turn == 1:
                coord_y = coord_y + 1  # Horizontal ship

            ship_dots.append(Dot(coord_x, coord_y))

        return ship_dots
