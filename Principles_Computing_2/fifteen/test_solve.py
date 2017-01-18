import unittest
import poc_fifteen as fifteen
# import poc_fifteen_gui as gui


class testSolve(unittest.TestCase):
    def test_solve_interior_tile_5(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 9, 17], [11, 0, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        position = (2, 1)
        game.solve_interior_tile(position[0], position[1])
        self.assertEqual(game.lower_row_invariant(position[0], position[1] - 1), True)

    def test_solve_interior_tile_6(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 9, 11], [17, 0, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        position = (2, 1)
        game.solve_interior_tile(position[0], position[1])
        self.assertEqual(game.lower_row_invariant(position[0], position[1] - 1), True)

    def test_solve_interior_tile_1(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 9, 17], [11, 12, 10, 13, 14], [15, 16, 0, 18, 19], [20, 21, 22, 23, 24]]
        game = fifteen.Puzzle(5, 5, board)
        target_position = (3, 2)
        game.solve_interior_tile(target_position[0], target_position[1])
        self.assertEqual(game.lower_row_invariant(target_position[0], target_position[1] - 1), True)

    def test_solve_interior_tile_2(self):
        board = [[17, 3, 1, 4, 5], [7, 6, 8, 9, 1], [11, 12, 10, 13, 14], [15, 16, 0, 18, 19], [20, 21, 22, 23, 24]]
        game = fifteen.Puzzle(5, 5, board)
        target_position = (3, 2)
        game.solve_interior_tile(target_position[0], target_position[1])
        self.assertEqual(game.lower_row_invariant(target_position[0], target_position[1] - 1), True)

    def test_solve_interior_tile_3(self):
        board = [[1, 3, 1, 4, 5], [7, 6, 8, 9, 1], [11, 12, 10, 13, 14], [15, 17, 0, 18, 19], [20, 21, 22, 23, 24]]
        game = fifteen.Puzzle(5, 5, board)
        target_position = (3, 2)
        game.solve_interior_tile(target_position[0], target_position[1])
        self.assertEqual(game.lower_row_invariant(target_position[0], target_position[1] - 1), True)

    def test_solve_interior_tile_4(self):
        board = [[1, 3, 1, 4, 5], [7, 6, 8, 9, 1], [11, 12, 10, 13, 14], [17, 13, 0, 18, 19], [20, 21, 22, 23, 24]]
        game = fifteen.Puzzle(5, 5, board)
        target_position = (3, 2)
        game.solve_interior_tile(target_position[0], target_position[1])
        self.assertEqual(game.lower_row_invariant(target_position[0], target_position[1] - 1), True)

    def test_solve_interior_tile_7(self):
        board = [[1, 3, 17, 4, 5], [7, 6, 8, 9, 1], [11, 12, 10, 13, 14], [12, 13, 0, 18, 19], [20, 21, 22, 23, 24]]
        game = fifteen.Puzzle(5, 5, board)
        target_position = (3, 2)
        moves = game.solve_interior_tile(target_position[0], target_position[1])
        game = fifteen.Puzzle(5, 5, board)
        game.update_puzzle(moves)
        self.assertEqual(game.lower_row_invariant(target_position[0], target_position[1] - 1), True)

    def test_solve_interior_tile_8(self):
        board = [[8, 7, 6], [5, 4, 3], [2, 1, 0]]
        game = fifteen.Puzzle(3, 3, board)
        game.solve_interior_tile(2, 2)

    def test_solve_col0_tile_1(self):
        board = [[1, 3], [2, 4], [0, 5], [6, 7]]
        game = fifteen.Puzzle(4, 2, board)
        target_position = (2, 0)
        game.solve_col0_tile(target_position[0])
        self.assertEqual(game.lower_row_invariant(1, 1), True)

    def test_solve_col0_tile_2(self):
        board = [[1, 3, 17, 4, 20], [7, 6, 8, 9, 1], [11, 12, 10, 13, 14], [12, 13, 10, 18, 19], [0, 21, 22, 23, 24]]
        game = fifteen.Puzzle(5, 5, board)
        target_position = (4, 0)
        game.solve_col0_tile(target_position[0])
        self.assertEqual(game.lower_row_invariant(3, 4), True)

    def test_solve_col0_tile_3(self):
        board = [[3, 2, 1], [5, 6, 4], [0, 7, 8]]
        game = fifteen.Puzzle(3, 3, board)
        game.solve_col0_tile(2)
        self.assertEqual(game.lower_row_invariant(1, 2), True)

    def test_solve_col0_tile_4(self):
        board = [[3, 2, 1], [6, 5, 4], [0, 7, 8]]
        game = fifteen.Puzzle(3, 3, board)
        game.solve_col0_tile(2)
        self.assertEqual(game.lower_row_invariant(1, 2), True)

    def test_solve_col0_tile_5(self):
        board = [[6, 2, 1], [3, 5, 4], [0, 7, 8]]
        game = fifteen.Puzzle(3, 3, board)
        game.solve_col0_tile(2)
        self.assertEqual(game.lower_row_invariant(1, 2), True)

    def test_solve_col0_tile_6(self):
        board = [[8, 2, 10, 9, 1], [7, 6, 5, 4, 3], [0, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_col0_tile(2)
        self.assertEqual(game.lower_row_invariant(1, 4), True)

    def test_solve_row1_1(self):
        board = [[9, 6, 5, 4, 1], [3, 2, 8, 7, 0], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row1_tile(4)
        self.assertEqual(game.row0_invariant(4), True)

    def test_solve_row1_2(self):
        board = [[6, 9, 5, 4, 1], [3, 2, 8, 7, 0], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row1_tile(4)
        self.assertEqual(game.row0_invariant(4), True)

    def test_solve_row1_3(self):
        board = [[6, 5, 9, 4, 1], [3, 2, 8, 7, 0], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row1_tile(4)
        self.assertEqual(game.row0_invariant(4), True)

    def test_solve_row1_4(self):
        board = [[6, 5, 4, 9, 1], [3, 2, 8, 7, 0], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row1_tile(4)
        self.assertEqual(game.row0_invariant(4), True)

    def test_solve_row1_5(self):
        board = [[6, 5, 4, 1, 9], [3, 2, 8, 7, 0], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row1_tile(4)
        self.assertEqual(game.row0_invariant(4), True)

    def test_solve_row1_6(self):
        board = [[6, 5, 4, 1, 3], [9, 2, 8, 7, 0], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row1_tile(4)
        self.assertEqual(game.row0_invariant(4), True)

    def test_solve_row1_7(self):
        board = [[6, 5, 4, 1, 3], [2, 9, 8, 7, 0], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row1_tile(4)
        self.assertEqual(game.row0_invariant(4), True)

    def test_solve_row1_8(self):
        board = [[6, 5, 4, 1, 3], [2, 7, 8, 9, 0], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row1_tile(4)
        self.assertEqual(game.row0_invariant(4), True)

    def test_solve_row1(self):
        board = [[7, 6, 5, 1, 4], [3, 2, 8, 0, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row1_tile(3)
        self.assertEqual(game.row0_invariant(3), True)

    def test_solve_row0_1(self):
        board = [[2, 3, 4, 1, 0], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row0_tile(4)
        self.assertEqual(game.row1_invariant(3), True)

    def test_solve_row0_2(self):
        board = [[2, 3, 3, 4, 0], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row0_tile(4)
        self.assertEqual(game.row1_invariant(3), True)

    def test_solve_row0_3(self):
        board = [[4, 3, 3, 2, 0], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row0_tile(4)
        self.assertEqual(game.row1_invariant(3), True)

    def test_solve_row0_4(self):
        board = [[1, 3, 2, 5, 0], [4, 8, 6, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row0_tile(4)
        self.assertEqual(game.row1_invariant(3), True)

    def test_solve_row0_4_1(self):
        board = [[1, 3, 2, 5, 0], [3, 8, 6, 4, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row0_tile(4)
        self.assertEqual(game.row1_invariant(3), True)

    def test_solve_row0_4_2(self):
        board = [[1, 3, 2, 5, 0], [7, 8, 6, 4, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row0_tile(4)
        self.assertEqual(game.row1_invariant(3), True)

    def test_solve_row0_4_3(self):
        board = [[2, 3, 4, 1, 0], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row0_tile(4)
        self.assertEqual(game.row1_invariant(3), True)

    def test_solve_row0_5(self):
        board = [[1, 7, 2, 0, 4], [5, 6, 3, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        game.solve_row0_tile(3)
        self.assertEqual(game.row1_invariant(2), True)

    def test_solve_row0_6(self):
        board = [[3, 7, 2, 0, 4], [5, 6, 1, 8, 9]]
        game = fifteen.Puzzle(2, 5, board)
        game.solve_row0_tile(3)
        self.assertEqual(game.row1_invariant(2), True)

    def test_solve_row0_7(self):
        board = [[2, 3, 0, 3, 4], [1, 6, 7, 8, 9]]
        game = fifteen.Puzzle(2, 5, board)
        result = game.solve_row0_tile(2)
        game = fifteen.Puzzle(2, 5, board)
        game.update_puzzle(result)
        self.assertEqual(game.row1_invariant(1), True)

    def test_solve_row0_8(self):
        board = [[2, 3, 0, 3, 4], [1, 6, 7, 8, 9]]
        game = fifteen.Puzzle(2, 5, board)
        result = game.solve_row0_tile(2)
        game = fifteen.Puzzle(2, 5, board)
        game.update_puzzle(result)
        self.assertEqual(game.row1_invariant(1), True)

    def test_solve_2x2_1(self):
        board = [[3, 2], [1, 0]]
        game = fifteen.Puzzle(2, 2, board)
        game.solve_2x2()

    def test_solve_2x2_3(self):
        board = [[4, 3, 2], [1, 0, 5], [6, 7, 8]]
        game = fifteen.Puzzle(3, 3, board)
        game.solve_2x2()

    def test_solve_puzzle_1(self):
        board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        initial_moves = "drdludrulurdluddrruldrluurdll"
        game = fifteen.Puzzle(3, 3, board)
        game.update_puzzle(initial_moves)
        print game
        game.solve_puzzle()
        print game

    def test_solve_puzzle_2(self):
        board = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
        initial_moves = "drdludrulurdluddrruldrluurdll"
        game = fifteen.Puzzle(4, 3, board)
        game.update_puzzle(initial_moves)
        print game
        game.solve_puzzle()
        print game

    def test_solve_puzzle_3(self):
        board = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
        initial_moves = "drdludrulurdludddrruldrluurdll"
        game = fifteen.Puzzle(4, 3, board)
        game.update_puzzle(initial_moves)
        print game
        game.solve_puzzle()
        print game

    def test_solve_puzzle_4(self):
        board = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]]
        initial_moves = "drdludrulurdluddrruldrluurdll"
        game = fifteen.Puzzle(3, 4, board)
        game.update_puzzle(initial_moves)
        print game
        game.solve_puzzle()
        print game

    def test_solve_puzzle_5(self):
        board = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        initial_moves = "drdludrulurdluddrruldrluurdll"
        game = fifteen.Puzzle(4, 4, board)
        game.update_puzzle(initial_moves)
        print game
        game.solve_puzzle()
        print game

    def test_solve_puzzle_6(self):
        board = [[8, 7, 6], [5, 4, 3], [2, 1, 0]]
        game = fifteen.Puzzle(3, 3, board)
        print game
        solution = game.solve_puzzle()
        game = fifteen.Puzzle(3, 3, board)
        game.update_puzzle(solution)
        print game


def main():
    unittest.main()

if __name__ == '__main__':
    main()
