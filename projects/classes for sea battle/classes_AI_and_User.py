from class_Player import Player
from class_Dot import Dot
from random import randint


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
