_ = require('underscore')

DIRECTIONS = [
  [0, -1],
  [-1, 0],
  [0, 1],
  [1, 0]
];

marked = [];

function contains(coordinate, board) {
  return _.where(board, coordinate).length > 0
};

function find_neighbour(coordinate, board) {
  neighbours = [];
  _.each(DIRECTIONS, function(d) {
    new_col = coordinate[0] + d[0];
    new_row = coordinate[1] + d[1];
    new_coordinate = [new_col, new_row]
    if (
      (contains(new_coordinate, board)) &&
      !(contains(new_coordinate, marked))
    ) {
      neighbours.push(new_coordinate)
    }
  });
  return neighbours;
};

function game_ended(marked, board) {
  return marked.length == board.length
};

function mark_coordinate(coordinate) {
  if (!contains(coordinate, marked)) {
    marked.push(coordinate);
  }
};

function calc_moves(board) {
  while (!game_ended(marked, board)) {
    _.each(board, function(coordinate) {
      neighbours = find_neighbour(coordinate);
      count = neighbours.length;
      if (count == 2 || count == 4 || count == 0) {
        mark_coordinate(coordinate);
      } else if (count == 1) {
        if (find_neighbour(neighbours[0]).length == 1) {
          mark_coordinate(coordinate)
        }
      }
    })
  }
  console.log(marked);
  return marked;
};

function sortBoard(a, b) {
  if (a[1] === b[1]) {
    return 0;
  } else {
    return (a[1] < b[1]) ? -1 : 1;
  }
};

board = [
  [0, 1],
  [0, 0],
  [1, 1],
  [2, 0],
  [2, 1]
]

board.sort(sortBoard);

calc_moves(board);