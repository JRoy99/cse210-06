import os
import random

import constants

from game.casting.actor import Actor
from game.casting.invader import Object
from game.casting.player import Player
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


def spawn_objects(cast, current_objects):
# create the objects

    for n in range(current_objects, constants.MAX_OBJECTS):
        x = random.randint(1, constants.COLS - 1)
        y = random.randint(1, int((constants.ROWS - 1)/5))
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)

        color = constants.RED
        
        object = Object()
        object.set_text("o")

        #Set score values
        if object.get_text() == "*":            
            object.set_score(random.randint(1, 5))
        else:
            object.set_score(random.randint(-5, -1))

        object.set_font_size(constants.FONT_SIZE)
        object.set_color(color)
        object.set_position(position)
        object.set_velocity(Point(0, abs(object.get_score())))


        cast.add_actor("objects", object)

def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(constants.FONT_SIZE)
    banner.set_color(constants.WHITE)
    banner.set_position(Point(constants.CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - constants.CELL_SIZE)
    position = Point(x, y)

    robot = Player()
    robot.set_text("#")
    robot.set_font_size(constants.FONT_SIZE)
    robot.set_color(constants.WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    spawn_objects(cast, 0, 0)
    
    # start the game
    keyboard_service = KeyboardService(constants.CELL_SIZE)
    video_service = VideoService(constants.CAPTION, constants.MAX_X, constants.MAX_Y, 
        constants.CELL_SIZE, constants.FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()