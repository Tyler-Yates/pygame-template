from abc import ABC
from typing import TYPE_CHECKING

from src.mygame.interfaces.frame_processor import FrameProcessor
from src.mygame.state.game_state import GameState

if TYPE_CHECKING:
    from src.mygame.controllers.scene_controller import SceneController


class Overlay(FrameProcessor, ABC):
    """
    Represents a single overlay. There can be multiple overlays active at one time.
    """

    def __init__(self, game_state: GameState, scene_controller: "SceneController"):
        super().__init__(game_state, scene_controller)
