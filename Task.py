from Board import Board


class Task:

    def __init__(self, id: int, next_player: int, board: Board):
        self.id = id
        self.next_player = next_player
        self.board = board

    def __str__(self):
        return f"Task(id={self.id}, next_player={self.next_player}, board=\n{self.board})"

