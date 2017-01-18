"""
An example of creating a distance field using Manhattan distance
"""

GRID_HEIGHT = 6
GRID_WIDTH = 8


def manhattan_distance(row0, col0, row1, col1):
    """
    Compute the Manhattan distance between the cells
    (row0, col0) and (row1, col1)
    """
    return abs(row1 - row0) + abs(col1 - col0)


def create_distance_field(entity_list):
        """
        Create a Manhattan distance field that contains the minimum distance to
        each entity (zombies or humans) in entity_list
        Each entity is represented as a grid position of the form (row, col)
        """
        distance_field = [[float("inf") for col in range(GRID_WIDTH)] for row in range(GRID_HEIGHT)]
        for entity in entity_list:
            for row in range(GRID_HEIGHT):
                for col in range(GRID_WIDTH):
                    distance = manhattan_distance(entity[0], entity[1], row, col)
                    if distance < distance_field[row][col]:
                        distance_field[row][col] = distance

        return distance_field


def print_field(field):
    """
    Print a distance field in a human readable manner with
    one row per line
    """
    output = ""
    for row in field:
        output += str(row) + "\n"

    print(output)


def run_example():
    """
    Create and print a small distance field
    """
    field = create_distance_field([[4, 0], [2, 5]])
    print_field(field)

run_example()

# Sample output for the default example
#[4, 5, 5, 4, 3, 2, 3, 4]
#[3, 4, 4, 3, 2, 1, 2, 3]
#[2, 3, 3, 2, 1, 0, 1, 2]
#[1, 2, 3, 3, 2, 1, 2, 3]
#[0, 1, 2, 3, 3, 2, 3, 4]
#[1, 2, 3, 4, 4, 3, 4, 5]
