def intro():
    print('Game of Xs and 0s')
    print('--------------')
    print('Rule 1: Game for 2 players')
    print('Rule 2: Turn based game (each player makes one input per turn)')
    print('Rule 3: Whichever player makes 3 (Xs or 0s) in a row wins, if neither player does it is a draw')
    print('--------------')


def field():
    print(f'  0|1|2|')
    for i in range(3):
        print(f'{i}|{game_field[i][0]}|{game_field[i][1]}|{game_field[i][2]}|')


def player_input():
    while True:
        coordinates = input('Your move: ').split()
        if len(coordinates) != 2:
            print("You didn't enter coordinates in correct format")
            continue
        row, column = coordinates
        if (row.isdigit()) is False or (column.isdigit()) is False:
            print("You didn't enter numbers as your (row and column) move")
            continue
        row, column = int(row), int(column)
        if row < 0 or row > 2 or column < 0 or column > 2:
            print('Move is outside of game field')
            continue
        if game_field[row][column] != ' ':
            print('Repeated move')
            continue
        return row, column


def win_game():
    win = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
           ((0, 0), (1, 0), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 1), (1, 1), (2, 1)),
           ((0, 2), (1, 1), (2, 0)), ((0, 2), (1, 2), (2, 2))]
    for coordinate in win:
        crd1 = coordinate[0]
        crd2 = coordinate[1]
        crd3 = coordinate[2]
        if game_field[crd1[0]][crd1[1]] == game_field[crd2[0]][crd2[1]] == game_field[crd3[0]][crd3[1]] != ' ':
            field()
            print('--------------')
            print(f'{game_field[crd1[0]][crd1[1]]}s won')
            return True
    return False


intro()
game_field = [[' ', ' ', ' '] for i in range(3)]
move = 0
while True:
    move = move + 1
    field()
    if move % 2 == 1:
        print('Xs turn')
    else:
        print('0s turn')
    row, column = player_input()
    if move % 2 == 1:
        game_field[row][column] = 'X'
    else:
        game_field[row][column] = '0'
    if win_game():
        break
    if move == 9:
        field()
        print('--------------')
        print('Draw')
        break
