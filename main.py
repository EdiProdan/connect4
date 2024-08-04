import random
from mpi4py import MPI
from Board import Board
from connect4 import generate_tasks, process_task, compute_best_move, human_play
from constants import HUMAN, CPU
from time import time


if __name__ == "__main__":

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    board = Board()

    mpi_status = MPI.Status()

    col_move = None
    if rank == 0:
        print("Enter your nickname: ")
        nickname = input()
        curr_player = random.randint(1, 2)  # CPU 1, human 2

        while not board.game_over(col_move):
            if curr_player == HUMAN:  # human plays
                print(f"{nickname}'s turn. Enter the column: ")
                col_move = human_play(board)
                print(board)
                curr_player = CPU

            else:  # CPU plays
                print("CPU's turn...")
                start_time = time()
                tasks = generate_tasks(board)
                expected_tasks = len(tasks)
                task_results = []

                for worker in range(1, size):
                    task = tasks.pop(0)
                    comm.send(obj=task, dest=worker)

                while tasks:
                    result = comm.recv(source=MPI.ANY_SOURCE, status=mpi_status)
                    task_results.append(result)
                    task = tasks.pop(0)
                    comm.send(task, dest=mpi_status.source)

                while len(task_results) != expected_tasks:
                    result = comm.recv(source=MPI.ANY_SOURCE)
                    task_results.append(result)

                for tr in task_results:
                    print(tr)

                col_move = compute_best_move(task_results)
                board.move(col_move, curr_player)
                end = time() - start_time
                print(board)
                curr_player = HUMAN

    else:
        while True:
            task = comm.recv(source=0)
            result = process_task(task)
            comm.send(result, dest=0)

    print(f"Game ended, {nickname if board.find_last_player(col_move) == 2 else 'CPU'} won")
    MPI.Finalize()
