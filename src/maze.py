from time import sleep
from graphics import Cell
class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.__num_rows):
            temp = []
            for j in range(self.__num_cols):
                cell = Cell(self.__win)
                temp.append(cell)
            self.__cells.append(temp)

        for j in range(self.__num_cols):
            for i in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        self.__cells[i][j].draw(self.__x1 + i * self.__cell_size_x, self.__y1 + j * self.__cell_size_y, self.__x1 + (i + 1) * self.__cell_size_x, self.__y1 + (j + 1) * self.__cell_size_y)
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        sleep(0.01)
