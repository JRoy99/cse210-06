from tkinter import font
from game.casting.actor import Actor
from game.shared.point import Point

class Bullet(Actor):

    def __init__(self, text, position, font_size, color):
        self._text = text
        self._position = position
        self._font_size = font_size
        self._color = color
        self._velocity = Point(0, -15)
