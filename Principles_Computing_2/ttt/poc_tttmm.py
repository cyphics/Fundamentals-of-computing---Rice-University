"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
# import codeskulptor
# codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

# rec_level = 0
def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    # rec_level
    # rec_level += 1
    # Base case
    for move in board.get_empty_squares():
        temp_board = board.clone()
        temp_board.move(move[0], move[1], player)
        if temp_board.check_win() == player:
            # print(temp_board)
            # rec_level -= 1
            return SCORES[player], move
        elif temp_board.check_win() == provided.DRAW:
            # rec_level -= 1
            return SCORES[provided.DRAW], move

    # Recursive case
    list_moves = []
    for move in board.get_empty_squares():
#        print "." * # rec_level, player, "plays", move
        temp_board = board.clone()
        temp_board.move(move[0], move[1], player)
        move_score = mm_move(temp_board, provided.switch_player(player))[0]  # * SCORES[player]
#        print "." * # rec_level, "If player", player, "plays", move, "with board\n", board, "the score is", move_score
        if move_score == SCORES[player]:
            return SCORES[player], move
        list_moves.append((move_score, move))
    # print
    # print "For", player, "with score", SCORES[player]
    # print board
    # print "." * # rec_level, list_moves
    # print

    # Move selection
    best_move = [float("-inf"), (-1, -1)]
    for elem in list_moves:
#        print "pot:", elem[0] * SCORES[player], ", curr:", best_move[0]
        if elem[0] * SCORES[player] > best_move[0]:
#            best_move = elem
            best_move[0] = elem[0] * SCORES[player]
            best_move[1] = elem[1]
    best_move[0] *= SCORES[player]
    # rec_level -= 1
#    print "Best move is then", best_move
#    print(list_moves)

    return tuple(best_move)


def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
