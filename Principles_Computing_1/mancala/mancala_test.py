"""
Template for testing suite for Solitaire Mancala
"""

import poc_simpletest

def run_suite(SolitaireMancala):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # create a game
    config1 = [0, 1, 1, 1, 3, 5, 0]
    config2 = [0, 0, 2, 3, 3, 5, 0]
    config3 = [0, 1, 1, 3, 3, 5, 0]
    config4 = [0, 0, 1, 3, 3, 5, 0]
    config5 = [0, 0, 0, 2, 3, 5, 0]
    config6 = [8, 0, 0, 0, 0, 0, 0]

    game1 = SolitaireMancala()
    game2 = SolitaireMancala()
    game3 = SolitaireMancala()
    game4 = SolitaireMancala()
    game5 = SolitaireMancala()
    game6 = SolitaireMancala()
    game1.set_board(config1)
    game2.set_board(config2)
    game3.set_board(config3)
    game4.set_board(config4)
    game5.set_board(config5)
    game6.set_board(config6)

    # add tests using suite.run_test(....) here

    suite.run_test(game1.get_num_seeds(1),config1[1], "get_num_seeds 1")
    suite.run_test(game1.get_num_seeds(3),config1[3], "get_num_seeds 2")
    suite.run_test(game1.get_num_seeds(5),config1[5], "get_num_seeds 3")
    suite.run_test(game2.get_num_seeds(1),config2[1], "get_num_seeds 4")
    suite.run_test(game2.get_num_seeds(3),config2[3], "get_num_seeds 5")
    suite.run_test(game2.get_num_seeds(5),config2[5], "get_num_seeds 6")
    suite.run_test(game3.get_num_seeds(1),config3[1], "get_num_seeds 7")
    suite.run_test(game3.get_num_seeds(3),config3[3], "get_num_seeds 8")
    suite.run_test(game3.get_num_seeds(5),config3[5], "get_num_seeds 9")

    suite.run_test(game3.is_game_won(), False, "Game won 1")
    suite.run_test(game6.is_game_won(), True, "Game won 2")

    suite.run_test(game1.is_legal_move(1), True, "is_legal_move 1")
    suite.run_test(game1.is_legal_move(2), False, "is_legal_move 2")
    suite.run_test(game1.is_legal_move(3), False, "is_legal_move 3")
    suite.run_test(game1.is_legal_move(5), True, "is_legal_move 5 ")

    suite.run_test(game1.choose_move(), 1, "Choose move 1: ")
    suite.run_test(game2.choose_move(), 2, "Choose move 2: ")
    suite.run_test(game3.choose_move(), 1, "Choose move 3: ")
    suite.run_test(game4.choose_move(), 3, "Choose move 4: ")
    suite.run_test(game5.choose_move(), 5, "Choose move 5: ")

    suite.run_test(game1.plan_moves(), [1, 5, 1, 2, 1, 4, 1, 3, 1, 2, 1], "Plan move: ")
    suite.run_test(game1._board, [0, 1, 1, 1, 3, 5, 0], "Plan move isometry: ")

    game1.apply_move(5)
    game2.apply_move(4)
    game3.apply_move(1)
    suite.run_test(game1._board, [1, 2, 2, 2, 4, 0, 0], "Apply move 1: ")
    suite.run_test(game2._board, config2, "Apply move 2: ")
    suite.run_test(game3._board, [1, 0, 1, 3, 3, 5, 0], "Apply move 3: ")


    # report number of tests and failures
    suite.report_results()
