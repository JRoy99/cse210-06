from game.casting.actor import Actor
from game.casting.bullet import Bullet
from game.casting.cast import Cast
from constants import *

class Player(Actor):

    def __init__(self):
        super().__init__()
        self._lives = 3
        pass

    def shoot_bullet(self, cast):
        bullet = Bullet(self.get_position())
        bullet.set_text("^")
        bullet.set_font_size(FONT_SIZE)
        bullet.set_color(WHITE)
        cast.add_actor("bullets", bullet)

    def is_alive(self):
        if self._lives > 0:
            return True
        else:
            return False
        
    def set_lives(self, lives_rem):
        self._lives= lives_rem

    def get_lives(self):
        return self._lives