# globals for user interface
WIDTH = 800
HEIGHT = 600
CANVAS_SIZE = (WIDTH, HEIGHT)
SPLASH_SCALE = 0.7
ROCK_DIM = 64
ROCK_CENTER = [64, 64]
ROCK_SIZE = [128, 128]
EXPLOSION_CENTER = [50, 50]
EXPLOSION_SIZE = [100, 100]
EXPLOSION_DIM = [9, 9]
BOMB_CENTER = [111, 111]
BOMB_SIZE = [222, 222]
BOMB_DIM = [4, 7]

# PHYSICS CONSTANTS
ACCELERATION = 0.2
FRICTION = 0.97  # between 0 and 1
ROTATION = 0.1
ROTATION_MAX = 0.1
ROCK_MAX_VELOCITY = 2

# gameplay constants
in_game = False
tuto = False
tuto_move = "Forward"
tuto_move_target = [WIDTH / 2, HEIGHT / 4]
tuto_done = False
tuto_loop = 0
score = 0
lives = 3
time = 0
SCORE_PER_HIT = 10
