# Avoid cyclic imports since we only want these for type checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mygame.state.game_state import GameState
    from mygame.state.scene_state import SceneState


class Scene:
    """Represents a scene of the game.

    Scenes must be created inheriting this class attributes
    in order to be used afterwards as menus, introduction screens,
    etc."""

    def __init__(self, game_state: 'GameState', scene_state: 'SceneState'):
        self.game_state = game_state
        self.scene_state = scene_state

    def process_input(self, events):
        raise NotImplementedError("Subclass must implement.")

    def update(self, time_delta: int):
        raise NotImplementedError("Subclass must implement.")

    def render(self, screen):
        raise NotImplementedError("Subclass must implement.")
