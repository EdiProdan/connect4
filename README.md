## Connect Four
This program is a parallel implementation of a Connect Four using Open MPI (Message Passing Interface) as part of a laboratory exercise in the course Parallel Programming.

### How It Works
1. Initialization:
- The master process initializes the tasks.
- Each task represents a different starting point in the game tree.
- Tasks are distributed to worker processes.
2. Task Distribution:
- The master sends the initial tasks to the worker processes.
- Each worker process performs a Depth-First Search (DFS) to explore the game tree.
3. Depth Calculation:
- The master sets an initial task depth (e.g., depth 2).
- Workers perform DFS with an additional search depth (e.g., depth 5), making the total depth 7.
4. Score Calculation:
- Each worker calculates scores for different possible moves.
- The best score from each worker is sent back to the master.
5. Best Move Selection:
- The master collects scores from all workers.
- The move with the highest score is selected as the CPU's move.

### Example Output
Below is an example output of the program, showing the CPU's turn and the calculated scores for each column.

```
Welcome fredyy

CPU's turn...
Column 0, score 0.007955868728165984
Column 1, score 0.014075767749832125
Column 2, score 0.020195666771498262
Column 3, score 0.026315565793164405
Column 4, score 0.020195666771498262
Column 5, score 0.014075767749832125
Column 6, score 0.007955868728165984

  0   1   2   3   4   5   6
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   | X |   |   |   |
+---+---+---+---+---+---+---+

fredyy's turn. Enter the column: 
2

  0   1   2   3   4   5   6
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   | O | X |   |   |   |
+---+---+---+---+---+---+---+

...

CPU's turn...
Column 0, score 0.24906289046230737
Column 1, score 0.19702674905864054
Column 2, score 0.27425647476816634
Column 3, score 0.2555737830325799
Column 4, score 0.2556077824715892
Column 5, score 1.0
Column 6, score 0.2838953157272905
  0   1   2   3   4   5   6
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   | O | O |   |   |
+---+---+---+---+---+---+---+
|   |   | O | X | X | X | X |
+---+---+---+---+---+---+---+

Game ended, CPU won


```