from typing import List

import pygame
from pygame import Surface
from pygame.event import Event

from mygame.interfaces.scene import Scene
from mygame.scenes.game_scene import GameScene
from mygame.state.game_state import GameState
from mygame.state.scene_state import SceneState
from mygame.util.fonts import BASIC_FONT


MAIN_MENU_BACKGROUND_COLOR = (200, 200, 200)

MAIN_MENU_TEXT = "Main Menu"
MAIN_MENU_TEXT_SIZE = 64


class MainMenuScene(Scene):
    """ Welcome screen of the game, the first one to be loaded."""

    def __init__(self, game_state: GameState, scene_state: SceneState):
        super().__init__(game_state, scene_state)

    def process_input(self, events: List[Event]):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.scene_state.change_scene(GameScene(self.game_state, self.scene_state))

    def update(self, time_delta: int):
        pass

    def render(self, screen: Surface):
        screen.fill(MAIN_MENU_BACKGROUND_COLOR)

        text_rect = BASIC_FONT.get_rect(MAIN_MENU_TEXT, size=MAIN_MENU_TEXT_SIZE)
        text_rect.center = screen.get_rect().center
        BASIC_FONT.render_to(screen, text_rect, MAIN_MENU_TEXT, 'black', size=MAIN_MENU_TEXT_SIZE)
