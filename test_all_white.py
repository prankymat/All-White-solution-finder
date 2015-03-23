import unittest, random
from operator import itemgetter
from all_white import AllWhiteCalc

# Unsorted test boards
UNSORTED_BOARD = [(0, 0), (0, 1), (2, 1), (1, 1), (2, 0), (2, 2)]
CROSS_BOARD = [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]

# Sorted test boards
SORTED_BOARD = [(0, 0), (2, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
NINE_BY_NINE_BOARD = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]

# Solutions
CROSS_BOARD_SOLUTION = [(1, 1), (2, 1), (1, 2), (1, 0), (0, 1)]
SORTED_BOARD_SOLUTION = [(0, 1), (0, 0), (1, 1), (2, 1), (2, 2), (2, 0)]
NINE_BY_NINE_BOARD_SOLUTION = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (2, 2), (2, 0), (0, 2)]



class AllWhiteTest(unittest.TestCase):
    def setUp(self):
        self.logic = AllWhiteCalc()

    def tearDown(self):
        self.logic.board = []
        self.logic.marked = []

    def test_sort_board(self):
        result = self.logic.sort_board(UNSORTED_BOARD)
        # result = sorted(UNSORTED_BOARD, key=itemgetter(1, 0))
        self.assertListEqual(result, SORTED_BOARD)

    def test_mark_coordinate(self):
        points = [(0, 0), (1, 0), (0, 0)]
        for point in points:
            self.logic.mark_coordinate(point)
        self.assertListEqual(self.logic.marked, [(0, 0), (1, 0)])

    def test_find_neighbours(self):
        boards = [CROSS_BOARD, SORTED_BOARD]
        boards_counts = ([1, 1, 4, 1, 1], [1, 1, 2, 2, 3, 1])
        for board, counts in zip(boards, boards_counts):
            self.logic.board = board
            for (coordinate, count) in zip(board, counts):
                result = self.logic.find_neighbours(coordinate)
                self.assertEqual(len(result), count)

    def test_game_ended(self):
        self.logic.board = SORTED_BOARD[:]
        self.logic.marked = []
        self.assertFalse(self.logic.game_ended())

    def test_calc_moves(self):
        boards = [CROSS_BOARD, UNSORTED_BOARD, NINE_BY_NINE_BOARD]
        solutions = [CROSS_BOARD_SOLUTION, SORTED_BOARD_SOLUTION, NINE_BY_NINE_BOARD_SOLUTION]

        for (board, solution) in zip(boards, solutions):
            result = self.logic.calc_moves(board)
            self.assertEqual(result, solution)