import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the bike collides
    with the food, or the bike collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self.winner = ""

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        robot = cast.get_first_actor("robots")
        bullets = cast.get_actors("bullets")
        objects = cast.get_actors("objects")

        #loop through objects
        for object in objects:
            try:
                #if object is sufficiently close to robot, delete object and change score
                difference = object.get_position().subtract(robot.get_position())
                if (difference.get_x() <= 60 and difference.get_x() >= -15 and 
                    abs(difference.get_y()) <= 20):
                    robot.set_lives(robot.get_lives() - 1)
                    cast.remove_actor("objects", object)
            except:
                pass

        #detect bullet collision
        for bullet in bullets:
            for object in objects:
                try:
                    #if bullet is sufficiently close to object, delete bullet, change score, decrement object lives
                    difference = bullet.get_position().subtract(object.get_position())  
                    if difference.get_y() <= 10:
                        if difference.get_x() <= 60 and difference.get_x() >= -15:
                            robot.set_score(robot.get_score() + object.get_score())
                            cast.remove_actor("bullets", bullet)

                            object.set_lives(object.get_lives() - 1)
                            object.set_text(f"-{object.get_lives()}-")
                            if not(object.is_alive()):
                                cast.remove_actor("objects", object)   
                except:
                    pass