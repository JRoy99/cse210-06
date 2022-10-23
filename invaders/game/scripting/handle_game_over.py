import constants

from game.shared.point import Point
from game.scripting.action import Action
from game.casting.actor import Actor

class HandleGameOver(Action):
  
  def execute(self, cast, script):

    robot = cast.get_first_actor("robots")

    if robot.is_alive():
        return

    x = int(constants.MAX_X / 4)
    y = int(constants.MAX_Y / 2)
    robot = cast.get_first_actor("robots")

    position = Point(x+20, y-150)
    message_gameover = Actor()
    message_gameover.set_text(f"  Game Over!   \nFinal Score: {robot.get_score()}") 
    message_gameover.set_font_size(constants.FONT_SIZE)
    message_gameover.set_position(position)
    message_gameover.set_color(constants.RED)
    cast.add_actor("messages", message_gameover)
