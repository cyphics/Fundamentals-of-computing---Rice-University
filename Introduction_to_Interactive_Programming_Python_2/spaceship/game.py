import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import constants
from ship import Ship
from sprite import Sprite
import artWorks as art
import info_images
import game_functions
import tutorial
import helper_functions as helper


class Game:
    def __init__(self):
        # General game variables
        self._in_game = False
        self._tuto = False
        self._tuto_done = False
        self._score = 0
        self._lives = 3
        self._time = 0

        # Game groups of sprites
        self._rocks_group = set()
        self._missiles_group = set()
        self._explosions_group = set()
        self._bombs_group = set()

        self._tutorial = tutorial.Tutorial()

        # Player ship
        self._my_ship = Ship([constants.WIDTH / 2, constants.HEIGHT / 2], [0, 0], 0, art.ship_image, info_images.ship_info, None, art.explosion_alpha_image, info_images.explosion_alpha_info)

        # Game timer
        self._timer = simplegui.create_timer(1000.0, self.rock_spawner)

    def is_in_game(self):
        return self._in_game

    def is_in_tuto(self):
        return self._tuto

    def is_tuto_done(self):
        return self._tuto_done

    def click(self):
        if not self._in_game:
            # Avoid repeating tuto after death
            if not self._tuto and not self._tuto_done:
                self._tuto = True
            # Start game
            else:
                self._missiles_group = set()
                self._explosions_group = set()
                self._rocks_group = set()
                self._bombs_group = set()
                self._tuto = False
                self._tuto_done = True
                self._in_game = True

    def key_up(self, key):
        """ Handles key up inputs"""
        if key == "right":
            self._my_ship.turn("No")
        elif key == "left":
            self._my_ship.turn("No")
        elif key == "up":
            self._my_ship.accelerate(False)

    def key_down(self, key):
        """ Handles key down inputs"""
        if self._in_game:
            if key == "left":
                self._my_ship.turn("Left")
            if key == "right":
                self._my_ship.turn("Right")
            if key == "up":
                self._my_ship.accelerate(True)
            if key == "space":
                self._my_ship.shoot(self._missiles_group)
            if key == "f":
                self._my_ship.shoot_bomb(self._bombs_group)

    def run(self, canvas):
        art.missile_sound.set_volume(0.5)
        art.ship_thrust_sound.set_volume(0.5)
        art.explosion_sound.set_volume(0.5)
        art.soundtrack.set_volume(0.5)

        # Draw background
        self.draw_background(canvas)
        # Start tutorial
#        self._tuto = True
#        self._in_game = True
        if self._tuto:
            if not self._tuto_done:
                info_images.bomb_info.lifespan = 50
                self._tutorial.run(canvas)
            else:
                self._tuto = False
        elif self._in_game:
            self.run_game(canvas)
        # Welcome screen
        else:
            self.draw_splash_screen(canvas)

    def draw_splash_screen(self, canvas):
        canvas.draw_image(art.splash_image,
                              info_images.splash_info.get_center(),
                              info_images.splash_info.get_size(),
                              [constants.WIDTH / 2, constants.HEIGHT / 2],
                              [constants.WIDTH * constants.SPLASH_SCALE, constants.HEIGHT * constants.SPLASH_SCALE])

    def draw_background(self, canvas):
        self._time += 1
        wtime = (self._time / 4) % constants.WIDTH
        center = info_images.debris_info.get_center()
        size = info_images.debris_info.get_size()
        canvas.draw_image(art.nebula_image,
                          info_images.nebula_info.get_center(),
                          info_images.nebula_info.get_size(),
                          [constants.WIDTH / 2, constants.HEIGHT / 2],
                          [constants.WIDTH, constants.HEIGHT])
        canvas.draw_image(art.debris_image,
                          center,
                          size,
                          (wtime - constants.WIDTH / 2, constants.HEIGHT / 2),
                          (constants.WIDTH, constants.HEIGHT))
        canvas.draw_image(art.debris_image,
                          center,
                          size,
                          (wtime + constants.WIDTH / 2, constants.HEIGHT / 2),
                          (constants.WIDTH, constants.HEIGHT))

    def draw_sprites(self, canvas):
        self.process_sprite_group(self._missiles_group, canvas)
        self.process_sprite_group(self._bombs_group, canvas)
        self.process_sprite_group(self._explosions_group, canvas)
        self.process_sprite_group(self._rocks_group, canvas)
        self._my_ship.draw(canvas)

    def run_game(self, canvas):
        info_images.bomb_info.lifespan = float('inf')
        self.update_game_state()
        self.draw_sprites(canvas)
        canvas.draw_text(str("Lifes: " + str(self._lives)), (20, 40), 32, 'Green')
        canvas.draw_text(str("Score : " + str(self._score)), (constants.CANVAS_SIZE[0] - 160, 40), 32, 'Green')
        canvas.draw_text(str("Bombs : " + str(self._my_ship.bombs)), (constants.CANVAS_SIZE[0] / 2 - 60, 40), 32, 'Green')


    def update_game_state(self):
        # If ships collides with object
        self.check_ship_state()
        self._score += self.group_group_collide(self._missiles_group, self._rocks_group) * 10
        self._score += self.group_group_collide(self._bombs_group, self._rocks_group) * 10
        self._my_ship.update()

    def process_sprite_group(self, group, canvas):
        """ Function that draws all the sprites of the given group on the canvas"""
        group_copy = set(group)
        for sprite in group_copy:
            sprite.draw(canvas)
            if sprite.update():
                group.remove(sprite)

    def group_collide(self, group, other_object):
        """ Test collisions between a group of sprites and a single other sprite"""
        group_copy = set(group)
        for object in group_copy:
            if object.collide(other_object):
                # If bomb, destroy all objects in radius
                if other_object.image == art.bomb_image:
                    other_object.explode(self._explosions_group)
                    art.explosion_sound.play()
                    for object2 in group_copy:
                        if helper.dist(object2.pos, other_object.pos) < 111:
                            object2.explode(self._explosions_group)
                            group.remove(object2)
                else:
                    object.explode(self._explosions_group)
                    group.remove(object)
                return True

    def group_group_collide(self, first_group, second_group):
        """ Test collision between two groups of sprites"""
        collided_objects = 0
        copy_first_group = set(first_group)
        for first_object in copy_first_group:
            if self.group_collide(second_group, first_object):
                    first_group.discard(first_object)
                    collided_objects += 1
        return collided_objects

    def initialize_game_state(self):
        self._rocks_group = set()
        self._explosions_group = set()
        self._bombs_group = set()
        self._my_ship = Ship([constants.WIDTH / 2, constants.HEIGHT / 2], [0, 0], 0, art.ship_image, info_images.ship_info, None, art.explosion_alpha_image, info_images.explosion_alpha_info)
        self._in_game = False
        self._score = 0
        self._lives = 3
        art.soundtrack.rewind()
        art.soundtrack.play()

    def check_ship_state(self):
        if self.group_collide(self._rocks_group, self._my_ship):
            self._my_ship.explode(self._explosions_group)
            self._lives -= 1
            if self._lives < 0:
                self.initialize_game_state()

                    # timer handler that spawns a rock
    def rock_spawner(self):
        if self._in_game:
            if len(self._rocks_group) < 12:
                a_rock = Sprite(game_functions.get_random_point(self._my_ship),
                                game_functions.get_random_velocity(constants.ROCK_MAX_VELOCITY),
                                0,
                                0,
                                art.rock_image,
                                info_images.rock_info,
                                art.explosion_mega_image,
                                info_images.explosion_mega_info)
                self._rocks_group.add(a_rock)
