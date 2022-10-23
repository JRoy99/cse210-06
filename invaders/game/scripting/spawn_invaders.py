import random
import constants
from game.shared.point import Point
from game.casting.invader import Invader

from game.scripting.action import Action

class SpawnInvaders(Action):
  
  def execute(self, cast, script):

    invaders = cast.get_actors("invaders")
    player = cast.get_first_actor("players")

    # create the invaders
    for n in range(len(invaders), constants.MAX_INVADERS):
      x = random.randint(1, constants.COLS - 1)
      y = random.randint(1, int((constants.ROWS - 1)/5))
      position = Point(x, y)
      position = position.scale(constants.CELL_SIZE)

      color = constants.RED

      strength = random.randint(int(player.get_score() ** 0.3), int(player.get_score() ** .4))

      if strength < 1:
        strength = 1

      invader = Invader(strength)
      invader.set_text(f"-{invader.get_lives()}-")
      invader.set_score(1)


      invader.set_font_size(constants.FONT_SIZE)
      invader.set_color(color)
      invader.set_position(position)
      invader.set_velocity(Point(0, strength))

      cast.add_actor("invaders", invader)