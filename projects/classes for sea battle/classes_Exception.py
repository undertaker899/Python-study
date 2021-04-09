class BoardException(Exception):  # Creating exception classes
    pass  # Not for user


class BoardOutException(BoardException):
    def __str__(self):
        return 'You are trying to move out of border'


class BoardUsedException(BoardException):
    def __str__(self):
        return 'You are repeating move'


class BoardWrongShipException(BoardException):
    pass  # Not for user
