import constants

from game.shared.point import Point
from game.scripting.action import Action
from game.casting.actor import Actor

class HandleGameOver(Action):
  
  def execute(self, cast, script):

    player = cast.get_first_actor("players")

    if player.is_alive():
        return

    x = int(constants.MAX_X / 4)
    y = int(constants.MAX_Y / 2)
    player = cast.get_first_actor("players")

    position = Point(x+20, y-150)
    message_gameover = Actor()
    message_gameover.set_text(f"  Game Over!   \nFinal Score: {player.get_score()}") 
    message_gameover.set_font_size(constants.FONT_SIZE)
    message_gameover.set_position(position)
    message_gameover.set_color(constants.RED)
    cast.add_actor("messages", message_gameover)
