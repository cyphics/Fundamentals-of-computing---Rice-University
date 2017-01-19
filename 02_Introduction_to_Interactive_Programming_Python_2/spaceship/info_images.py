"""
Store artworks informations
"""

import imageInfo as info
import constants

debris_info = info.ImageInfo([320, 240], [640, 480])
nebula_info = info.ImageInfo([400, 300], [800, 600])
splash_info = info.ImageInfo([200, 150], [400, 300])
ship_info = info.ImageInfo([45, 45], [90, 90], 35)
missile_info = info.ImageInfo([5, 5], [10, 10], 3, 50)
bomb_info = info.ImageInfo([10, 10], [20, 20], 6, 0)
asteroid_info = info.ImageInfo([45, 45], [90, 90], 40)
rock_info = info.ImageInfo(constants.ROCK_CENTER, constants.ROCK_SIZE, 50, None, True)
explosion_alpha_info = info.ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_mega_info = info.ImageInfo(constants.EXPLOSION_CENTER, constantsl.EXPLOSION_SIZE, 40, 40, True)
explosion_bomb_info = info.ImageInfo([111, 111], [222, 222], 40, 40, True)
