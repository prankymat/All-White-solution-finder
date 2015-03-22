queue = []
marked = []
# BOARD = [(0,0), (1,0), (2,0), (3,0), (0,1), (1,1), (2,1), (3,1)]
# BOARD = [(0,1),(1,0),(1,1),(2,0),(2,1),(3,0),(3,1),(4,1),(5,1)]
# BOARD = [(0,0),(1,0),(2,0), (0,1),(1,1),(2,1), (0,2),(1,2),(2,2)]

BOARD = []
DIRECTION = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def find_neighbours(coordinate):
    neighbours = []

    for d in DIRECTION:
        new_col = coordinate[0] + d[0]
        new_row = coordinate[1] + d[1]
        new_coordinate = (new_col, new_row)
        if new_coordinate in BOARD and new_coordinate not in marked:
            neighbours.append(new_coordinate)

    return neighbours

def game_ended():
    return len(marked) == len(BOARD)

def r(c):
    neighbours = find_neighbours(c)
    if len(neighbours) == 2 and c not in marked:
        marked.append(c)
    for n in neighbours:
        r(n)

def calc_moves(board):
    r(board[0])
    marked.extend(list(set(board).difference(marked)))
    return marked