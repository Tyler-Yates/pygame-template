from abc import ABC
from typing import TYPE_CHECKING

from src.mygame.interfaces.frame_processor import FrameProcessor
from src.mygame.state.game_state import GameState

if TYPE_CHECKING:
    from src.mygame.controllers.scene_controller import SceneController


class Scene(FrameProcessor, ABC):
    """
    Only a single scene should be active at a given time.

    This is an abstract class and should be implemented by other classes.
    """

    def __init__(self, game_state: GameState, scene_controller: "SceneController"):
        super().__init__(game_state, scene_controller)
