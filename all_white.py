from operator import itemgetter
import string

DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

class AllWhiteCalc:
    def __init__(self):
        self.marked = []
        self.board = []
        self.symbol = dict()

    def find_neighbours(self, coordinate):
        neighbours = []

        for d in DIRECTIONS:
            new_col = coordinate[0] + d[0]
            new_row = coordinate[1] + d[1]
            new_coordinate = (new_col, new_row)
            if new_coordinate in self.board \
                    and new_coordinate not in self.marked:
                neighbours.append(new_coordinate)

        return neighbours

    def game_ended(self):
        return len(self.marked) == len(self.board)

    def mark_coordinate(self, coordinate):
        if coordinate not in self.marked:
            self.marked.append(coordinate)

    @classmethod
    def sort_board(cls, board):
        return sorted(board, key=itemgetter(1, 0)) or []

    def calc_moves(self, board):

        self.board = self.sort_board(board)
        self.marked = []
        # count = 0
        # for c in self.board:
        #     self.symbol[c] = string.ascii_letters[count]
        #     count += 1

        while not self.game_ended():
            for grid in self.board:
                neighbours = self.find_neighbours(grid)
                if len(neighbours) == 2:
                    self.mark_coordinate(grid)
                elif len(neighbours) == 1:
                    if len(self.find_neighbours(neighbours[0])) == 1:
                        self.mark_coordinate(neighbours[0])
                elif len(neighbours) == 0:
                    self.mark_coordinate(grid)
                elif len(neighbours) == 4:
                    self.mark_coordinate(grid)

        # print("marked:", [self.symbol[x] for x in self.marked])
        return self.marked