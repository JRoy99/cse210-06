import os, sys
sys.path.append(os.path.abspath(os.path.join('..', '..', '..', '..', 'invaders')))

import constants

from game.shared.point import Point
from game.scripting.action import Action
from game.casting.actor import Actor

DATA_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/data/highscore.txt"


class BannerUpdate(Action):
  
  def execute(self, cast, script):
    player = cast.get_first_actor("players")
    scores = cast.get_actors("scores")

    with open(DATA_PATH,"r") as f:
        high_score = int(f.readline())
        if player.get_score() > high_score:
            with open(DATA_PATH,"w") as f:
                f.write(str(player.get_score()))

    for score in scores:
      score.set_text("")

    scores[0].set_text(f"HIGH SCORE: {high_score}")
    scores[1].set_text(f"SCORE: {player.get_score()}")
    scores[2].set_text(f"LIVES: {player.get_lives()}")