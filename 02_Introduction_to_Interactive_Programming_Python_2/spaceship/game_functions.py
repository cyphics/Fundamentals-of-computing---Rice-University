import random
import constants
import helper_functions as helper
import artWorks as art


def get_random_point(ship):
    """ Return a random point on the canvas"""
    point = [0, 0]
    for i in range(2):
        point[i] = random.random() * constants.CANVAS_SIZE[i]
    if helper.dist(point, ship.get_pos()) < ship.get_radius() * 4:
        point = get_random_point(ship)
    return point


def get_random_velocity(max_speed):
    """ Return a random velocity"""
    velocity = [0, 0]
    for i in range(2):
        velocity[i] = (random.random() * 2 - 1) * max_speed
    return velocity


def process_sprite_group(canvas, group):
    """ Function that draws all the sprites of the given group on the canvas"""
    group_copy = set(group)
    for sprite in group_copy:
        sprite.draw(canvas)
        if sprite.update():
            group.remove(sprite)


def group_collide(group, other_object, explosion_group):
    """ Test collisions between a group of sprites and a single other sprite"""
    group_copy = set(group)
    for object in group_copy:
        if object.collide(other_object):
            # If bomb, destroy all objects in radius
            if other_object.image == art.bomb_image:
                other_object.explode(explosion_group)
                art.explosion_sound.play()
                for object2 in group_copy:
                    if helper.dist(object2.pos, other_object.pos) < 111:
                        object2.explode(explosion_group)
                        group.remove(object2)
            else:
                object.explode(explosion_group)
                group.remove(object)
            return True


def group_group_collide(first_group, second_group, explosion_group):
    """ Test collision between two groups of sprites"""
    collided_objects = 0
    copy_first_group = set(first_group)
    for first_object in copy_first_group:
        if group_collide(second_group, first_object, explosion_group):
                first_group.discard(first_object)
                collided_objects += 1
    return collided_objects
