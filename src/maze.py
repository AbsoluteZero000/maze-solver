from time import sleep
from graphics import Cell
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        if(seed):
            random.seed(seed)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
    def _create_cells(self):
        for i in range(self._num_rows):
            temp = []
            for j in range(self._num_cols):
                cell = Cell(self._win)
                temp.append(cell)
            self._cells.append(temp)

        for j in range(self._num_cols):
            for i in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        self._cells[i][j].draw(self._x1 + i * self._cell_size_x, self._y1 + j * self._cell_size_y, self._x1 + (i + 1) * self._cell_size_x, self._y1 + (j + 1) * self._cell_size_y)
        self._animate()

    def _animate(self):
        if(self._win == False):
            return
        self._win.redraw()
        sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows-1][self._num_cols-1].has_bottom_wall = False
        self._draw_cell(self._num_rows-1, self._num_cols-1)
        sleep(1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        coords = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
        while True:
            to_visit = []

            for coord in coords:
                if 0 < coord[0] < self._num_rows-1 and 0 < coord[1] < self._num_cols-1:
                    if not self._cells[coord[0]][coord[1]].visited:
                        to_visit.append(coord)

            if(len(to_visit) == 0):
                self._draw_cell(i,j)
                return
            choice = random.choice(to_visit)
            if(choice[1] == j-1):
                self._cells[i][j].has_left_wall = False
                self._cells[choice[0]][choice[1]].has_right_wall = False
            elif(choice[1] == j+1):
                self._cells[i][j].has_right_wall = False
                self._cells[choice[0]][choice[1]].has_left_wall = False
            elif(choice[0] == i-1):
                self._cells[i][j].has_top_wall = False
                self._cells[choice[0]][choice[1]].has_bottom_wall = False
            elif(choice[0] == i+1):
                self._cells[i][j].has_bottom_wall = False
                self._cells[choice[0]][choice[1]].has_top_wall = False

            self._break_walls_r(choice[0], choice[1])

    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False
