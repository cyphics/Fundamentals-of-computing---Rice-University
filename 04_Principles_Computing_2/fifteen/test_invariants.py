import unittest
import poc_fifteen as fifteen
import poc_fifteen_gui as gui


class testsLowerRowInvariant(unittest.TestCase):

    def test_lower_row_invariant_zero_position_1(self):
        board = [[1, 0], [2, 3]]
        game = fifteen.Puzzle(2, 2, board)
        self.assertEqual(game.lower_row_invariant(0, 1), True)

    def test_lower_row_invariant_zero_position_2(self):
        board = [[0, 1], [2, 3]]
        game = fifteen.Puzzle(2, 2, board)
        self.assertEqual(game.lower_row_invariant(0, 1), False)

    def test_lower_row_invariant_below_rows_1(self):
        board = [[2], [1], [0], [3], [4], [5], [6], [7]]
        game = fifteen.Puzzle(8, 1, board)
        self.assertEqual(game.lower_row_invariant(2, 0), True)

    def test_lower_row_invariant_below_rows_2(self):
        board = [[2], [1], [0], [3], [4], [5], [7], [6]]
        game = fifteen.Puzzle(8, 1, board)
        self.assertEqual(game.lower_row_invariant(2, 0), False)

    def test_lower_row_invariant_current_col_1(self):
        board = [[2, 1, 0, 3, 4, 5, 6, 7]]
        game = fifteen.Puzzle(1, 8, board)
        self.assertEqual(game.lower_row_invariant(0, 2), True)

    def test_lower_row_invariant_current_col_2(self):
        board = [[2, 1, 0, 3, 4, 5, 7, 6]]
        game = fifteen.Puzzle(1, 8, board)
        self.assertEqual(game.lower_row_invariant(0, 2), False)

    def test_lower_row_invariant_final_1(self):
        board = [[2, 1, 0], [5, 4, 0], [6, 7, 8]]
        game = fifteen.Puzzle(3, 3, board)
        self.assertEqual(game.lower_row_invariant(1, 2), True)

    def test_lower_row_invariant_final_2(self):
        board = [[2, 3, 1], [5, 4, 0], [6, 7, 8], [10, 9, 11]]
        game = fifteen.Puzzle(4, 3, board)
        self.assertEqual(game.lower_row_invariant(1, 2), False)

    def test_lower_row_invariant_final_3(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 9, 10], [11, 12, 0, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
        game = fifteen.Puzzle(5, 5, board)
        self.assertEqual(game.lower_row_invariant(2, 2), True)

    def test_lower_row_invariant_final_4(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 9, 10], [11, 0, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
        game = fifteen.Puzzle(5, 5, board)
        self.assertEqual(game.lower_row_invariant(2, 2), False)

    def test_lower_row_invariant_final_5(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 9, 10], [11, 12, 0, 14, 13], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
        game = fifteen.Puzzle(5, 5, board)
        self.assertEqual(game.lower_row_invariant(2, 2), False)

    def test_lower_row_invariant_final_6(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 9, 10], [11, 12, 0, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 24, 23]]
        game = fifteen.Puzzle(5, 5, board)
        self.assertEqual(game.lower_row_invariant(2, 2), False)

    def test_lower_row_invariant_1(self):
        board = [[2, 3], [1, 4], [5, 7], [6, 8]]
        game = fifteen.Puzzle(4, 2, board)
        self.assertEqual(game.lower_row_invariant_partial(2, 1), False)

    def test_lower_row_invariant_2(self):
        board = [[2, 3], [1, 4], [5, 7], [6, 7]]
        game = fifteen.Puzzle(4, 2, board)
        self.assertEqual(game.lower_row_invariant_partial(2, 1), True)

    def test_lower_row_invariant_3(self):
        board = [[2, 3], [1, 4], [5, 7], [7, 8]]
        game = fifteen.Puzzle(4, 2, board)
        self.assertEqual(game.lower_row_invariant_partial(2, 1), False)

    def test_lower_row_invariant_4(self):
        board = [[2, 3], [1, 4], [0, 7], [8, 9]]
        game = fifteen.Puzzle(4, 2, board)
        self.assertEqual(game.lower_row_invariant_partial(2, 0), False)

    def test_lower_row_invariant_5(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 9, 17], [11, 0, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.lower_row_invariant_partial(2, 1), True)


class testsRowInvariant(unittest.TestCase):

    def test_row1_invariant_1(self):
        board = [[2, 3, 1, 5, 4], [7, 6, 8, 0, 9], [10, 11, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row1_invariant(3), True)

    def test_row1_invariant_1_1(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 0, 9], [10, 11, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row1_invariant(3), False)

    def test_row1_invariant_2(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 0, 9], [10, 11, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row1_invariant(4), False)

    def test_row1_invariant_3(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 0, 9], [10, 11, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row1_invariant(2), False)

    def test_row1_invariant_4(self):
        board = [[2, 3, 1, 9, 4], [5, 6, 7, 8, 0], [10, 11, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row1_invariant(4), True)

    def test_row1_invariant_5(self):
        board = [[2, 3, 1, 4, 5], [5, 6, 7, 8, 0], [10, 11, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row1_invariant(4), True)

    def test_row1_invariant_6(self):
        board = [[5, 1, 2, 3, 4], [0, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row1_invariant(0), True)

    def test_row1_invariant_6_1(self):
        board = [[5, 2, 1, 3, 4], [0, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row1_invariant(0), False)

    def test_row1_invariant_7(self):
        board = [[2, 3, 1, 4, 9], [0, 6, 7, 8, 9], [10, 11, 12, 14, 13]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row1_invariant(0), False)

    def test_row1_invariant_8(self):
        board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        game = fifteen.Puzzle(3, 3, board)
        self.assertEqual(game.row1_invariant(0), False)

    def test_row1_invariant_9(self):
        board = [[3, 1, 2], [0, 4, 5], [6, 7, 8]]
        game = fifteen.Puzzle(3, 3, board)
        self.assertEqual(game.row1_invariant(0), True)

    def test_row0_invariant_1(self):
        board = [[2, 3, 1, 4, 0], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row0_invariant(4), True)

    def test_row0_invariant_2(self):
        board = [[2, 3, 1, 0, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row0_invariant(3), True)

    def test_row0_invariant_3(self):
        board = [[2, 3, 1, 0, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row0_invariant(2), False)

    def test_row0_invariant_4(self):
        board = [[2, 3, 1, 4, 0], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row0_invariant(4), True)

    def test_row0_invariant_5(self):
        board = [[2, 3, 1, 0, 4], [6, 7, 5, 8, 9], [10, 11, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row0_invariant(3), True)

    def test_row0_invariant_6(self):
        board = [[2, 3, 1, 0, 4], [6, 7, 5, 2, 9], [10, 11, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        self.assertEqual(game.row0_invariant(3), False)

    def test_row0_invariant_7(self):
        board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        game = fifteen.Puzzle(3, 3, board)
        self.assertEqual(game.row0_invariant(0), True)

    def test_row0_invariant_8(self):
        board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        game = fifteen.Puzzle(3, 3, board)
        self.assertEqual(game.row0_invariant(1), False)



def main():
    unittest.main()

if __name__ == '__main__':
    main()
