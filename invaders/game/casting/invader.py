import constants
import random

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
    
    def __init__(self, strength_range, isBoss, position, player_position, type):
        """Constructs a new invader"""
        super().__init__()
        self._lives = random.randint(strength_range[0], strength_range[1])
        self._boss = isBoss
        self._type = type
        self.set_position(position)
        
        self._type_gen(type, player_position)
        self.set_font_size(int(constants.FONT_SIZE/1.5))

        if isBoss:
            self._boss_gen(strength_range)
        
        self.set_text(f"-{self.get_lives()}-")
        

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

    def _boss_gen(self, strength_range):
        self.set_lives(strength_range[1])
        self.set_velocity(Point(0, int(self.get_lives() / 2)))
        self.set_lives(int((self.get_lives() + 2) ** 1.5))
        self.set_color(constants.PURPLE)
        self.set_font_size(int(constants.FONT_SIZE * 1.5))

        if abs(self.get_velocity().get_y()) > 5:
            self.set_velocity(Point(0, 5))

    def _type_gen(self, type, player_position):

        #Fast Type
        if type == 1:
            self.set_color(constants.ORANGE)
            total_velocity = int(self.get_lives()/(1.5)+1)
            if total_velocity > 12:
                total_velocity = 12

            self.set_velocity(Point(0, total_velocity))

        #Diagonal Type
        if type == 2:
            self.set_color(constants.YELLOW)
            total_velocity = int(self.get_lives()/(1.5)+3)
            if total_velocity > 15:
                total_velocity = 15

            x_vel = random.choice([-9, 9])/12 * total_velocity 
            y_vel = total_velocity - abs(x_vel)

            self.set_velocity(Point(x_vel, y_vel))


        #Targeted Type
        if type == 3:
            self.set_color(constants.RED)

            total_velocity = int(self.get_lives()/(1.75)+1)
            if total_velocity > 10:
                total_velocity = 10

            y_dist = (player_position.get_y() - self.get_position().get_y())
            x_dist = (player_position.get_x() - self.get_position().get_x())
            h_dist = (x_dist ** 2 + y_dist ** 2) ** .5

            x_vel = total_velocity * (x_dist / h_dist)
            y_vel = total_velocity * (y_dist / h_dist)
 
            self.set_velocity(Point(x_vel, y_vel))
            print(f"{x_vel}/{x_dist}/{self.get_position().get_x()} -- {player_position.get_x()}" )

    def get_type(self):
        return self._type
