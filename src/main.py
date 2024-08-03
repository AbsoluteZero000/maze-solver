from graphics import Window, Line, Point, Cell
from maze import Maze

def main():
    maze = Maze(100, 100, 20, 20, 30, 30, Window(800, 800))
    maze.solve()
if __name__ == "__main__":
    main()
