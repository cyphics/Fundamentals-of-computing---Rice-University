"""
Test Suite for 2048
"""

import poc_simpletest

def run_suite(TwentyFortyEight):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # create a game
    game = TwentyFortyEight(5, 4)

    suite.run_test(game.get_grid_height(), game._grid_height, "Get grid height 1: ")
    suite.run_test(game.get_grid_width(), game._grid_width, "Get grid width 1: ")

    game.set_tile(0, 0, 8)
    game.set_tile(0, 1, 8)
    game.set_tile(0, 2, 8)
    game.set_tile(0, 3, 8)

    print(game)

    suite.run_test(game.get_tile(0, 0), 8, "Get tile 1: ")
    suite.run_test(game.get_tile(0, 1), 8, "Get tile 2: ")
    suite.run_test(game.get_tile(0, 2), 8, "Get tile 3: ")
    suite.run_test(game.get_tile(0, 3), 8, "Get tile 4: ")

    game.move(4)
    print(game._move_indices[4])
    print(game)

    suite.report_results()
