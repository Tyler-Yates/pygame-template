from dataclasses import dataclass, field
from typing import List

from src.mygame.state.asteroid_actor import Asteroid
from src.mygame.state.player_actor import Player


@dataclass
class GameState:
    """
    Class meant to hold the entire game state.
    """

    level: int = 1
    score: int = 0

    player: Player = Player()
    asteroids: List[Asteroid] = field(default_factory=list)
