"""
Student portion of Zombie Apocalypse mini-project
"""
import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list=None,
                 zombie_list=None, human_list=None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list is not None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list is not None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list is not None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._zombie_list = []
        self._human_list = []
        poc_grid.Grid.clear(self)

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        num = 0
#        zombies_list_copy = list(self._zombie_list)
        while num < len(self._zombie_list):
            yield self._zombie_list[num]
            num += 1

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        num = 0
        while num < len(self._human_list):
            yield self._human_list[num]
            num += 1

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        # Init variables
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
#        visited = [[0 for col in range(self._grid_width)] for row in range(self._grid_height)]
        distance_field = [[(self._grid_height * self._grid_width) for col in range(self._grid_width)] for row in range(self._grid_height)]
#        distance_field = poc_grid.Grid(self._grid_height, self._grid_width)

        # Create copy queue
        boundary = poc_queue.Queue()
        if entity_type == ZOMBIE:
            for zombie in self.zombies():
                boundary.enqueue(zombie)
        else:
            for human in self.humans():
                boundary.enqueue(human)

        ## Init field
        # Set initial boundary and mark as visited
        for cell in boundary:
            visited.set_full(cell[0], cell[1])
            distance_field[cell[0]][cell[1]] = 0
        # Set obstacles as visited
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if not self.is_empty(row, col):
                    visited.set_full(row, col)

        ## Compute
        # While queue is not empty
        while len(boundary) > 0:
            # Set current cell from queue
            current_cell = boundary.dequeue()
            # Set current cell as full in visited
            visited.set_full(current_cell[0], current_cell[1])
            # Set neighborhood to evaluate
            neighbors = visited.four_neighbors(current_cell[0], current_cell[1])
            # Update neighborhood
            for cell in neighbors:
                # If cell not yet visited
                if visited.is_empty(cell[0], cell[1]):
                    visited.set_full(cell[0], cell[1])
                    # Add cell to queue
                    boundary.enqueue(cell)
                    actual_distance = distance_field[current_cell[0]][current_cell[1]] + 1
                    if actual_distance != self._grid_height * self._grid_width:
                        # Set distance (current + 1)
                        distance_field[cell[0]][cell[1]] = actual_distance
        return distance_field

    def print_distance_field(self, field):
        """
        Print a distance field in a human readable manner with
        one row per line
        """
        output = ""
        for row in field:
            output += str(row) + "\n"

        print(output)

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        count = 0
        # For each human in list
        for human in self.humans():
            # Evaluate distance to nearest zombie
            #            human = self._human_list[count]
            current_distance = zombie_distance_field[human[0]][human[1]]
            # Set his neighborhood
            neighborhood = self.eight_neighbors(human[0], human[1])
            next_cell = human
            # Find best next cell
            for cell in neighborhood:
                if self.is_empty(cell[0], cell[1]):
                    # Set cell distance
                    potential_distance = zombie_distance_field[cell[0]][cell[1]]
                    # If cell is better than current
                    if potential_distance > current_distance:
                        # Update distance and next cell
                        current_distance = potential_distance
                        next_cell = cell
            # Remove old position
            self._human_list[count] = tuple(next_cell)
            count += 1


    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        count = 0
        # For zombie in list
        for zombie in self.zombies():
            # Evaluate distance to nearest human
            current_distance = human_distance_field[zombie[0]][zombie[1]]
            # Set his neighborhood
            neighborhood = self.four_neighbors(zombie[0], zombie[1])
            next_cell = zombie
            # Find best next cell
            for cell in neighborhood:
                if self.is_empty(cell[0], cell[1]):
                    # Set cell distance
                    potential_distance = human_distance_field[cell[0]][cell[1]]
                    # If cell is better than current
                    if potential_distance < current_distance:
                        # Update distance and next cell
                        current_distance = potential_distance
                        next_cell = cell
            # Remove old position
            self._zombie_list[count] = tuple(next_cell)
            count += 1


# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(30, 40))
