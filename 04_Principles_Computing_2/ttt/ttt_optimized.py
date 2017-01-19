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


def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """

    # Base case
    if board.check_win() is not None:
        return SCORES[board.check_win()], (-1, -1)

    # Recursive case
    list_moves = []
    for move in board.get_empty_squares():
        temp_board = board.clone()
        temp_board.move(move[0], move[1], player)
        move_score = mm_move(temp_board, provided.switch_player(player))[0]
        if move_score == SCORES[player]:
            return SCORES[player], move
        list_moves.append((move_score, move))

    # Move selection
    best_move = [float("-inf"), (-1, -1)]
    for elem in list_moves:
        if elem[0] * SCORES[player] > best_move[0]:
            best_move[0] = elem[0] * SCORES[player]
            best_move[1] = elem[1]
    best_move[0] *= SCORES[player]

    return tuple(best_move)


def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]


if __name__ == '__main__':
    # provided.play_game(move_wrapper, 1, False)
    poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
