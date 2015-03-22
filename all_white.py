DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


class AllWhiteCalc:
    def __init__(self, board):
        self.marked = []
        self.board = board

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

    def r(self, c):
        neighbours = self.find_neighbours(c)
        if len(neighbours) == 2 and c not in self.marked:
            self.marked.append(c)
        for n in neighbours:
            self.r(n)

    def calc_moves(self):
        self.r(self.board[0])
        self.marked.extend(list(set(self.board).difference(self.marked)))
        return self.marked