from typing import List

from src.mygame.state.asteroid_actor import Asteroid
from src.mygame.state.hiscore_state import HiscoreState
from src.mygame.state.player_actor import Player


class GameState:
    """
    Class meant to hold the entire game state.
    """

    def __init__(self):
        self.score = 0

        self.player = Player()
        self.asteroids: List[Asteroid] = []

        self.hiscores = HiscoreState()

    def reset(self):
        """
        Method to be called whenever the game state should be reset, for example starting a new game.
        """
        self.score = 0

        self.player = Player()
        self.asteroids: List[Asteroid] = []

        # We do not need to reset the hiscore as that is persistent
