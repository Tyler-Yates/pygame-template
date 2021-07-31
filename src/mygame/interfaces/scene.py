from abc import ABC

from src.mygame.interfaces.frame_processor import FrameProcessor
from src.mygame.state.game_state import GameState
from src.mygame.state.scene_state import SceneState


class Scene(FrameProcessor, ABC):
    """
    Only a single scene should be active at a given time.

    This is an abstract class and should be implemented by other classes.
    """

    def __init__(self, game_state: GameState, scene_state: SceneState):
        super().__init__(game_state, scene_state)
