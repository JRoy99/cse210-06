import random
import constants
from game.shared.point import Point
from game.casting.invader import Object

from game.scripting.action import Action

class SpawnInvaders(Action):
  
  def execute(self, cast, script):

    objects = cast.get_actors("objects")
    robot = cast.get_first_actor("robots")

    # create the objects
    for n in range(len(objects), constants.MAX_OBJECTS):
      x = random.randint(1, constants.COLS - 1)
      y = random.randint(1, int((constants.ROWS - 1)/5))
      position = Point(x, y)
      position = position.scale(constants.CELL_SIZE)

      color = constants.RED

      strength = random.randint(int(robot.get_score() ** 0.3), int(robot.get_score() ** .4))

      if strength < 1:
        strength = 1

      object = Object(strength)
      object.set_text(f"-{object.get_lives()}-")
      object.set_score(1)


      object.set_font_size(constants.FONT_SIZE)
      object.set_color(color)
      object.set_position(position)
      object.set_velocity(Point(0, strength))

      cast.add_actor("objects", object)