import math
import artWorks as art
import constants
from ship import Ship
from sprite import Sprite
import info_images
import helper_functions as helper
import game_functions


class Tutorial:

    def __init__(self):
        """ Init function for tutorial"""
        # Create 3 ships
        self._move_ship = Ship([constants.WIDTH / 4, constants.HEIGHT / 4], [0, 0], 0, art.ship_image, info_images.ship_info, None, art.explosion_alpha_image, info_images.explosion_alpha_info)
        self._fire_ship = Ship([80, constants.HEIGHT / 4 * 3], [0, 0], 0, art.ship_image, info_images.ship_info, None, art.explosion_alpha_image, info_images.explosion_alpha_info)
        self._bomb_ship = Ship([constants.WIDTH / 2 + 50, constants.HEIGHT / 4 * 3], [0, 0], 0, art.ship_image, info_images.ship_info, None, art.explosion_alpha_image, info_images.explosion_alpha_info)

        # Create sprite groups
        self._bomb_ship.bombs = float('inf')
        self._ships_group = []
        self._missiles_group = set()
        self._bombs_group = set()
        self._rocks_group = set()
        self._explosions_group = set()
        self._ships_group.append(self._move_ship)
        self._ships_group.append(self._fire_ship)
        self._ships_group.append(self._bomb_ship)
        self._move_ship.angle_vel = 0
        self._move_ship.thrust = True
        self._move_ship.accelerate(True)

        self._target1 = [140, constants.HEIGHT / 4]
        self._target2 = [constants.WIDTH / 3, constants.HEIGHT / 4]
        self._ROT_SPEED = 1
        self._CIRCLE_RAD = 30
        self._ANGLE_OFFSET = 1
        self._ANGLE_OFFSET2 = 0.5
        self._movement_direction = "Forward"
        self._movement_target = [constants.WIDTH / 2, constants.HEIGHT / 4]
        self._loop = 0

        self._bomb_text_width = 400
        self._shoot_text_width = 400
        self._tuto_text_width = 400
        self._click_text_width = 400
        # self._bomb_text_width = frame.get_canvas_textwidth("Launch bomb : F key", 32)
        # self._shoot_text_width = frame.get_canvas_textwidth("Shoot: Space bar", 32)
        # self._tuto_text_width = frame.get_canvas_textwidth("TUTORIAL", 32)
        # self._click_text_width = frame.get_canvas_textwidth("Click to play", 32)

        art.missile_sound.set_volume(0)
        art.explosion_sound.set_volume(0)
        art.ship_thrust_sound.set_volume(0)
        art.ship_thrust_sound.pause()
        art.missile_sound.pause()
        art.explosion_sound.pause()

    def run(self, canvas):
        self.update_move_ship()
        self.update_fire_ship(canvas)
        self.update_bomb_ship(canvas)
        self.generate_rocks()

        self.update_tutorial_state(canvas)
        for ship in self._ships_group:
            ship.draw(canvas)

        self.draw_explanations(canvas)

    def draw_explanations(self, canvas):
        move_square = [(10, 10),
                       (constants.WIDTH - 10, 10),
                       (constants.WIDTH - 10, constants.HEIGHT / 2 - 10),
                       (constants.WIDTH - 10, constants.HEIGHT / 2 - 10),
                       (10, constants.HEIGHT / 2 - 10),
                       (10, 10)]
        fire_square = [(10, constants.HEIGHT / 2 + 10),
                       (constants.WIDTH / 2 - 10, constants.HEIGHT / 2 + 10),
                       (constants.WIDTH / 2 - 10, constants.HEIGHT - 50),
                       (constants.WIDTH / 2 - 10 - self._shoot_text_width / 2, constants.HEIGHT - 50),
                       (constants.WIDTH / 2 - 10 - self._shoot_text_width / 2, constants.HEIGHT - 10),
                       (10, constants.HEIGHT - 10), (10, constants.HEIGHT / 2 + 10)]
        bomb_square = [(constants.WIDTH / 2 + 10, constants.HEIGHT / 2 + 10),
                       (constants.WIDTH - 10, constants.HEIGHT / 2 + 10),
                       (constants.WIDTH - 10, constants.HEIGHT - 10),
                       (constants.WIDTH / 2 + 10 + self._shoot_text_width / 2, constants.HEIGHT - 10),
                       (constants.WIDTH / 2 + 10 + self._shoot_text_width / 2, constants.HEIGHT - 50),
                       (10 + constants.WIDTH / 2, constants.HEIGHT - 50),
                       (10 + constants.WIDTH / 2, constants.HEIGHT / 2 + 10)]
        canvas.draw_polyline(move_square, 3, "White")
        canvas.draw_polyline(fire_square, 3, "White")
        canvas.draw_polyline(bomb_square, 3, "White")
        canvas.draw_text("TUTORIAL",
                         (constants.WIDTH / 2 - self._tuto_text_width / 2, 50),
                         32,
                         "White")
        canvas.draw_text("Movement : Arrow keys",
                         (constants.WIDTH / 2, constants.HEIGHT / 4),
                         32,
                         "White")
        canvas.draw_text("Shoot: Space bar",
                         (constants.WIDTH / 4 + 10 - self._shoot_text_width / 2, constants.HEIGHT / 2 + 40),
                         32,
                         "White")

        canvas.draw_text("Launch bomb : F key",
                         (constants.WIDTH / 4 * 3 + 10 - self._bomb_text_width / 2, constants.HEIGHT / 2 + 40),
                         32,
                         "White")

        canvas.draw_text("Click to play",
                         (constants.WIDTH / 2 - self._click_text_width / 2, constants.HEIGHT - 20),
                         32,
                         "White")

        # canvas.draw_circle(self._movement_target, 3, 1, "White", "White")

    def update_move_ship(self):
        """ Manage move ship behaviour. Make it move between to points"""
        # Set target point
        if self._move_ship.pos[0] < self._target1[0]:
            self._movement_target = self._target2
        elif self._move_ship.pos[0] > self._target2[0]:
            self._movement_target = self._target1

        # Set ship motion to reach target
        vector_to_target = helper.points_to_vector(self._move_ship.pos, self._movement_target)
        angle_to_target = helper.vector_to_angle(vector_to_target) - self._move_ship.angle  # (2 * math.pi - self._move_ship.angle)
        angle_to_target = helper.fix_angle(angle_to_target)
        if abs(angle_to_target) < 0.4 or angle_to_target > 2 * math.pi - 0.4:
            self._move_ship.turn("No")
        elif angle_to_target < math.pi:
            # self._move_ship.turn("Left")
            self._move_ship.turn("Right")
        elif angle_to_target >= math.pi:
            self._move_ship.turn("Left")

        self._move_ship.update()

    def update_fire_ship(self, canvas):
        if self._loop % 100 < 50:
            if self._loop % 10 == 0:
                self._fire_ship.shoot(self._missiles_group)
        game_functions.process_sprite_group(canvas, self._missiles_group)
        self._loop += 1

    def update_bomb_ship(self, canvas):
        # BOMB SHIP
        if ((self._loop - 1) % 100) == 0:
            self._bomb_ship.shoot_bomb(self._bombs_group)
        game_functions.process_sprite_group(canvas, self._bombs_group)

    def generate_rocks(self):
        if (self._loop - 1) % 100 == 0:
            a_rock = Sprite([constants.WIDTH / 2 - 70, constants.HEIGHT / 4 * 3],
                            (0, 0),
                            0,
                            0,
                            art.rock_image,
                            info_images.rock_info,
                            art.explosion_mega_image,
                            info_images.explosion_mega_info)
            self._rocks_group.add(a_rock)
            a_rock = Sprite([constants.WIDTH - 100, constants.HEIGHT / 4 * 3],
                            (0, 0),
                            0,
                            0,
                            art.rock_image,
                            info_images.rock_info,
                            art.explosion_mega_image,
                            info_images.explosion_mega_info)
            self._rocks_group.add(a_rock)
            a_rock = Sprite([constants.WIDTH - 70, constants.HEIGHT / 4 * 3 - 50],
                            (0, 0),
                            0,
                            0,
                            art.rock_image,
                            info_images.rock_info,
                            art.explosion_mega_image,
                            info_images.explosion_mega_info)
            self._rocks_group.add(a_rock)
            a_rock = Sprite([constants.WIDTH - 70, constants.HEIGHT / 4 * 3 + 50],
                            (0, 0),
                            0,
                            0,
                            art.rock_image,
                            info_images.rock_info,
                            art.explosion_mega_image,
                            info_images.explosion_mega_info)
            self._rocks_group.add(a_rock)

    def update_tutorial_state(self, canvas):
        game_functions.process_sprite_group(canvas, self._rocks_group)
        game_functions.group_group_collide(self._missiles_group, self._rocks_group, self._explosions_group)
        game_functions.group_group_collide(self._bombs_group, self._rocks_group, self._explosions_group)
        game_functions.process_sprite_group(canvas, self._explosions_group)
