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

BACKGROUND_COLOR = (0, 0, 0)

GAME_OVER_TEXT = "Game Over"
MAIN_MENU_TEXT_SIZE = 64
SCORE_TEXT_SIZE = 32
CONTINUE_TEXT_SIZE = 24


class GameOverScene(Scene):
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
                    # Reset the game state since the game is over
                    self.game_state.__init__()
                    self.scene_controller.change_active_scene(SceneEnum.MainMenu)

    def update(self, time_delta: float):
        pass

    def render(self, screen: Surface):
        screen.fill(BACKGROUND_COLOR)

        screen_center = screen.get_rect().center

        # Game over text
        text_rect = BASIC_FONT.get_rect(GAME_OVER_TEXT, size=MAIN_MENU_TEXT_SIZE)
        text_rect.center = screen_center
        BASIC_FONT.render_to(screen, text_rect, GAME_OVER_TEXT, "white", size=MAIN_MENU_TEXT_SIZE)

        # Score text
        score_text = f"Your score: {self.game_state.score}"
        score_text_rect = BASIC_FONT.get_rect(score_text, size=SCORE_TEXT_SIZE)
        score_text_rect.center = (screen_center[0], screen_center[1] - 100)
        BASIC_FONT.render_to(screen, score_text_rect, score_text, "white", size=SCORE_TEXT_SIZE)

        # Press Enter to continue
        continue_text = "Press Enter to go back to Main Menu"
        continue_text_rect = BASIC_FONT.get_rect(continue_text, size=CONTINUE_TEXT_SIZE)
        continue_text_rect.center = (screen_center[0], screen_center[1] + 150)
        BASIC_FONT.render_to(screen, continue_text_rect, continue_text, "white", size=CONTINUE_TEXT_SIZE)
