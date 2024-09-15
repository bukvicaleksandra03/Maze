import sys
import time
from bfs_maze import BFSMaze
from dfs_maze import DFSMaze
from greedy_bfs_maze import GreedyBFSMaze
from a_maze import AMaze

if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

m = AMaze(sys.argv[1])
# print("Maze:")
# m.print()
print("Solving...")

start = time.time()
m.solve()
end = time.time()

print(f"Time needed to find solution: {(end - start) * 1000}ms")
print("States Explored:", m.num_explored)
print("Solution:")
m.print()
m.output_image("maze.png", show_explored=True)
