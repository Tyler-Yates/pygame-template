from typing import List

import pygame
from pygame.event import Event
from pygame.surface import Surface

from interfaces.overlay import Overlay
from state.game_state import GameState
from state.scene_state import SceneState
from util.fonts import BASIC_FONT


TOGGLE_HOTKEY = pygame.K_F12


class PerformanceOverlay(Overlay):
    """
    Displays performance information for the game.

    This information can be toggled by pressing F12.
    """

    def __init__(self, game_state: GameState, scene_state: SceneState):
        super().__init__(game_state, scene_state)

        self.show_fps = True
        self.time_delta = 0

    def process_input(self, events: List[Event]):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == TOGGLE_HOTKEY:
                    self.show_fps = not self.show_fps

    def update(self, time_delta: float):
        self.time_delta = int(time_delta * 1000)

    def render(self, screen: Surface):
        if self.show_fps:
            BASIC_FONT.render_to(screen, (screen.get_width() - 20, 5), f"{self.time_delta}", "red", size=14)
