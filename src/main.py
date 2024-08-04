import threading
from maze import Maze
from graphics import Window
from time import sleep
from random import randint
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
    seed = randint(0, 10000)
    dfs_thread = threading.Thread(target=run_dfs_solver, args=(seed,))
    bfs_thread = threading.Thread(target=run_bfs_solver, args=(seed,))

    dfs_thread.start()
    bfs_thread.start()

    dfs_thread.join()
    bfs_thread.join()


if __name__ == "__main__":
    main()
