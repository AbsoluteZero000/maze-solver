from graphics import Window, Line, Point, Cell


def main():
    window = Window(600, 600)
    cell = Cell(window)
    cell2 = Cell(window)
    cell3 = Cell(window)
    cell.has_right_wall = False
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell3.has_top_wall = False
    cell.draw(100, 100, 200, 200)
    cell2.draw(200, 100, 300, 200)
    cell3.draw(200,200, 300, 300)
    cell.draw_move(cell2, True)
    cell2.draw_move(cell3, False)

    window.wait_for_close()


if __name__ == "__main__":
    main()
