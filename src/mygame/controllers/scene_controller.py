from src.mygame.constants.scene_enum import SceneEnum
from src.mygame.frameprocessors.game_scene import GameScene
from src.mygame.frameprocessors.main_menu_scene import MainMenuScene
from src.mygame.interfaces.scene import Scene
from src.mygame.state.game_state import GameState


class SceneController:
    """
    Class to manage the active scene of the game.
    """

    def __init__(self, game_state: GameState):
        self.game_state = game_state

        # Default to Main Menu
        self.active_scene: Scene = self._get_scene_object(SceneEnum.MainMenu)

    def _get_scene_object(self, scene_id: SceneEnum) -> Scene:
        if scene_id == SceneEnum.MainMenu:
            return MainMenuScene(self.game_state, self)
        if scene_id == SceneEnum.Game:
            return GameScene(self.game_state, self)

    def get_active_scene(self) -> Scene:
        return self.active_scene

    def change_active_scene(self, next_scene: SceneEnum):
        self.active_scene = self._get_scene_object(next_scene)