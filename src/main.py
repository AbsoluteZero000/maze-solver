from graphics import Window, Line, Point, Cell
from maze import Maze

def main():
    maze = Maze(100, 100, 20, 20, 20, 20, Window(800, 800))
    maze._break_entrance_and_exit()
    maze
if __name__ == "__main__":
    main()
