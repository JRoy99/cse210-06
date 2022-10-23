import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the bike.
    
    The responsibility of ControlActorsAction is to get the direction and move the bike's bike.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        
        if (velocity.get_y() == 0):
            robot.set_velocity(velocity)
        else:
            robot.shoot_bullet(cast)