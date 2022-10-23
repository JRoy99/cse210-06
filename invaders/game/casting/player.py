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
        self._gun_req = 3

    def shoot_bullets(self, cast):

        if self.get_guns() == 1:
            bullet = Bullet("^", self.get_position().add(Point(0,-3)), constants.FONT_SIZE, constants. WHITE)
            cast.add_actor("bullets", bullet)

        if self.get_guns() == 2:
            bullet = Bullet("^", self.get_position().add(Point(7,0)), constants.FONT_SIZE, constants. WHITE)
            cast.add_actor("bullets", bullet)
            bullet = Bullet("^", self.get_position().add(Point(-7,0)), constants.FONT_SIZE, constants. WHITE)
            cast.add_actor("bullets", bullet)

        if self.get_guns() == 3:
            bullet = Bullet("^", self.get_position().add(Point(3,0)), constants.FONT_SIZE, constants. WHITE)
            cast.add_actor("bullets", bullet)
            bullet = Bullet("^", self.get_position().add(Point(-7,0)), constants.FONT_SIZE, constants. WHITE)
            cast.add_actor("bullets", bullet)
            bullet = Bullet("^", self.get_position().add(Point(0,-7)), constants.FONT_SIZE, constants. WHITE)
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

    def get_gun_req(self):
        return self._gun_req

    def set_gun_req(self, gun_req):
        self._gun_req = gun_req