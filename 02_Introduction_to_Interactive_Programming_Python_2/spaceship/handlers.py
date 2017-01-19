import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


def keydown_handler(key):
    global my_ship
    if in_game:
        if key == simplegui.KEY_MAP["left"]:
            my_ship.turn("Left")
        if key == simplegui.KEY_MAP["right"]:
            my_ship.turn("Right")
        if key == simplegui.KEY_MAP["up"]:
            my_ship.accelerate(True)
        if key == simplegui.KEY_MAP["space"]:
            my_ship.shoot()
        if key == simplegui.KEY_MAP["f"]:
            my_ship.shoot_bomb()


def keyup_handler(key):
    global my_ship
    if key == simplegui.KEY_MAP["right"]:
        my_ship.turn("No")
    elif key == simplegui.KEY_MAP["left"]:
        my_ship.turn("No")
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.accelerate(False)


def mouseclick(pos):
    global in_game, tuto, ships_group, missiles_group, tuto_done, explosions_group, rock_group, bomb_group
    if pos:
        if not in_game:
            # Avoid repeating tuto after death
            if tuto is False and tuto_done is False:
                tuto = True
            # Start game
            else:
                ships_group = []
                missiles_group = set()
                explosions_group = set()
                rock_group = set()
                bomb_group = set()
                tuto = False
                tuto_done = True
                in_game = True
