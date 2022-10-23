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
      x = random.randint(3, int(constants.COLS - 3))
      y = random.randint(1, int((constants.ROWS - 1)/8))
      position = Point(x, y)
      position = position.scale(constants.CELL_SIZE)

      strength_range = [int(player.get_score() ** 0.25)-1, int(player.get_score() ** .35)-1]

      if strength_range[0] < 1:
        strength_range[0] = 1

      if strength_range[1] < 1:
        strength_range[1] = 1

      if player.get_boss_flag():
        invader = Invader(strength_range, True, position, player.get_position(), type = 0, )
        player.set_boss_flag(False)
        cast.add_actor("bosses", invader)
        cast.add_actor("invaders", invader)

      else:
        type = random.randint(1,3)
        invader = Invader(strength_range, False, position, player.get_position(), type)
        cast.add_actor("invaders", invader)
