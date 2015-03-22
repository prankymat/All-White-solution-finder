queue = []
marked = []
BOARD = [(0,0), (1,0), (2,0), (3,0), (0,1), (1,1), (2,1), (3,1)]

DIRECTION = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def find_neighbour_and_mark_self(coordinate):
    neighbours = []

    for d in DIRECTION:
        new_col = coordinate[0] + d[0]
        new_row = coordinate[1] + d[1]
        new_coordinate = (new_col, new_row)
        if new_coordinate in BOARD:
            neighbours.append(new_coordinate)

    if len(neighbours) == 2 and coordinate not in marked:
        marked.append(coordinate)
        print("Marked:", coordinate)

    print("done finding", coordinate, "neighbour:", neighbours)
    return neighbours


while True:
    for coordinate in BOARD:
        neighbours = find_neighbour_and_mark_self(coordinate)

        for neighbour in neighbours:
            queue.append(neighbour)
    break

print(len(marked))