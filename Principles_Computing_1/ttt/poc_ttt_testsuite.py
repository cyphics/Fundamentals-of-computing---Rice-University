"""
Test suite for Tic Tac Toe game
"""

import poc_simpletest
import poc_ttt as ttt
import poc_ttt_provided as provided

def run_suite():
    suite = poc_simpletest.TestSuite()

    score = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    ttt.mc_update_scores(score, provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]]), 3)
    suite.run_test(score, [[1.0, 1.0, -2.0], [-2.0, 1.0, 0], [0, 1.0, -2.0]], "mc_update_scores #1:")

    suite.run_test(ttt.mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.EMPTY, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERO, 100), (2, 1), "mc_move # 1")

    suite.run_test(ttt.get_best_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]), [[0, 0], [3, 0]]), (1, 0), "get_best_move #1")



    suite.report_results()


run_suite()

test_board = provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]])

test_board2 = provided.TTTBoard(3, False, [[provided.EMPTY, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERX], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY]])

print(test_board)

#print(test_board2)

# print(ttt.mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), provided.PLAYERX, 100))
# print(ttt.mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), provided.PLAYERX, 100))
# print(ttt.mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), provided.PLAYERX, 100))
# print(ttt.mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), provided.PLAYERX, 100))
# print(ttt.mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), provided.PLAYERX, 100))
