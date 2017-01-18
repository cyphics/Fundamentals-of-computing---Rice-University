import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import constants
import game


class Frame:

    def __init__(self):
        self._frame = simplegui.create_frame("Asteroids", constants.WIDTH, constants.HEIGHT)
        self._game = game.Game()
        self._frame.set_draw_handler(self._game.run)
        self._frame.set_keydown_handler(self.keydown_handler)
        self._frame.set_keyup_handler(self.keyup_handler)
        self._frame.set_mouseclick_handler(self.mouseclick)
        self._timer = simplegui.create_timer(1000.0, self._game.rock_spawner)
        self._timer.start()
        self._frame.start()

    def keydown_handler(self, key):
        if key == simplegui.KEY_MAP["left"]:
            self._game.key_down("left")
        if key == simplegui.KEY_MAP["right"]:
            self._game.key_down("right")
        if key == simplegui.KEY_MAP["up"]:
            self._game.key_down("up")
        if key == simplegui.KEY_MAP["space"]:
            self._game.key_down("space")
        if key == simplegui.KEY_MAP["f"]:
            self._game.key_down("f")
        if key == simplegui.KEY_MAP["q"]:
            self._timer.stop()
            self._frame.stop()

    def keyup_handler(self, key):
        if key == simplegui.KEY_MAP["right"]:
            self._game.key_up("right")
        elif key == simplegui.KEY_MAP["left"]:
            self._game.key_up("left")
        elif key == simplegui.KEY_MAP["up"]:
            self._game.key_up("up")

    def mouseclick(self, pos):
        if pos:
            self._game.click()
