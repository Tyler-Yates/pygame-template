from abc import ABC

from mygame.interfaces.frame_processor import FrameProcessor
from mygame.state.game_state import GameState
from mygame.state.scene_state import SceneState


class Overlay(FrameProcessor, ABC):
    """
    Represents a single overlay. There can be multiple overlays active at one time.
    """

    def __init__(self, game_state: GameState, scene_state: SceneState):
        super().__init__(game_state, scene_state)
