from dataclasses import dataclass

from mygame.state.player_state import PlayerState


@dataclass
class GameState:
    """
    Class meant to hold the entire game state.
    """

    level: int = 1
    score: int = 0

    player: PlayerState = PlayerState()
