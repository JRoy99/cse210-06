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
      x = random.randint(1, int(constants.COLS - 1))
      y = random.randint(1, int((constants.ROWS - 1)/5))
      position = Point(x, y)
      position = position.scale(constants.CELL_SIZE)

      strength = random.randint(int(player.get_score() ** 0.3), int(player.get_score() ** .4))

      if strength < 1:
        strength = 1

      if player.get_boss_flag():
        invader = Invader(strength, True, position)
        player.set_boss_flag(False)
        cast.add_actor("bosses", invader)
        cast.add_actor("invaders", invader)

      else:
        invader = Invader(strength, False, position)
        cast.add_actor("invaders", invader)
