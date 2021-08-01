from typing import List

from src.mygame.state.asteroid_actor import Asteroid
from src.mygame.state.high_score_state import HighScoreState
from src.mygame.state.player_actor import Player


class GameState:
    """
    Class meant to hold the entire game state.
    """

    def __init__(self):
        self.score = 0

        self.player = Player()
        self.asteroids: List[Asteroid] = []

        self.high_scores = HighScoreState()

    def reset(self):
        """
        Method to be called whenever the game state should be reset, for example starting a new game.
        """
        self.score = 0

        self.player = Player()
        self.asteroids: List[Asteroid] = []

        # We do not need to reset the high scores as that is persistent
