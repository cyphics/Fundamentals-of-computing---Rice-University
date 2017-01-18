import unittest
import poc_fifteen as fifteen
import poc_fifteen_gui as gui


class testMove(unittest.TestCase):
    def test_move_left_to_target_1(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 9, 17], [11, 12, 10, 13, 14], [15, 16, 0, 18, 19], [20, 21, 22, 23, 24]]
        game = fifteen.Puzzle(5, 5, board)
        target_position = (0, 0)
        target_value = game.get_number(target_position[0], target_position[1])
        game.move_left_to_target(target_position[0], target_position[1])
        current_zero = game.current_position(0, 0)
        self.assertEqual(game.get_number(current_zero[0], current_zero[1] + 1), target_value)

    def test_move_left_to_target_2(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 9, 17], [11, 12, 10, 13, 14], [15, 16, 0, 18, 19], [20, 21, 22, 23, 24]]
        game = fifteen.Puzzle(5, 5, board)
        target_position = (2, 3)
        target_value = game.get_number(target_position[0], target_position[1])
        game.move_left_to_target(target_position[0], target_position[1])
        current_zero = game.current_position(0, 0)
        self.assertEqual(game.get_number(current_zero[0], current_zero[1] + 1), target_value)

    def test_move_left_to_target_3(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 9, 17], [11, 0, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        target_position = (1, 3)
        target_value = game.get_number(target_position[0], target_position[1])
        game.move_left_to_target(target_position[0], target_position[1])
        current_zero = game.current_position(0, 0)
        self.assertEqual(game.get_number(current_zero[0], current_zero[1] + 1), target_value)

    def test_move_left_to_target_4(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 9, 17], [11, 12, 0, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        target_position = (2, 1)
        target_value = game.get_number(target_position[0], target_position[1])
        game.move_left_to_target(target_position[0], target_position[1])
        current_zero = game.current_position(0, 0)
        self.assertEqual(game.get_number(current_zero[0], current_zero[1] + 1), target_value)

    def test_move_left_to_target_5(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 9, 17], [11, 0, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        target_position = (2, 0)
        target_value = game.get_number(target_position[0], target_position[1])
        game.move_left_to_target(target_position[0], target_position[1])
        current_zero = game.current_position(0, 0)
        self.assertEqual(game.get_number(current_zero[0], current_zero[1] + 1), target_value)

    def test_move_left_to_target_6(self):
        board = [[2, 3], [1, 4], [0, 5], [6, 7]]
        game = fifteen.Puzzle(4, 2, board)
        target_position = (2, 1)
        target_value = game.get_number(target_position[0], target_position[1])
        game.move_left_to_target(target_position[0], target_position[1])
        current_zero = game.current_position(0, 0)
        self.assertEqual(game.get_number(current_zero[0], current_zero[1] + 1), target_value)

    def test_move_left_to_target_7(self):
        board = [[2, 3], [1, 4], [0, 5], [6, 7]]
        game = fifteen.Puzzle(4, 2, board)
        target_position = (0, 1)
        target_value = game.get_number(target_position[0], target_position[1])
        game.move_left_to_target(target_position[0], target_position[1])
        current_zero = game.current_position(0, 0)
        self.assertEqual(game.get_number(current_zero[0], current_zero[1] + 1), target_value)

    def test_move_left_to_target_10(self):
        board = [[2, 3, 1, 4, 5], [7, 6, 8, 9, 17], [11, 12, 10, 13, 14], [15, 16, 0, 18, 19], [20, 21, 22, 23, 24]]
        game = fifteen.Puzzle(5, 5, board)
        target_position = (1, 4)
        target_value = game.get_number(target_position[0], target_position[1])
        game.move_left_to_target(target_position[0], target_position[1])
        current_zero = game.current_position(0, 0)
        self.assertEqual(game.get_number(current_zero[0], current_zero[1] + 1), target_value)

    def test_move_left_to_target_11(self):
        board = [[1, 3, 17, 4, 5], [7, 6, 8, 9, 1], [11, 12, 10, 13, 14], [12, 13, 0, 18, 19], [20, 21, 22, 23, 24]]
        game = fifteen.Puzzle(5, 5, board)
        target_position = (0, 2)
        target_value = game.get_number(target_position[0], target_position[1])
        game.move_left_to_target(target_position[0], target_position[1])
        current_zero = game.current_position(0, 0)
        self.assertEqual(game.get_number(current_zero[0], current_zero[1] + 1), target_value)

    def test_move_left_to_target_12(self):
        board = [[6, 9, 5, 4, 1], [3, 2, 8, 7, 0], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
        game = fifteen.Puzzle(4, 5, board)
        target_position = (0, 1)
        target_value = game.get_number(target_position[0], target_position[1])
        game.move_left_to_target(target_position[0], target_position[1])
        current_zero = game.current_position(0, 0)
        self.assertEqual(game.get_number(current_zero[0], current_zero[1] + 1), target_value)

    def test_move_left_to_target_13(self):
        board = [[6, 2, 1], [0, 5, 4], [3, 7, 8]]
        game = fifteen.Puzzle(3, 3, board)
        target_position = (0, 0)
        target_value = game.get_number(target_position[0], target_position[1])
        game.move_left_to_target(target_position[0], target_position[1])
        current_zero = game.current_position(0, 0)
        self.assertEqual(game.get_number(current_zero[0], current_zero[1] + 1), target_value)

    def test_move_target_to_col_1(self):
        board = [[2, 3, 1, 0, 5], [7, 6, 8, 9, 17], [11, 4, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        # game.update_puzzle("rdllu")
        game.move_target_to_col(0, "down")
        self.assertEqual(game.get_number(0, 0), 5)

    def test_move_target_to_col_2(self):
        board = [[0, 3, 1, 9, 5], [7, 6, 8, 9, 17], [11, 4, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        game.move_target_to_col(0, "down")
        self.assertEqual(game.get_number(0, 0), 3)

    def test_move_target_to_col_3(self):
        board = [[0, 2, 1, 5, 5], [7, 6, 8, 9, 17], [11, 4, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        game.move_target_to_col(0, "down")
        self.assertEqual(game.get_number(0, 0), 2)

    def test_move_target_to_col_4(self):
        board = [[3, 2, 1, 5, 5], [7, 4, 8, 0, 17], [11, 4, 12, 13, 14]]
        game = fifteen.Puzzle(3, 5, board)
        game.move_target_to_col(0, "down")
        self.assertEqual(game.get_number(1, 0), 17)

    def test_move_target_to_col_5(self):
        board = [[3, 2, 1, 5, 5], [7, 4, 8, 9, 17], [11, 4, 12, 0, 14]]
        game = fifteen.Puzzle(3, 5, board)
        game.move_target_to_col(0, "up")
        self.assertEqual(game.get_number(2, 0), 14)

    def test_move_target_to_row_1(self):
        board = [[3, 0, 1, 5, 5], [7, 4, 8, 9, 17], [11, 4, 12, 4, 14]]
        game = fifteen.Puzzle(3, 5, board)
        game.move_target_to_row(2)
        self.assertEqual(game.get_number(2, 2), 1)

    def test_move_target_to_row_2(self):
        board = [[3, 0, 1, 5, 5], [7, 4, 8, 9, 17], [11, 4, 12, 4, 14]]
        game = fifteen.Puzzle(3, 5, board)
        game.move_target_to_row(0)
        self.assertEqual(game.get_number(0, 2), 1)




def main():
    unittest.main()

if __name__ == '__main__':
    main()
