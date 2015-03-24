function initSolver() {

  _ = require("underscore");

  DIRECTIONS = [
    [0, -1],
    [-1, 0],
    [0, 1],
    [1, 0]
  ];

  function contains(coordinate, board) {
    return _.where(board, coordinate).length > 0
  };

  function find_neighbour(coordinate, board, marked) {
    neighbours = [];
    DIRECTIONS.forEach(function(d) {
      new_col = coordinate[0] + d[0];
      new_row = coordinate[1] + d[1];
      new_coordinate = [new_col, new_row]
      if (
        contains(new_coordinate, board) &&
        !contains(new_coordinate, marked)
      ) {
        neighbours.push(new_coordinate)
      }
    });
    return neighbours;
  };

  function game_ended(marked, board) {
    return marked.length == board.length;
  };

  function mark_coordinate(coordinate, marked) {
    if (!contains(coordinate, marked)) {
      marked.push(coordinate);
    }
  };

  this.calc_move = function(board) {

    var marked = [];


    board.sort(function(a, b) {
      if (a[1] === b[1]) {
        return 0;
      } else {
        return (a[1] < b[1]) ? -1 : 1;
      }
    });

    while (!game_ended(marked, board)) {

      board.forEach(function(coordinate) {
        neighbours = find_neighbour(coordinate, board, marked);
        count = neighbours.length;
        if (count == 2 || count == 4 || count == 0) {
          if (count == 0) {}
          mark_coordinate(coordinate, marked);
        } else if (count == 1) {
          if (find_neighbour(neighbours[0], board, marked).length == 1) {
            mark_coordinate(coordinate, marked);
          }
        }
      })
    }
    return marked;
  };

  return this;
};

/*
solver = new initSolver();

board = [
  [0, 1],
  [0, 0],
  [1, 1],
  [2, 0],
  [2, 1]
];

console.log(solver.calc_move(board))
*/