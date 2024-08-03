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
        self._reset_cells_visited()

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
        sleep(0.001)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows-1][self._num_cols-1].has_bottom_wall = False
        self._draw_cell(self._num_rows-1, self._num_cols-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))


            if(len(to_visit) == 0):
                self._draw_cell(i,j)
                return
            direction_index = random.randrange(len(to_visit))
            next_index = to_visit[direction_index]

            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_bfs(0,0)

    def _solve_dfs(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        sleep(0.01)
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_dfs(i - 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j], True)

        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_dfs(i + 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j], True)

        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_dfs(i, j - 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1], True)
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_dfs(i, j + 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], True)
        return False

    def _solve_bfs(self, i, j):
        to_visit = [(i,j)]

        while(to_visit):
            self._animate()
            sleep(0.01)
            i,  j = to_visit.pop(0)
            self._cells[i][j].visited = True

            if((i, j)== (self._num_rows -1, self._num_cols -1)):
                return True

            if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                to_visit.append((i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                to_visit.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                to_visit.append((i, j + 1))
