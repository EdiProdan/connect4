from copy import deepcopy
from typing import List

import numpy as np


class Board:
    def __init__(self, rows: int = 6, cols: int = 7):
        self.rows = rows
        self.cols = cols
        self.board = self.initialize_board()

    def __str__(self) -> str:

        sb = "  " + "   ".join(str(i) for i in range(len(self.board[0]))) + "\n"
        row_separator = '+' + '+'.join('---' for _ in range(len(self.board[0]))) + '+\n'

        def item_to_char(item):
            if item == 0:
                return ' '
            elif item == 1:
                return 'X'
            elif item == 2:
                return 'O'
            else:
                return ' '

        sb += row_separator
        for row in self.board:
            sb += '| '
            sb += ' | '.join(item_to_char(item) for item in row)
            sb += ' |\n'
            sb += row_separator

        return sb

    def initialize_board(self) -> List[List]:
        return np.zeros((self.rows, self.cols), dtype=int).tolist()

    def is_legal(self, col_move: int) -> bool:
        if not (0 <= col_move < self.cols):
            return False
        return True

    # CPU 1, human 2
    def move(self, col_move: int, player: int) -> bool:
        if not self.is_legal(col_move):
            return False

        for row in range(len(self.board) - 1, -1, -1):
            if self.board[row][col_move] == 0:
                self.board[row][col_move] = player
                break

        return True

    def undo(self, col_undo: int) -> bool:
        if not self.is_legal(col_undo):
            return False

        found = False
        for row in range(len(self.board)):
            if self.board[row][col_undo] != 0:
                self.board[row][col_undo] = 0
                found = True
                break

        return found

    def copy(self):
        return deepcopy(self)

    def find_last_player(self, last_col) -> int:
        for i in range(self.rows):
            player = self.board[i][last_col]
            if player != 0:
                return player

    def __check_direction(self, board, start_row, start_col, dr, dc, player):
        count = 0
        r, c = start_row, start_col
        while 0 <= r < self.rows and 0 <= c < self.cols and board[r, c] == player:
            count += 1
            r += dr
            c += dc
        return count

    def __check_win(self, board, row, col, player):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            count += self.__check_direction(board, row + dr, col + dc, dr, dc, player)
            count += self.__check_direction(board, row - dr, col - dc, -dr, -dc, player)
            if count >= 4:
                return True
        return False

    def game_over(self, last_col) -> bool:
        if last_col is None:
            return False

        for i in range(self.rows):
            if self.board[i][last_col] != 0:
                row = i
                break
        col = last_col
        self.board = np.array(self.board)
        player = self.board[row, col]
        if player == 0:
            return False

        return self.__check_win(self.board, row, col, player)
