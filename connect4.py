import math
from typing import List

import numpy as np

from constants import HUMAN, CPU, TASK_DEPTH, SEARCH_DEPTH
from Board import Board
from Task import Task
from utils import input_column, get_opponent, Result


def generate_tasks(board: Board):
    cols = board.cols
    curr_player = CPU

    tasks = [Task(0, curr_player, board)]

    for level in range(TASK_DEPTH):
        level_tasks = []

        for idx, task in enumerate(tasks):
            for col in range(cols):
                task_id = idx * 7 + col
                new_board = task.board.copy()
                succ = new_board.move(col, curr_player)
                if not succ:
                    continue
                level_tasks.append(Task(task_id, get_opponent(curr_player), new_board))

        tasks = level_tasks
        curr_player = HUMAN if curr_player == CPU else CPU

    return tasks


def process_task(task: Task) -> Result:
    max_depth = SEARCH_DEPTH
    task_col = task.id % task.board.cols

    def dfs(board: Board, curr_col: int, depth: int, curr_player: int) -> float:
        if board.game_over(curr_col):
            if board.find_last_player(curr_col) == CPU:
                return 1.0
            else:
                return -1.0

        if depth == 0:
            return 0.0

        total_score = 0
        num_moves = 0

        for col in range(board.cols):
            new_board = board.copy()
            succ = new_board.move(col, curr_player)
            if not succ:
                continue
            score = dfs(new_board, col, depth - 1, get_opponent(curr_player))
            total_score += score
            num_moves += 1

        return total_score / num_moves if num_moves else 0

    avg_score = dfs(task.board, task_col, max_depth, task.next_player)

    result = Result(task.id, avg_score)

    return result


def find_max(task_results: List[Result]) -> int:
    max_score = -math.inf
    best_move = None
    for task in task_results:
        if task.score > max_score:
            max_score = task.score
            best_move = task.id

    return best_move


def compute_best_move(task_results: List[Result]) -> int:
    for _ in reversed(range(1, TASK_DEPTH)):
        new_task_results = []
        for idx, j in enumerate(range(0, len(task_results), 7)):
            new_task = task_results[j: j + 7]

            new_task_scores = [task.score for task in new_task]

            new_task_results.append(Result(idx, np.mean(new_task_scores)))

        task_results = new_task_results

    return find_max(task_results)


def human_play(board: Board) -> int:
    col_move = input_column(board)
    succ = board.move(col_move, HUMAN)
    while not succ:
        print("Invalid value. Enter again: ")
        col_move = input_column(board)
        succ = board.move(col_move, HUMAN)

    return col_move
