from random import randint  # For random AI moves


class BoardException(Exception):  # Creating exception classes
    pass  # Not for player


class BoardOutException(BoardException):
    def __str__(self):
        return 'You are trying to move out of border'


class BoardUsedException(BoardException):
    def __str__(self):
        return 'You are repeating move'


class BoardWrongShipException(BoardException):
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
                raise BoardWrongShipException
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

    def end_game(self):  # Method for checking win condition
        return self.count == len(self.ships)


class Player:
    def __init__(self, user_board, ai_board):
        self.user_board = user_board
        self.ai_board = ai_board

    def ask(self):
        raise NotImplementedError  # Doesn't work yet, for child classes

    def move(self):
        while True:
            try:
                player_input = self.ask()
                repeat_input = self.ai_board.shot(player_input)
                return repeat_input
            except BoardException as error:  # Using parent exception to catch any exceptions
                print(error)


class AI(Player):
    def ask(self):
        dot = Dot(randint(0, 5), randint(0, 5))  # AI moves randomly
        print(f'AI move: {dot.x + 1}, {dot.y + 1}')
        return dot


class User(Player):
    def ask(self):
        while True:
            coords = input('User move: ').split()
            if len(coords) != 2:
                print('Enter 2 coordinates as your move')
                continue

            x, y = coords
            if not(x.isdigit()) and not (y.isdigit()):
                print('Enter two numbers (from 1 to 6) as coordinates')
                continue

            x, y = int(x), int(y)
            return Dot(x - 1, y - 1)  # List indexes start from 0, but we use 1 as first number in our game field


class Game:
    def __init__(self, size=6):
        self.size = size
        us = self.random_board()
        ai = self.random_board()
        ai.hid = True

        self.ai = AI(ai, us)
        self.us = User(us, ai)

    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for length in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), length, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.next_stage()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):
        print("  Sea battle  ")
        print("-------------------")
        print(" Input your move as x and y ")
        print(" x - № of row  ")
        print(" y - № of column ")

    def loop(self):
        step = 0
        while True:
            print("-" * 20)
            print("User board:")
            print(self.us.board)
            print("-" * 20)
            print("AI board:")
            print(self.ai.board)
            print("-" * 20)
            if step % 2 == 0:
                print("User move")
                repeat = self.us.move()
            else:
                print("AI move")
                repeat = self.ai.move()
            if repeat:
                step = step - 1

            if self.ai.board.end_game():
                print("-" * 20)
                print("User wins")
                break

            if self.us.board.end_game():
                print("-" * 20)
                print("AI wins")
                break
            step = step + 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()
