from class_Dot import Dot
from classes_Exception import WrongShipException, BoardOutException, BoardUsedException


class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid
        self.count = 0  # Score
        self.field = [['0'] * size for _ in range(size)]  # Creating game field as 2d massive
        self.ships = []  # Ships position
        self.taken = []  # Taken coordinates

    def __str__(self):
        show_ship = ''
        show_ship = show_ship + '  | 1 | 2 | 3 | 4 | 5 | 6 |'

        for i, row in enumerate(self.field):  # Rows of our board
            show_ship = show_ship + f'\n{i + 1} | ' + ' | '.join(row) + ' | '  # № of row + dots in this row

        if self.hid:
            show_ship = show_ship.replace('■ ', '0')  # Hiding our ships, if needed

        return show_ship

    def add_ship(self, ship):
        for dot in ship.dots:
            if self.out(dot) or dot in self.taken:
                raise WrongShipException
                # Raising exception if coordinate where we want to put ship is taken or out of game board

        for dot in ship.dots:
            self.field[dot.x][dot.y] = '■'
            self.taken.append(dot)  # Creating ships on board

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, play_stage=False):
        near_ship = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        # All possible coordinates near the ship

        for dot in ship.dots:
            for dotx, doty in near_ship:
                coord = Dot(dot.x + dotx, dot.y + doty)
                if not(self.out(coord)) and coord not in self.taken:
                    if play_stage:  # Stage of game, when we put ships on board or when we play
                        self.field[coord.x][coord.y] = '.'
                    self.taken.append(coord)

    def out(self, dot):
        return not ((0 <= dot.x <= self.size) and (0 <= dot.y <= self.size))  # Checking if shot outside the game field

    def shot(self, dot):
        if self.out(dot):
            raise BoardOutException

        if dot in self.taken:  # Coordinate taken by ship, its contour or was shot at previously
            raise BoardUsedException

        self.taken.append(dot)  # Coordinate taken after shooting

        for ship in self.ships:
            if dot in ship.dots:  # Successful shot
                ship.life = ship.life - 1
                self.field[dot.x][dot.y] = 'X'
                if ship.life == 0:
                    self.count = self.count + 1  # Keeping score of destroyed ships
                    self.contour(ship, play_stage=True)
                    print('Ship destroyed')
                    return False  # Ending current player turn
                else:
                    print('Enemy ship successfully shot at, but not destroyed')
                    return True  # Keeping current player turn

            self.field[dot.x][dot.y] = '.'
            print('You missed')
            return False  # Ending current player turn

    def next_stage(self):  # Method to reset state of game board so the game could be played
        self.taken = []
