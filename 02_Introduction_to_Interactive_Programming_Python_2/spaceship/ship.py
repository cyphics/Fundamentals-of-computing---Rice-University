# Ship class

import math
import artWorks as art
import constants
import helper_functions as helper
from sprite import Sprite
import info_images
import game_functions


class Ship:
    def __init__(self, pos, vel, angle, image, info, sound=art.ship_thrust_sound, explosion_image=None, explosion_info=None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.acceleration = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.sound = art.ship_thrust_sound
        self.sound.play()
        self.sound.rewind()
        self.explosion_image = explosion_image
        self.explosion_info = explosion_info
        self.bombs = 5
        self.bomb_group = set()
        self.missiles_group = set()

    def get_pos(self):
        return self.pos

    def set_pos(self, new_pos):
        for i in range(2):
            self.pos[i] = new_pos[i]

    def set_angle(self, angle):
        angle %= 2 * math.pi
        if angle < 0:
            angle = 2 * math.pi - angle
        self.angle = angle

    def get_radius(self):
        return self.radius

    def update_position(self):
        for i in range(2):
            self.pos[i] = (self.pos[i] + self.vel[i]) % constants.CANVAS_SIZE[i]

    def update_velocity(self):
        for i in range(2):
            self.vel[i] += self.acceleration * helper.angle_to_vector(self.angle)[i] - self.vel[i] * (1 - constants.FRICTION)

    def update_angle(self):
        self.angle += self.angle_vel
        self.angle %= 2 * math.pi

    def accelerate(self, acceleration):
        if acceleration:
            self.sound.play()
            self.acceleration = constants.ACCELERATION
            self.thrust = True
        else:
            self.sound.rewind()
            self.acceleration = 0
            self.thrust = False

    def turn(self, direction):
        if direction == "Left":
            self.angle_vel -= constants.ROTATION
        elif direction == "Right":
            self.angle_vel += constants.ROTATION
        else:
            self.angle_vel = 0

        # Cap velocity angle
        if self.angle_vel > constants.ROTATION_MAX:
            self.angle_vel = constants.ROTATION_MAX
        elif self.angle_vel < -constants.ROTATION_MAX:
            self.angle_vel = -constants.ROTATION_MAX

    def shoot(self, missiles_group):
        # global missiles_group
        a_missile = Sprite([self.get_pos()[0] + helper.angle_to_vector(self.angle)[0] * self.radius,
                                   self.get_pos()[1] + helper.angle_to_vector(self.angle)[1] * self.radius],
                                  [self.vel[0] + 5 * helper.angle_to_vector(self.angle)[0],
                                   self.vel[1] + 5 * helper.angle_to_vector(self.angle)[1]],
                                  0,
                                  0,
                                  art.missile_image,
                                  info_images.missile_info,
                                  None,
                                  None,
                                  art.missile_sound)
        missiles_group.add(a_missile)
        a_missile.sound.play()

    def shoot_bomb(self, bombs_group):
        if self.bombs > 0:
            a_bomb = Sprite([self.get_pos()[0] + helper.angle_to_vector(self.angle)[0] * self.radius,
                             self.get_pos()[1] + helper.angle_to_vector(self.angle)[1] * self.radius],
                            [self.vel[0] + 5 * helper.angle_to_vector(self.angle)[0],
                             self.vel[1] + 5 * helper.angle_to_vector(self.angle)[1]],
                            self.angle,
                            0,
                            art.bomb_image,
                            info_images.bomb_info,
                            art.explosion_bomb_image,
                            info_images.explosion_bomb_info,
                            art.missile_sound)
            bombs_group.add(a_bomb)
            self.bombs -= 1

    def explode(self, explosions_group):
        explosion = Sprite(self.pos,
                           self.vel,
                           0,
                           0,
                           self.explosion_image, self.explosion_info)
        explosions_group.add(explosion)

    def draw(self, canvas):
        if self.thrust:
            canvas.draw_image(self.image,
                              (self.image_center[0] + self.image_size[0], self.image_center[1]),
                              self.image_size,
                              self.pos,
                              self.image_size,
                              self.angle)
        else:
            canvas.draw_image(self.image,
                              self.image_center,
                              self.image_size,
                              self.pos,
                              self.image_size,
                              self.angle)

        game_functions.process_sprite_group(canvas, self.missiles_group)

    def update(self):
        self.update_position()
        self.update_velocity()
        self.update_angle()

    def get_missiles(self):
        return self.missiles_group
