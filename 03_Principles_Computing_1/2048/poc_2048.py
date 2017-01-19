"""
Clone of 2048 game.
Has to be run in CodeSculptor
"""

import poc_2048_gui
import random
# import poc_2048_test

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    new_line = []
    # Move tiles to the left
    for num in line:
        if num != 0:
            new_line.append(num)
    # Fill the rest with zeros
    while len(new_line) < len(line):
        new_line.append(0)

    for dummy_num in range(len(line) - 1):
        if new_line[dummy_num] == new_line[dummy_num + 1]:
            new_line[dummy_num] *= 2
            new_line.pop(dummy_num + 1)
            new_line.append(0)

    return new_line


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = [[0 for dummy_col in range(grid_width)]
                      for dummy_row in range(grid_height)]
        self.reset()
        self._move_indices = {}
        move_indice = []
        # Create move dictionary
        # UP
        for dummy_num in range(self._grid_width):
            move_indice.append((0, dummy_num))
        self._move_indices[UP] = move_indice
        # DOWN
        move_indice = []
        for dummy_num in range(self._grid_width):
            move_indice.append((self._grid_height - 1, dummy_num))
        self._move_indices[DOWN] = move_indice
        # LEFT
        move_indice = []
        for dummy_num in range(self._grid_height):
            move_indice.append((dummy_num, 0))
        self._move_indices[LEFT] = move_indice
        # RIGHT
        move_indice = []
        for dummy_num in range(self._grid_height):
            move_indice.append((dummy_num, self._grid_width - 1))
        self._move_indices[RIGHT] = move_indice

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_width)]
                      for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        board_string = ""
        for dummy_num in range(self._grid_height):
            board_string += str(self._grid[dummy_num]) + "\n"
        return board_string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return len(self._grid)

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return len(self._grid[0])

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        has_changed = False
        # Set number of steps for given direction
        if direction == UP or direction == DOWN:
            steps = len(self._move_indices[LEFT])
        else:
            steps = len(self._move_indices[DOWN])
        # Iterate over number of col/row according to direction

        for start_cell in self._move_indices[direction]:
            # Create a temp copy of processing line
            temp_line = []
            # copy each value in temp copy
            for step in range(steps):
                row = start_cell[0] + step * OFFSETS[direction][0]
                col = start_cell[1] + step * OFFSETS[direction][1]
                temp_line.append(self.get_tile(row, col))
            # Merge temp line
            temp_line = merge(temp_line)
            # Put temp line back in grid
            for step in range(steps):
                row = start_cell[0] + step * OFFSETS[direction][0]
                col = start_cell[1] + step * OFFSETS[direction][1]
                if self.get_tile(row, col) != temp_line[step]:
                    self.set_tile(row, col, temp_line[step])
                    has_changed = True
        if has_changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # Set tile value
        occupied_tile = True
        value = 0
        rand_value = random.randrange(0, 10)
        if rand_value > 0:
            value = 2
        else:
            value = 4
        # Set tile position
        while occupied_tile:
            rand_row = random.randrange(0, self._grid_height)
            rand_col = random.randrange(0, self._grid_width)
            random_tile = [rand_row, rand_col]
            # If tile is emtpy, quit loop
            if self.get_tile(rand_row, rand_col) == 0:
                occupied_tile = False

        self.set_tile(random_tile[0], random_tile[1], value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


# poc_2048_test.run_suite(TwentyFortyEight)
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
