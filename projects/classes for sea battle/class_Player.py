from classes_Exception import BoardException


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
