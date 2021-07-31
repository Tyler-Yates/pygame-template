# Avoid cyclic imports since we only want these for type checking
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from interfaces.scene import Scene


class SceneState:
    """
    This class is meant to manage the state of the game's active scene.
    """

    def __init__(self):
        self.active_scene = None

    def get_active_scene(self) -> "Scene":
        return self.active_scene

    def change_scene(self, next_scene: "Scene"):
        self.active_scene = next_scene
