from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.running)

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed")

    def close(self):
        self.running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = window

    def draw(self, x1, y1, x2, y2, fill_color="black"):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if(self.has_top_wall):
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), fill_color)
        if(self.has_bottom_wall):
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), fill_color)
        if(self.has_left_wall):
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), fill_color)
        if(self.has_right_wall):
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), fill_color)


    def draw_move(self, to_cell, undo=False):
        cell_color = "black" if not undo else "red"
        self.__win.draw_line(Line(Point((self.__x1 + self.__x2)/2, (self.__y1 + self.__y2)/2), Point((to_cell.__x1 + to_cell.__x2)/2, (to_cell.__y1 + to_cell.__y2)/2)), cell_color)
