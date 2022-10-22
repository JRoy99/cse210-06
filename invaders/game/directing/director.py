import pyray
import time
import os, sys
sys.path.append(os.path.abspath(os.path.join('..', '..', '..', '..', 'invaders')))
import __main__
from game.shared.point import Point
from game.casting.actor import Actor
import constants


DATA_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/data/highscore.txt"

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")

        self._video_service.open_window()
        while self._video_service.is_window_open() and robot.is_alive():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        time.sleep(3)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        if (velocity.get_y() == 0):
            robot.set_velocity(velocity)
        else:
            robot.shoot_bullet(cast)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        objects = cast.get_actors("objects")
        bullets = cast.get_actors("bullets")

        

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        #check and update high score
        with open(DATA_PATH,"r") as f:
            high_score = int(f.readline())
        if robot.get_score() > high_score:
            with open(DATA_PATH,"w") as f:
                f.write(str(robot.get_score()))  
        banner.set_text(f"SCORE: {robot.get_score()} HIGH SCORE: {high_score}")     
        
        #loop through objects
        for object in objects:
            try:
                #if object is sufficiently close to robot, delete object and change score
                if (abs(object.get_position().get_x() - robot.get_position().get_x()) <= 20 and 
                    abs(object.get_position().get_y() - robot.get_position().get_y()) <= 20):
                    robot.set_lives(robot.get_lives() - 1)
                    cast.remove_actor("objects", object)
            except:
                pass
            try:
                #delete objects as they exit the screen
                if object.get_position().get_y() >= max_y - 10:
                    cast.remove_actor("objects", object)
                else:
                    object.move_next(max_x, max_y)   
            except:
                pass      
        #spawn new objects up to the max number allowed on the screen
        __main__.spawn_objects(cast, len(objects))
        cast.add_actor("objects", object)

        #loop through bullets
        for bullet in bullets:
            try:
                #delete objects as they exit the screen
                if bullet.get_position().get_y() <= 5:
                    cast.remove_actor("bullets", bullet)
                else:
                    bullet.move_next(max_x, max_y)   
            except:
                pass   
        
        #detect bullet collision
        for bullet in bullets:
            for object in objects:
                try:
                    #if bullet is sufficiently close to object, delete object and change score
                    if (abs(bullet.get_position().get_x() - object.get_position().get_x()) <= 20 and 
                            abs(bullet.get_position().get_y() - object.get_position().get_y() <= 20)):
                        robot.set_score(robot.get_score() + object.get_score())
                        cast.remove_actor("objects", object)
                        cast.remove_actor("bullets", bullet)
                except:
                    pass

        #check game over
        if not(robot.is_alive()):
            self._game_over(cast)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()


    def _game_over(self, cast):
        """Handles game over events
        
        Args:
            cast (Cast): The cast of actors.
        """
        x = int(constants.MAX_X / 6)
        y = int(constants.MAX_Y / 2)
        robot = cast.get_first_actor("robots")

        position = Point(x, y-150)
        message_gameover = Actor()
        message_gameover.set_text(f"  Game Over!   \nFinal Score: {robot.get_score()}") 
        message_gameover.set_font_size(constants.FONT_SIZE)
        message_gameover.set_position(position)
        message_gameover.set_color(constants.RED)
        cast.add_actor("messages", message_gameover)
