import constants

from game.casting.actor import Actor
from game.shared.point import Point


class Invader(Actor):
    """A falling invader which increment or decrement points when touched in the game. Subclass of Actor.
    
    The responsibility of invader is to keep track of its appearance, position, and text message
        Inherited attributes:
            _text (string): The text to display
            _font_size (int): The font size to use.
            _color (Color): The color of the text.
            _position (Point): The screen coordinates.
            _velocity (Point): The speed and direction.
            _score: The number of points an invader has/is worth
    """
    
    def __init__(self, strength, isBoss, position):
        """Constructs a new invader"""
        super().__init__()
        self._lives = strength
        self._boss = isBoss
        self.set_color(constants.RED)
        self.set_velocity(Point(0, int(strength/2+1)))
        self.set_font_size(constants.FONT_SIZE)

        if isBoss:
            self._boss_gen()

        self.set_text(f"-{self.get_lives()}-")
        self.set_position(position)
        

    def is_alive(self):
        if self._lives > 0:
            return True
        else:
            return False
        
    def set_lives(self, lives_rem):
        self._lives = lives_rem

    def get_lives(self):
        return self._lives

    def is_boss_enemy(self):
        return self._boss

    def _boss_gen(self):
        self.set_velocity(Point(0, int(self.get_lives() + 1)))
        self.set_lives(int((self.get_lives() + 3) ** 1.5))
        self.set_color(constants.PURPLE)
        self.set_font_size(int(constants.FONT_SIZE * 2))