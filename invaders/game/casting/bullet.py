from game.casting.actor import Actor
from game.shared.point import Point

class Bullet(Actor):

    def __init__(self, position):
        self._position = position.add(Point(0,-1))
        self._velocity = Point(0, -5)
