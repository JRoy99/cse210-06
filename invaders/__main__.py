import imp
import os
import random

import constants

from game.casting.actor import Actor
from game.casting.player import Player
from game.casting.cast import Cast
from game.casting.score import Score

from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.spawn_invaders import SpawnInvaders
from game.scripting.handle_game_over import HandleGameOver
from game.scripting.banner_update import BannerUpdate
from game.scripting.draw_actors_action import DrawActorsAction

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point



def main():
    
    # create shared services
    keyboard_service = KeyboardService(constants.CELL_SIZE)
    video_service = VideoService(constants.CAPTION, constants.MAX_X, constants.MAX_Y, 
        constants.CELL_SIZE, constants.FRAME_RATE)

    # create the cast
    cast = Cast()

    cast.add_actor("scores", Score("HIGH SCORE: ",Point(int(constants.MAX_X * .05), 0), constants.WHITE))
    cast.add_actor("scores", Score("SCORE: ",Point(int(constants.MAX_X * .05), 40), constants.WHITE))  
    cast.add_actor("scores", Score("LIVES: ",Point(int(constants.MAX_X * .8), 0), constants.WHITE))

    # create the player
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - constants.CELL_SIZE)
    position = Point(x, y)

    player = Player()
    player.set_text("#")
    player.set_font_size(constants.FONT_SIZE)
    player.set_color(constants.WHITE)
    player.set_position(position)
    cast.add_actor("players", player)

    # create the script
    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", SpawnInvaders())
    script.add_action("update", HandleGameOver())
    script.add_action("update", BannerUpdate())
    script.add_action("output", DrawActorsAction(video_service))
    
    # start the game

    director = Director(keyboard_service, video_service)

    director.start_game(cast, script)


if __name__ == "__main__":
    main()