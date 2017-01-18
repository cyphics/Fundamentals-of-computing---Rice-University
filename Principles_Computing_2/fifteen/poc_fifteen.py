"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui


def helper_move_zero_to(game, target_row, target_col):
    """
    Move zero tile to given position
    """
    result = ""
    # Move vertically
    if game.current_position(0, 0)[0] > target_row:
        while game.current_position(0, 0)[0] > target_row:
            game.update_puzzle("u")
        result += "u"
        # result += game.move_zero_up(target_row)
    else:
        while game.current_position(0, 0)[0] < target_row:
            game.update_puzzle("d")
            result += "d"
        # result += game.move_zero_down(target_row)
    # Move horizontally
    if game.current_position(0, 0)[1] > target_col:
        while game.current_position(0, 0)[1] > target_col:
            game.update_puzzle("l")
            result += "l"
        # result += game.move_zero_left(target_col)
    else:
        while game.current_position(0, 0)[1] < target_col:
            game.update_puzzle("r")
            result += "r"
        # result += game.move_zero_right(target_col)
    return result

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid is not None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods
    def lower_row_invariant_partial(self, target_row, target_col):
        """
        Check if solved part is still solved
        """
        # Test if below rows are solved
        for row in range(target_row + 1, self.get_height()):
            for col in range(self.get_width()):
                if self.get_number(row, col) != col + row * self.get_width():
                    return False
        # Test if current row is solved
        for col in range(target_col + 1, self.get_width()):
            if self.get_number(target_row, col) != col + target_row * self.get_width():
                return False
        return True

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        # Test if 0 in tested position
        if self.get_number(target_row, target_col) != 0:
            return False
        # Test if below rows are solved
        return self.lower_row_invariant_partial(target_row, target_col)

    # def move_zero_up(self, target_row):
    #     """
    #     Move zero tile up to given row
    #     """
    #     result = ""
    #     while self.current_position(0, 0)[0] > target_row:
    #         self.update_puzzle("u")
    #         result += "u"
    #     return result

    # def move_zero_down(self, target_row):
    #     """
    #     Move zero tile down to given row
    #     """
    #     result = ""
    #     while self.current_position(0, 0)[0] < target_row:
    #         self.update_puzzle("d")
    #         result += "d"
    #     return result

    # def move_zero_left(self, target_col):
    #     """
    #     Move zero tile left to given col
    #     """
    #     result = ""
    #     while self.current_position(0, 0)[1] > target_col:
    #         self.update_puzzle("l")
    #         result += "l"
    #     return result

    # def move_zero_right(self, target_col):
    #     """
    #     Move zero tile right to given col
    #     """
    #     result = ""
    #     while self.current_position(0, 0)[1] < target_col:
    #         self.update_puzzle("r")
    #         result += "r"
    #     return result

    # def move_zero_to(self, target_row, target_col):
    #     """
    #     Move zero tile to given position
    #     """
    #     result = ""
    #     # Move vertically
    #     if self.current_position(0, 0)[0] > target_row:
    #         while self.current_position(0, 0)[0] > target_row:
    #             self.update_puzzle("u")
    #         result += "u"
    #         # result += self.move_zero_up(target_row)
    #     else:
    #         while self.current_position(0, 0)[0] < target_row:
    #             self.update_puzzle("d")
    #             result += "d"
    #         # result += self.move_zero_down(target_row)
    #     # Move horizontally
    #     if self.current_position(0, 0)[1] > target_col:
    #         while self.current_position(0, 0)[1] > target_col:
    #             self.update_puzzle("l")
    #             result += "l"
    #         # result += self.move_zero_left(target_col)
    #     else:
    #         while self.current_position(0, 0)[1] < target_col:
    #             self.update_puzzle("r")
    #             result += "r"
    #         # result += self.move_zero_right(target_col)
    #     return result

    def move_left_to_target(self, target_row, target_col):
        """
        Takes a coordinate, and move the zero tile
        left to this location
        """
        result = ""

        if target_col == 0 and self.current_position(0, 0)[1] == 0:
            # Go right to target, then move left
            self.update_puzzle("r")
            result += "r"
            # while self.current_position(0, 0)[0] != target_row:
            #     self.update_puzzle("u")
            #     result += "u"
            # while self.current_position(0, 0)[1] != 0:
            #     self.update_puzzle("l")
            #     result += "l"
            # return result

        # If on same col, go left first
        if self.current_position(0, 0)[1] == target_col:
            self.update_puzzle("l")
            result += "l"
        # Move on correct row
        if self.current_position(0, 0)[0] > target_row:
            while self.current_position(0, 0)[0] > target_row:
                self.update_puzzle("u")
                result += "u"
            # result += self.move_zero_up(target_row)
        else:
            while self.current_position(0, 0)[0] < target_row:
                self.update_puzzle("d")
                result += "d"
            # result += self.move_zero_down(target_row)

        # Move on correct col
        # If target is on left
        if self.current_position(0, 0)[1] > target_col:
            while self.current_position(0, 0)[1] > target_col:
                self.update_puzzle("l")
                result += "l"
            # result += self.move_zero_left(target_col)
        # If target is on right
        elif self.current_position(0, 0)[1] < target_col:
            while self.current_position(0, 0)[1] < target_col - 1:
                self.update_puzzle("r")
                result += "r"
            # result += self.move_zero_right(target_col - 1)

        # Test game state is preserved
        # assert self.lower_row_invariant_partial(starting_point[0], starting_point[1]), "Game messed up"
        return result

    def move_target_to_col(self, destination, sens):
        """
        Take a direction (number) and a sens (up or down)
        and rotates until the tile on the right of the zero
        tile reaches the destination
        """
        result = ""
        # Calculate number of required moves (positive = to the left, neg = to the right)
        moves = self.current_position(0, 0)[1] + 1 - destination
        # while self.current_position(target_row, target_col)[1] != destination:
        while moves != 0:
            # Move to the right
            if moves < 0:
                if self.current_position(0, 0)[1] == self.get_width() - 1:
                    self.update_puzzle("r")
                    result += "r"
                elif sens is "down":
                    self.update_puzzle("drrul")
                    result += "drrul"
                else:
                    self.update_puzzle("urrdl")
                    result += "urrdl"
                moves += 1
            # Move to the left
            else:
                if self.current_position(0, 0)[1] == 0:
                    self.update_puzzle("r")
                    result += "r"
                elif sens is "down":
                    self.update_puzzle("rdllu")
                    result += "rdllu"
                else:
                    self.update_puzzle("rulld")
                    result += "rulld"
                moves -= 1
        return result

    def move_target_to_row(self, destination_row):
        """
        Move target tile to given row
        """
        result = ""
        while self.current_position(0, 0)[0] < destination_row:
            self.update_puzzle("druld")
            result += "druld"
        return result

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        total_moves = ""
        # Check that board is solved at this point
        assert self.lower_row_invariant(target_row, target_col), "Error, board not solved"
        # Find target tile
        target_tile = self.current_position(target_row, target_col)

        total_moves += self.move_left_to_target(target_tile[0], target_tile[1])

        # Move target above final position
        if target_tile[0] < target_row - 2 or target_tile[0] == 0:
            total_moves += self.move_target_to_col(target_col, "down")
        else:
            total_moves += self.move_target_to_col(target_col, "up")

        # Move target down until in place
        total_moves += self.move_target_to_row(target_row)
        # Test new board
        assert self.lower_row_invariant(target_row, target_col - 1)
        return total_moves

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        total_moves = ""
        # Check initial state
        assert self.lower_row_invariant(target_row, 0), "Error, board not solved"

        self.update_puzzle("u")
        total_moves += "u"

        # If already solved
        if self.lower_row_invariant_partial(target_row - 1, self.get_width() - 1):
            self.update_puzzle("r" * (self.get_width() - 1))
            total_moves += "r" * (self.get_width() - 1)
            return total_moves

        # Bring tile above target_row
        target_tile = self.current_position(target_row, 0)

        total_moves += self.move_left_to_target(target_tile[0], target_tile[1])
        # print self

        # Move target above final position
        if target_tile[0] < target_row - 2 or target_tile[0] == 0:
            total_moves += self.move_target_to_col(1, "down")
        else:
            total_moves += self.move_target_to_col(1, "up")
        # Move tile down
        total_moves += self.move_target_to_row(target_row - 1)
        # Cicle to solve
        self.update_puzzle("ruldrdlurdluurddlur")
        total_moves += "ruldrdlurdluurddlur"

        # Put zero tile to next position
        self.update_puzzle("r" * (self.get_width() - 2))
        total_moves += "r" * (self.get_width() - 2)
        # Test new board
        assert self.lower_row_invariant(target_row - 1, self.get_width() - 1)
        return total_moves

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # Test if below rows are solved
        if self.current_position(0, 0) != (0, target_col):
            return False
        if not self.lower_row_invariant_partial(1, target_col - 1):
            return False
        # Test if current row is solved
        for col in range(target_col + 1, self.get_width()):
            if self.get_number(0, col) != col:
                return False
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # Test if row 0 is solved
        for col in range(target_col + 1, self.get_width()):
            if self.get_number(0, col) != col:
                return False
        # Test is rest is solved
        return self.lower_row_invariant(1, target_col)

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row0_invariant(target_col), "Board not ready to be solved"
        result = ""

        # Go left to target
        self.update_puzzle("ld")
        result += "ld"
        # If not already solved, continue
        if not self.row1_invariant(target_col - 1):
            target_tile = self.current_position(0, target_col)
            # Go left to target
            result += self.move_left_to_target(target_tile[0], target_tile[1])
            # Go row 1
            result += self.move_target_to_row(1)
            # Go to col -1
            result += self.move_target_to_col(target_col - 1, "up")
            # Cicle to final position
            self.update_puzzle("urdlurrdluldrruld")
            result += "urdlurrdluldrruld"
        assert self.row1_invariant(target_col - 1)
        return result

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        result = ""
        assert self.row1_invariant(target_col), "Board not ready to be solved"
        result += self.solve_interior_tile(1, target_col)
        self.update_puzzle("ur")
        result += "ur"
        assert self.row0_invariant(target_col), "Board messed up"
        return result

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        result = ""

        # Put zero at final position
        self.update_puzzle("ul")
        result += "ul"
        # Cicle until solved
        # print self
        while self.get_number(0, 1) != 1:
            self.update_puzzle("drul")
            result += "drul"
            # print self
        return result

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        total_moves = ""
        # Place zero tile on bottom right
        while self.current_position(0, 0)[1] != self.get_width() - 1:
            self.update_puzzle("r")
            total_moves += "r"
        while self.current_position(0, 0)[0] != self.get_height() - 1:
            self.update_puzzle("d")
            total_moves += "d"
        # Solve m-2 rows
        for idx in range(2, self.get_height()):
            current_row_to_solve = self.get_height() + 1 - idx
            for idx2 in range(1, self.get_width()):
                current_col_to_solve = self.get_width() - idx2
                total_moves += self.solve_interior_tile(current_row_to_solve, current_col_to_solve)
            total_moves += self.solve_col0_tile(current_row_to_solve)
        # Solve n-2 columns
        for idx in range(2, self.get_width()):
            current_col_to_solve = self.get_width() + 1 - idx
            total_moves += self.solve_row1_tile(current_col_to_solve)
            total_moves += self.solve_row0_tile(current_col_to_solve)
        # Solve final square
        total_moves += self.solve_2x2()
        assert self.row0_invariant(0)
        return total_moves

# Start interactive simulation
poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))
