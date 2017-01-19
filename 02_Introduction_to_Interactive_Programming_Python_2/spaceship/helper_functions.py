""" Helper functions"""

import math


def points_to_vector(point1, point2):
    """ Take two points and return the resulting vector (tuple)"""
    # vector_ship_target = [point2[0] - point1[0], -1* point2[1] - -1 * point1[1]]
    vector_ship_target = (point2[0] - point1[0], point2[1] - point1[1])
    return vector_ship_target


def vector_to_angle(vector):
    """ Take a vector and return angle to abscissa"""
    angle = math.atan2(vector[1], vector[0])
    return fix_angle(angle)


def angle_to_vector(ang):
    """ Take an angle and return the vector with same angle to abscissa"""
    return (math.cos(ang), math.sin(ang))


def fix_angle(angle):
    """ Take an angle and normalize it (positive, below 2 pi)"""
    while angle < 0:
        angle += 2 * math.pi
    angle %= 2 * math.pi
    return angle


def dist(p, q):
    """Take two points, return distance between them"""
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
