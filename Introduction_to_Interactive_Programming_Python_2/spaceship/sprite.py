import helper_functions as helper
import artWorks as art
import constants


# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, explosion_image=None, explosion_info=None, sound=None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        self.explosion_image = explosion_image
        self.explosion_info = explosion_info
        if sound:
            self.sound = sound
            self.sound.rewind()
            self.sound.play()

    def get_pos(self):
        return self.pos

    def get_radius(self):
        return self.radius

    def set_pos(self, position):
        for i in range(2):
            self.pos[i] = position[i]

    def set_vel(self, velocity):
        for i in range(2):
            self.vel[i] = velocity[i]

    def collide(self, other_object):
        if not self == other_object:
            if helper.dist(self.get_pos(), other_object.get_pos()) < self.get_radius() + other_object.get_radius():
                return True

    def explode(self, explosions_group):
        try:
            self.explosion_image
        except NameError:
            pass
        else:
            explosion = Sprite(self.get_pos(),
                               (0, 0),
                               0,
                               0,
                               self.explosion_image, self.explosion_info)
            explosions_group.add(explosion)

    def draw(self, canvas):
        canvas.draw_image(self.image,
                          self.image_center,
                          self.image_size,
                          self.pos,
                          self.image_size,
                          self.angle)

    def update(self):
        self.age += 1
        if self.age >= self.lifespan:
            return True
        elif not self.animated:
            self.angle += self.angle_vel
        else:
            # Specify explosion animation according to image file
            if self.image == art.explosion_mega_image:
                current_sprite_index = [self.age % constants.EXPLOSION_DIM[0],
                                        (self.age // constants.EXPLOSION_DIM[0]) % constants.EXPLOSION_DIM[1]]
                current_sprite_center = [constants.EXPLOSION_CENTER[0] + current_sprite_index[0] * constants.EXPLOSION_SIZE[0],
                                         constants.EXPLOSION_CENTER[1] + current_sprite_index[1] * constants.EXPLOSION_SIZE[1]]

                self.image_center = current_sprite_center

            elif self.image == art.explosion_bomb_image:
                current_sprite_index = [self.age % constants.BOMB_DIM[0],
                                        (self.age // constants.BOMB_DIM[0]) % constants.BOMB_DIM[1]]
                current_sprite_center = [constants.BOMB_CENTER[0] + current_sprite_index[0] * constants.BOMB_SIZE[0],
                                         constants.BOMB_CENTER[1] + current_sprite_index[1] * constants.BOMB_SIZE[1]]

                self.image_center = current_sprite_center

            else:
                current_sprite_index = ((self.age * 0.4) % constants.ROCK_DIM) // 1
                current_sprite_center = [constants.ROCK_CENTER[0] + current_sprite_index * constants.ROCK_SIZE[0], constants.ROCK_CENTER[1]]
                self.image_center = current_sprite_center
        for i in range(2):
            self.pos[i] = (self.pos[i] + self.vel[i]) % constants.CANVAS_SIZE[i]

        return False
