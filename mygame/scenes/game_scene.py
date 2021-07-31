from typing import List

import pygame
from pygame import Surface
from pygame.event import Event

from mygame.interfaces.scene import Scene
from mygame.state.game_state import GameState
from mygame.state.scene_state import SceneState
from mygame.util.fonts import BASIC_FONT

BACKGROUND_COLOR = (50, 50, 50)

SCORE_TEXT_PREFIX = "Score: "
SCORE_TEXT_SIZE = 20


class GameScene(Scene):
    """ Welcome screen of the game, the first one to be loaded."""

    def __init__(self, game_state: GameState, scene_state: SceneState):
        super().__init__(game_state, scene_state)

    def process_input(self, events: List[Event]):
        self.game_state.player.handle_events(events)

    def update(self, time_delta: int):
        self.game_state.player.update(time_delta)

    def render(self, screen: Surface):
        screen.fill(BACKGROUND_COLOR)

        # Score in upper-left
        score_text = SCORE_TEXT_PREFIX + str(self.game_state.score)
        BASIC_FONT.render_to(screen, (5, 5), score_text, 'white', size=SCORE_TEXT_SIZE)

        # Player
        self.game_state.player.draw_player(screen)
