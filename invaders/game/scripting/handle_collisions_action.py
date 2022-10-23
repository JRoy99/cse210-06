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

        player = cast.get_first_actor("players")
        bullets = cast.get_actors("bullets")
        invaders = cast.get_actors("invaders")

        #loop through invaders
        for invader in invaders:
            try:
                #if invader is sufficiently close to player, delete invader and change score
                difference = invader.get_position().subtract(player.get_position())
                if (difference.get_x() <= 60 and difference.get_x() >= -15 and 
                    abs(difference.get_y()) <= 20):
                    player.set_lives(player.get_lives() - 1)
                    cast.remove_actor("invaders", invader)
            except:
                pass

        #detect bullet collision
        for bullet in bullets:
            for invader in invaders:
                try:
                    #if bullet is sufficiently close to invader, delete bullet, change score, decrement invader lives
                    difference = bullet.get_position().subtract(invader.get_position())  
                    if difference.get_y() <= 10:
                        if difference.get_x() <= 60 and difference.get_x() >= -15:
                            player.set_score(player.get_score() + invader.get_score())
                            cast.remove_actor("bullets", bullet)

                            invader.set_lives(invader.get_lives() - 1)
                            invader.set_text(f"-{invader.get_lives()}-")
                            if not(invader.is_alive()):
                                cast.remove_actor("invaders", invader)   
                except:
                    pass