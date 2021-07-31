from typing import List, TYPE_CHECKING

import pygame
from pygame import Surface
from pygame.event import Event

from src.mygame.constants.scene_enum import SceneEnum
from src.mygame.interfaces.scene import Scene
from src.mygame.state.game_state import GameState
from src.mygame.util.fonts import BASIC_FONT

if TYPE_CHECKING:
    from src.mygame.controllers.scene_controller import SceneController

MAIN_MENU_BACKGROUND_COLOR = (200, 200, 200)

MAIN_MENU_TEXT = "Main Menu"
MAIN_MENU_TEXT_SIZE = 64


class MainMenuScene(Scene):
    """
    Main menu of the game.
    """

    def __init__(self, game_state: GameState, scene_controller: "SceneController"):
        super().__init__(game_state, scene_controller)

    def process_input(self, events: List[Event]):
        for event in events:
            if event.type == pygame.KEYDOWN:
                # Pressing Return will take you to the game
                if event.key == pygame.K_RETURN:
                    self.scene_controller.change_active_scene(SceneEnum.Game)

    def update(self, time_delta: float):
        pass

    def render(self, screen: Surface):
        screen.fill(MAIN_MENU_BACKGROUND_COLOR)

        text_rect = BASIC_FONT.get_rect(MAIN_MENU_TEXT, size=MAIN_MENU_TEXT_SIZE)
        text_rect.center = screen.get_rect().center
        BASIC_FONT.render_to(screen, text_rect, MAIN_MENU_TEXT, "black", size=MAIN_MENU_TEXT_SIZE)
