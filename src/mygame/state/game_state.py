from typing import List

from src.mygame.state.asteroid_actor import Asteroid
from src.mygame.state.player_actor import Player


class GameState:
    """
    Class meant to hold the entire game state.
    """

    def __init__(self):
        self.score = 0

        self.player = Player()
        self.asteroids: List[Asteroid] = []
