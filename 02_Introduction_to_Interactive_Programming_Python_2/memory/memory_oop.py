# implementation of tile game - Memory

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
import sys

TILE_WIDTH=50
TILE_HEIGHT = 100

# State of the 'turning tile' process
click_counter=0
# Position in tile_states that are currently evaluated
trial_tiles=[]
# List of all tiles
tile_collection = []

# Create deck to play with
value_basis=list(range(1,9))
values_to_distribute=value_basis*2

class Tile:
    def __init__(self, value, exp, pos):
        self.number = value
        self.exposed = exp
        self.position = pos
    def __str__(self):
        return "Tile no " + str(self.number) + ", exposed is "+ str(self.exposed) + "position " + str(self.position)
    def getNumber(self):
        return self.number
    def is_exposed(self):
        return self.exposed
    def expose_tile(self):
        self.exposed = True
    def hide_tile(self):
        self.exposed = False
    def draw_tile(self, canvas):
        if self.exposed:
            canvas.draw_text(str(self.number), (self.position * TILE_WIDTH + TILE_WIDTH / 2, TILE_HEIGHT / 2), 32, 'Green')
        else:
            canvas.draw_line((self.position * TILE_WIDTH + TILE_WIDTH/2, TILE_HEIGHT), (self.position * TILE_WIDTH + TILE_WIDTH/2, 0), TILE_WIDTH -1, 'Green')

    def is_selected(self, click):
        return click[0]  > self.position * TILE_WIDTH and click[0] < self.position * TILE_WIDTH + TILE_WIDTH


# helper function to initialize globals
def new_game():
    # Set new list of tiles
    global tile_values, tile_states, click_counter, trial_tiles, tile_collection
    tile_values = values_to_distribute
    random.shuffle(tile_values)
    while len(tile_values) > 0:
        t = Tile(tile_values[-1], False, len(tile_values)-1)
        tile_collection.append(t)
        tile_values.pop()

    # Reset states
    click_counter = 0
    trial_tiles = []


# define event handlers
def mouseclick(pos):
    global tial_tiles
    for tile in tile_collection:
        if tile.is_selected(pos):
            print(tile)
            tile.expose_tile()
            trial_tiles.append(tile.position)


# tiles are logically 50x100 pixels in size
def draw(canvas):
    global tile_collection
    for tile in tile_collection:
        tile.draw_tile(canvas)



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(click_counter))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
