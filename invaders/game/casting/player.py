from game.casting.actor import Actor
from game.casting.bullet import Bullet
from game.casting.cast import Cast
from game.shared.point import Point
import constants

class Player(Actor):

    def __init__(self):
        super().__init__()
        self._lives = 3
        self._boss_flag = False
        self._guns = 1

    def shoot_bullets(self, cast):

        bullet = Bullet("^", self.get_position().add(Point(32,-3)), constants.FONT_SIZE, constants.WHITE)
        cast.add_actor("bullets", bullet)

        if self.get_guns() > 1:
            for n in range(2, self.get_guns()+1):
                if n % 2 == 0:
                    bullet = Bullet("^", self.get_position().add(Point((3*n)+32,-3+n)), constants.FONT_SIZE, constants.WHITE)
                else:
                    bullet = Bullet("^", self.get_position().add(Point((-3*(n-1))+32,-3+(n-1))), constants.FONT_SIZE, constants.WHITE)
                cast.add_actor("bullets", bullet)

    def is_alive(self):
        if self._lives > 0:
            return True
        else:
            return False
        
    def set_lives(self, lives_rem):
        self._lives = lives_rem

    def get_lives(self):
        return self._lives

    def get_boss_flag(self):
        return self._boss_flag

    def set_boss_flag(self, bool_val):
        self._boss_flag = bool_val

    def get_guns(self):
        return self._guns

    def set_guns(self, guns):
        self._guns = guns
