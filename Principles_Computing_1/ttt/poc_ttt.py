"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_provided as provided
# import poc_ttt_testsuite
# import poc_ttt_gui


# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 2.0  # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player


def mc_trial(board, player):
    """
    Takes an unfinished board and a player.
    Play the board, starting with player, until
    the game is over
    """
    while not board.check_win():
        random_square = get_random_square(board)
        board.move(random_square[0], random_square[1], player)
        if not board.check_win():
            random_square = get_random_square(board)
            board.move(random_square[0],
                       random_square[1],
                       provided.switch_player(player))


def mc_update_scores(scores, board, player):
    """
    Takes a finished board, and update the score
    according to player
    """
    if player == provided.PLAYERX:
        score_x = SCORE_CURRENT
        score_o = -SCORE_OTHER
    elif player == provided.PLAYERO:
        score_x = -SCORE_OTHER
        score_o = SCORE_CURRENT

    if board.check_win() == player:
        factor = 1
    elif board.check_win() == provided.switch_player(player):
        factor = -1
    else:
        factor = 0

    for col in range(board.get_dim()):
        for row in range(board.get_dim()):
            if board.square(row, col) == provided.PLAYERX:
                scores[row][col] += score_x * factor
            elif board.square(row, col) == provided.PLAYERO:
                scores[row][col] += score_o * factor


def get_best_move(board, scores):
    """
    Takes a board and a grid of scores.
    Returns the empty square (tuple )with the maximum
    score for player.
    """
    best_score = None
    best_moves = []
    for square in board.get_empty_squares():
        if scores[square[0]][square[1]] > best_score:
            best_score = scores[square[0]][square[1]]
    for square in board.get_empty_squares():
        if scores[square[0]][square[1]] == best_score:
            best_moves.append(square)

    return tuple(random.choice(best_moves))


def mc_move(board, player, trials):
    """
    Takes a board, a player, and an amount of trials.
    Returns the best move (tuple) to play, according to simulation.
    """
    scores = [[0 for dummycol in range(board.get_dim())]
              for dummyrow in range(board.get_dim())]
    trial = 0
    while trial < trials:
        clone_board = board.clone()
        mc_trial(clone_board, player)
        mc_update_scores(scores, clone_board, player)
        trial += 1
    return get_best_move(board, scores)


def get_random_square(board):
    """
    Returns an empty square of the board
    chosen by random"""
    squares_list = board.get_empty_squares()
    if len(squares_list) > 0:
        return squares_list[random.randrange(len(squares_list))]
    else:
        print("Error, no more available squares")


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)

# poc_ttt_testsuite.run_suite()
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
