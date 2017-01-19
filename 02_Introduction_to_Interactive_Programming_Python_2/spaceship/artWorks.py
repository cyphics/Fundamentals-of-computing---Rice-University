"""
Load all the artworks
"""

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                  debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_image = simplegui.load_image("/home/cyphix/programmation/fundamentals/python2/assignments/spaceship/art/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_image = simplegui.load_image("/home/cyphix/programmation/fundamentals/python2/assignments/spaceship/art/nebula_blue.f2014.png")

# splash image
splash_image = simplegui.load_image("/home/cyphix/programmation/fundamentals/python2/assignments/spaceship/art/splash.png")

# my_ship image
# ship_image = simplegui.load_image("/home/cyphix/programmation/fundamentals/python2/assignments/spaceship/art/double_ship.png")
ship_image = simplegui.load_image("/home/cyphix/programmation/fundamentals/python2/assignments/spaceship/art/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_image = simplegui.load_image("/home/cyphix/programmation/fundamentals/python2/assignments/spaceship/art/shot2.png")


bomb_image = simplegui.load_image("/home/cyphix/programmation/fundamentals/python2/assignments/spaceship/art/shot3.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_image = simplegui.load_image("/home/cyphix/programmation/fundamentals/python2/assignments/spaceship/art/asteroid_blue.png")
rock_image = simplegui.load_image("/home/cyphix/programmation/fundamentals/python2/assignments/spaceship/art/asteroid1.opengameart.warspawn.png")


# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_alpha_image = simplegui.load_image("/home/cyphix/programmation/fundamentals/python2/assignments/spaceship/art/explosion_alpha.png")
explosion_mega_image = simplegui.load_image("/home/cyphix/programmation/fundamentals/python2/assignments/spaceship/art/explosion.hasgraphics.png")

explosion_bomb_image = simplegui.load_image("https://cyphix.org/explosion.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
soundtrack.set_volume(0.5)

missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)

soundtrack.play()
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
# soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")
