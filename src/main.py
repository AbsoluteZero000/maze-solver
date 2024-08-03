import threading
from maze import Maze
from graphics import Window

def run_dfs_solver():
    maze1 = Maze(100, 100, 20, 20, 30, 30, Window(800, 800, "DFS Maze Solver"), 2020)
    maze1._solve_dfs(0, 0)
    maze1._win.wait_for_close()


def run_bfs_solver():
    maze2 = Maze(100, 100, 20, 20, 30, 30, Window(800, 800, "BFS Maze Solver"), 2020)
    maze2._solve_bfs(0, 0)
    maze2._win.wait_for_close()


def main():
    dfs_thread = threading.Thread(target=run_dfs_solver)
    bfs_thread = threading.Thread(target=run_bfs_solver)

    dfs_thread.start()
    bfs_thread.start()

    dfs_thread.join()
    bfs_thread.join()


if __name__ == "__main__":
    main()
