from all_white import AllWhiteCalc
import tkinter

class Gui:
    BOARD_SIZE = 500
    DIMENSION = 10
    GRID_SIZE = BOARD_SIZE // DIMENSION

    def __init__(self, parent):
        # Setup GUI
        self.e = tkinter.Entry(parent)
        parent.title("All White! Solver")

        top_frame = tkinter.Frame(parent)
        top_frame.pack(side=tkinter.TOP)
        center_frame = tkinter.Frame(top_frame)
        center_frame.pack(side=tkinter.BOTTOM)
        bottom_frame = tkinter.Frame(parent)
        bottom_frame.pack(side=tkinter.BOTTOM)
        board_canvas = tkinter.Canvas(center_frame,
                                      width=Gui.BOARD_SIZE,
                                      height=Gui.BOARD_SIZE)

        self.board_canvas = board_canvas
        self.board = []

        start_simulation = tkinter.Button(bottom_frame, text="Start "
                                                             "simulation")
        start_simulation.bind("<Button-1>", self.start_simulation)
        start_simulation.pack()

        reset_board = tkinter.Button(bottom_frame, text="Reset board")
        reset_board.bind("<Button-1>", self.reset_board)
        reset_board.pack()

        self.draw_grids()

    def reset_board(self, event):
        self.board = []
        self.board_canvas.delete("all")
        self.draw_grids()

    def draw_grids(self):
        # Draw separation lines
        for i in range(1, Gui.DIMENSION):
            # Horizontal lines
            self.board_canvas.create_line(0,
                                          Gui.GRID_SIZE * i,
                                          Gui.BOARD_SIZE,
                                          Gui.GRID_SIZE * i)
            # Vertical lines
            self.board_canvas.create_line(Gui.GRID_SIZE * i,
                                          0,
                                          Gui.GRID_SIZE * i,
                                          Gui.BOARD_SIZE)
        self.board_canvas.bind("<Button-1>", self.toggle_grid)
        self.board_canvas.pack()


    def start_simulation(self, event):
        calculator = AllWhiteCalc()
        try:
            moves = calculator.calc_moves(self.board)
            print("Moves found:", moves)
        except ValueError:
            print("No solution found!")
        # for move in moves:


    @classmethod
    def yield_moves(cls, moves):
        for move in moves:
            yield move

    def mark_grid(self, coordinate):
        column = coordinate[0]
        row = coordinate[1]
        grid_start = (column * Gui.GRID_SIZE, row * Gui.GRID_SIZE)
        grid_end = (grid_start[0] + Gui.GRID_SIZE,
                    grid_start[1] + Gui.GRID_SIZE)

        color = "green"

        self.board_canvas.create_rectangle(grid_start[0],
                                           grid_start[1],
                                           grid_end[0],
                                           grid_end[1],
                                           fill=color,
                                           tags="mark")

    def clear_marks(self):
        self.board_canvas.find_withtag("mark")

    def toggle_grid(self, event):
        column = int(event.x * (Gui.DIMENSION/Gui.BOARD_SIZE))
        row = int(event.y * (Gui.DIMENSION/Gui.BOARD_SIZE))
        coordinate = (column, row)
        if coordinate in self.board:
            self.board.remove(coordinate)
            self.clear_grid(coordinate)
        else:
            self.board.append(coordinate)
            self.fill_grid(coordinate)

    def fill_grid(self, coordinate):
        column = coordinate[0]
        row = coordinate[1]
        grid_start = (column * Gui.GRID_SIZE, row * Gui.GRID_SIZE)
        grid_end = (grid_start[0] + Gui.GRID_SIZE,
                    grid_start[1] + Gui.GRID_SIZE)

        color = "red"

        self.board_canvas.create_rectangle(grid_start[0],
                                           grid_start[1],
                                           grid_end[0],
                                           grid_end[1],
                                           fill=color,
                                           tags=".".join(str(x)
                                                         for x in coordinate))

    def clear_grid(self, coordinate):
        self.board_canvas.delete(".".join(str(x)
                                          for x in coordinate))

def main():
    root = tkinter.Tk()
    Gui(root)
    root.mainloop()

if __name__ == '__main__':
    main()