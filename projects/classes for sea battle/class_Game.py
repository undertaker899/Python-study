from random import randint
from classes_AI_and_User import AI, User
from class_Board import Board
from class_Ship import Ship
from class_Dot import Dot
from classes_Exception import BoardWrongShipException


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
