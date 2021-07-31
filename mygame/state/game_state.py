from dataclasses import dataclass


@dataclass
class GameState:
    """
    Class meant to hold all state that should be saved.
    """

    level: int = 1
    score: int = 0
