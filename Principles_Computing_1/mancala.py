"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""

import mancala_test


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """

    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = [0]

    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board *= len(configuration)
        for dummy_num in range(len(configuration)):
            self._board[dummy_num] = configuration[dummy_num]

    def __str__(self):
        """
        Return string representation for Mancala _board
        """
        board_string = "["
        for dummy_num in range(len(self._board) - 1):
            board_string += str(self._board[len(self._board) - dummy_num - 1]) + ", "
        board_string += str(self._board[0]) + "]"
        return board_string

    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on _board
        """
        return self._board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for dummy_num in range(len(self._board) - 1):
            if self._board[dummy_num + 1] != 0:
                return False
        return True

    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if self._board[house_num] == house_num:
            return True
        return False

    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if house_num == 0:
            pass
        elif self.is_legal_move(house_num):
            self._board[house_num] = 0
            for dummy_num in range(house_num):
                self._board[dummy_num] += 1

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        move = 0
        for dummy_num in range(len(self._board) - 1):
            tested_position = len(self._board) - dummy_num - 1
            if self.is_legal_move(tested_position):
                move = tested_position
        if move == 0:
            if self.is_game_won():
                print("Game won!")
            else:
                print("No legal move left!")
        return move

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic:
        After each move, move the seeds in the house closest to the store
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        moves = []

        temp_board = SolitaireMancala()
        temp_board.set_board(self._board)
        while not temp_board.is_game_won():
            moves.append(temp_board.choose_move())
            temp_board.apply_move(temp_board.choose_move())

        return moves


# Create tests to check the correctness of your code
mancala_test.run_suite(SolitaireMancala)


# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())
