print('Game of Xs and 0s')
print('--------------')
print('Starting game field')
print('  | 0 | 1 | 2 ')
print('0 | - | - | -')
print('1 | - | - | -')
print('2 | - | - | -')
print('--------------')
print('Rule 1: Game for 2 players')
print('Rule 2: Turn based game (each player makes one input per turn)')
print('Rule 3: Whichever player makes 3 (Xs or 0s) in a row wins, if neither player does it is a draw')
print('--------------')
print('Xs input two numbers (row and column) with whitespace between: ')
game_field = [[' ', ' ', ' '] for i in range(3)]


def field():
    print(f'  0 1 2')
    for i in range(3):
        print(f'{i} {game_field[i][0]} {game_field[i][1]} {game_field[i][2]}')


field()


def player_input():
    while True:
        row, column = map(int, input('Your move: ').split())
        return row, column


player_input()
