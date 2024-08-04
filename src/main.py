import threading
from maze import Maze
from graphics import Window
from time import sleep
from random import randint
import sys

def run_dfs_solver(seed):
    maze1 = Maze(100, 100, 20, 20, 30, 30, Window(800, 800, "DFS Maze Solver"), seed)
    maze1._solve_dfs(0, 0)
    sleep(100)
    maze1._win.wait_for_close()


def run_bfs_solver(seed):
    maze2 = Maze(100, 100, 20, 20, 30, 30, Window(800, 800, "BFS Maze Solver"), seed)
    maze2._solve_bfs(0, 0)
    sleep(100)
    maze2._win.wait_for_close()



def main():
    dfs = True
    bfs = True
    if len(sys.argv) > 1:
        if "-b" in sys.argv and "-d" in sys.argv:
            pass
        elif "-b" in sys.argv:
            dfs = False
        elif "-d" in sys.argv:
            bfs = False
        elif "-h" in sys.argv:
            print("Usage: python3 main.py [-b] [-d] [-h]")
            print("-b: run bfs solver")
            print("-d: run dfs solver")
            print("-b -d: run both bfs and dfs solver")
            print("-h: print this help message")
            exit(0)
        else:
            print("Invalid argument please use -h to get the arugments")


    seed = randint(0, 10000)
    dfs_thread = threading.Thread(target=run_dfs_solver, args=(seed,))
    bfs_thread = threading.Thread(target=run_bfs_solver, args=(seed,))

    if dfs:
        dfs_thread.start()
    if bfs:
        bfs_thread.start()

    if dfs:
        dfs_thread.join()
    if bfs:
        bfs_thread.join()


if __name__ == "__main__":
    main()
