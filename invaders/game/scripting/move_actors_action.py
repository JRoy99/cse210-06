from game.scripting.action import Action
import constants

class MoveActorsAction(Action):
    """
    An update action that handles actor movement.
    
    The responsibility of MoveActorsAction is to iterate through all move_next() methods for actors. 
    """
    def execute(self, cast, script):
        """Executes move_next() method for all actors

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        player = cast.get_first_actor("players")
        bullets = cast.get_actors("bullets")
        invaders = cast.get_actors("invaders")
        bosses = cast.get_actors("bosses")

        player.move_next(constants.MAX_X, constants.MAX_Y)

        for bullet in bullets:
            try:
                #delete bullets as they exit the screen
                if bullet.get_position().get_y() <= 15:
                    cast.remove_actor("bullets", bullet)
                else:
                    bullet.move_next(constants.MAX_X, constants.MAX_Y)   
            except:
                pass

        for invader in invaders:
            try:
                #delete invaders as they exit the screen
                if invader.get_position().get_y() >= constants.MAX_Y - 20:
                    cast.remove_actor("invaders", invader)
                    if invader in bosses:
                        cast.remove_actor("bosses", invader)
                else:
                    invader.move_next(constants.MAX_X, constants.MAX_Y)   
            except:
                pass
