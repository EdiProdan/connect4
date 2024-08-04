from constants import HUMAN, CPU


class Result:
    def __init__(self, id, score):
        self.id = id
        self.score = score

    def __str__(self):
        return f"Task {self.id}, score {self.score}"


def input_column(board):
    col_move = input()
    while not (col_move.isdigit() and len(col_move) < board.cols):
        print("Invalid value. Enter again: ")
        col_move = input()
    return int(col_move)


def get_opponent(curr_player):
    return HUMAN if curr_player == CPU else CPU
